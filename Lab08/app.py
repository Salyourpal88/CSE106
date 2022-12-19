from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from flask_bcrypt import Bcrypt
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

import os

app = Flask(__name__)
CORS(app)

admin = Admin(app)

courses = os.path.abspath(os.path.dirname(__file__)) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(courses, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'EldenRing'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db = SQLAlchemy(app)
bcrypt = Bcrypt(app) 

class Icarus(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    course_id = db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
    class_name = db.Column('class_name', db.String)
    teacher = db.Column('teacher', db.String)
    time = db.Column('time', db.String)
    enrollment = db.Column('enrollment', db.Integer)
    capacity = db.Column('capacity', db.Integer)
    user = db.relationship('User', back_populates = 'lazy1')
    course = db.relationship('Course', back_populates = 'lazy2')

Teaches = db.Table('Teaches', 
    db.Column('Teacher_id', db.Integer, db.ForeignKey('teacher.id')),
    db.Column('Class_id', db.Integer, db.ForeignKey('course.id'))
)
class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    course_id = db.Column(db.String, unique = True)
    teacher = db.Column(db.String, unique = False) 
    time = db.Column(db.String, unique = False)
    enrollment = db.Column(db.Integer, unique = False)
    capacity = db.Column(db.Integer, unique = False)
    learners = db.relationship('Roster', back_populates = 'course')
    taughtBy = db.relationship('Teacher', secondary = Teaches, backref = 'taughtby') 
    lazy2 = db.relationship('Icarus', back_populates = 'course')
    def __init__(self, course_id, teacher, time, enrollment, capacity):
        self.course_id = course_id
        self.teacher = teacher
        self.time = time 
        self.enrollment = enrollment
        self.capacity = capacity

class Roster(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    class_id = db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
    grade = db.Column('grade', db.String)
    user = db.relationship('User', back_populates = 'scheduele')
    course = db.relationship('Course', back_populates = 'learners')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True, nullable = False)
    authentication = db.Column(db.String, nullable = False)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    scheduele = db.relationship('Roster', back_populates ='user')
    instructor = db.relationship('Attendance', back_populates ='user')
    lazy1 = db.relationship('Icarus', back_populates = 'user')
    def __repr__(self):
        return f'Student: {self.name}'   

class Teacher(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True, nullable = False)
    authentication = db.Column(db.String, nullable = False)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    philosopher = db.relationship('Attendance', back_populates = 'teacher')
    def __repr__(self):
        return f'{self.name}'
    
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    teacher_id = db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id'))
    user = db.relationship('User', back_populates = 'instructor')
    teacher = db.relationship('Teacher', back_populates = 'philosopher')

class Admins(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True, nullable = False)
    authentication = db.Column(db.String, nullable = False)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    
class RegisterForm(FlaskForm):
    authChoice = ["Student", "Teacher", "Admin(don't abuse thx)"]
    name = StringField(validators = [InputRequired(), Length(min = 4, max = 20)], render_kw={"placeholder" : "name"})
    authentication = SelectField('Role', choices=authChoice, validators=[InputRequired()], render_kw={"placeholder" : "authentication"})
    username = StringField(validators = [InputRequired(), Length(min = 4, max = 20)], render_kw={"placeholder" : "username"})
    password = PasswordField(validators = [InputRequired(), Length(min = 4, max = 20)], render_kw={"placeholder" : "password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username = username.data).first()
        if existing_user_username:
            raise ValidationError("That username already exists. Please choose a different one.") 

class LoginForm(FlaskForm):
    username = StringField(validators = [InputRequired(), Length(min = 4, max = 20)], render_kw={"placeholder" : "username"})
    password = PasswordField(validators = [InputRequired(), Length(min = 4, max = 20)], render_kw={"placeholder" : "password"})
    submit = SubmitField("Login")

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Teacher, db.session))
admin.add_view(ModelView(Admins, db.session))
admin.add_view(ModelView(Course, db.session))
admin.add_view(ModelView(Attendance, db.session))
admin.add_view(ModelView(Roster, db.session))

@app.route('/student', methods = ['GET'])
@login_required
def student():
    classes = Icarus.query.filter_by(user_id = current_user.id).all() 
    return render_template('student_page.html', classes = classes)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        if form.authentication.data == 'Student':
            new_user = User(name = form.name.data, authentication = form.authentication.data, username = form.username.data, password = hashed_password)
        elif form.authentication.data == 'Teacher':
            new_user = Teacher(name = form.name.data, authentication = form.authentication.data, username = form.username.data, password = hashed_password)
        else:
            new_user = Admins(name = form.name.data, authentication = form.authentication.data, username = form.username.data, password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('Register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if User.query.filter_by(username = form.username.data).first():
            user = User.query.filter_by(username = form.username.data).first()
        elif Teacher.query.filter_by(username = form.username.data).first():
            user = Teacher.query.filter_by(username = form.username.data).first()
        elif Admins.query.filter_by(username = form.username.data).first():
            user = Admins.query.filter_by(username = form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                if user.authentication == 'Student':
                    return redirect(url_for('student', name=user.name, ID=user.id))
                elif user.authentication == 'Teacher':
                    return redirect(url_for('instructor', name=user.name, ID=user.id))
                elif user.authentication == 'Admin':
                    return redirect(url_for('admin.index'))
    return render_template('login.html', form = form)

@app.route('/instructor', methods = ['GET'])
#@login_required
def instructor():
    instructorName = request.args.get('name') 
    instructorID = request.args.get('ID') 
    taughtClasses = Course.query.filter_by(teacher=instructorName).all()
    return render_template('instructor_page.html', displayName=instructorName, id=instructorID, courses=taughtClasses)

@app.route('/<int:id>/<string:className>', methods = ['POST'])
def changeGrade(id,className):
    #get current Teacher id and Course
    currentTeacher = Teacher.query.filter_by(id=id).first()
    thisClass = Course.query.filter_by(course_id=className).first() #query of Classes matching classname e.g. CSE106 
    #get new grade from student and their name from frontend
    newGrade = request.form.get("newGrade")
    selectedName = request.form.get("selectedName")
    #update db 
    selectStudentQuery = User.query.filter_by(name=selectedName).first() #create query of selected student
    selectGradeQuery = Roster.query.filter_by(user_id=selectStudentQuery.id).first() #get matching student id
    # selectGradeQuery = Enrollment.query.filter_by(student_id=selectStudentQuery.id, class_id=thisClass.id).first()
    selectGradeQuery.grade = newGrade
    db.session.commit()
    nameGradeTable = User.query.join(Roster, Roster.user_id==User.id).add_columns(User.name, Roster.grade).filter_by(class_id=thisClass.id).all()
    return render_template('class_1.html', course=thisClass, names=nameGradeTable, ID=id, displayName=currentTeacher)

    
@app.route('/<int:id>/<string:className>', methods = ['GET'])
# @login_required
def coursesTaught(id,className):
    currentTeacher = Teacher.query.filter_by(id=id).first()
    thisClass = Course.query.filter_by(course_id=className).first() #query of Classes matching classname e.g. CSE106 
    nameGradeTable = User.query.join(Roster, Roster.user_id==User.id).add_columns(User.name, Roster.grade).filter_by(class_id=thisClass.id).all()
    return render_template('class_1.html', course=thisClass, names=nameGradeTable, displayName=currentTeacher)

@app.route('/add', methods = ['GET', 'POST'])
@login_required
def add():
    if(request.method == "GET"):
        print("\n\n\n",current_user.id,"current_user")
        return render_template('add_courses.html', students = Course.query.all())
    if(request.method == "POST"):
        row = request.form.get("Add")
        one = User.query.filter_by(id = current_user.id).first()
        two = Course.query.filter_by(id = row).first()
        if(two.capacity == two.enrollment):
            flash("Sorry, but this class is full", "info")
            return redirect(url_for('add'))
        two.enrollment = two.enrollment + 1
        db.session.commit()
        three = Teacher.query.filter_by(name = two.teacher).first()
        new_course = Roster(user = one, course = two, grade = "null")
        new_scheduele = Icarus(user = one, course = two, class_name = two.course_id, teacher = two.teacher, time = two.time, enrollment = two.enrollment, capacity = two.capacity)
        new_student = Attendance(user = one, teacher = three)
        db.session.add(new_course) 
        db.session.add(new_student) 
        db.session.add(new_scheduele)
        db.session.commit()
        flash("Class added!", "info")
        return redirect(url_for('add'))

@app.route('/logout', methods = ['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run()

with app.app_context():
    db.create_all()