from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


with app.app_context():
    app.config["SQLAlchemy_DATABASE_URI"] = "sqlite:///:memory:"
    info = SQLAlchemy(app)
    CORS(app)
    class classroom(info.Model):
        id = info.Column(info.Integer, primary_key = True)
        Name = info.Column(info.String, nullable = False, unique = True)
        Grade = info.Column(info.Float, nullable = False, unique = False)
        def __init__ (self, Name, Grade):
            self.Name = Name
            self.Grade = Grade
    info.create_all()

def CreateJson(Class):
    json = {}
    for Student in Class:
        json.update({Student.Name:Student.Grade})   #! returns json into a dictionary
    return json
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/grades', methods = ['GET'])
def get_grades():
    return CreateJson(classroom.query.all()) 

@app.route('/grades/<id>', methods = ['GET'])
def get_student(id):
    return CreateJson(classroom.query.filter_by(Name = id))

@app.route('/grades' , methods = ['POST'])
def add_student():
    submission = request.get_json()
    Name = submission['name']
    Grade = submission['grade'] 
    Student = classroom(Name, Grade)
    info.session.add(Student)
    info.session.commit()
    return {Name:Grade}

@app.route('/grades/<id>', methods = ['PUT'])
def update_grade(id):
    submission = request.get_json()
    NewGrade = submission['grade']
    Student = classroom.query.filter_by(Name = id)
    Student = Student.update(dict(Grade = NewGrade))
    info.session.commit()
    return CreateJson(classroom.query.all())

@app.route('/grades/<id>', methods = ['DELETE'])
def delete_student(id):
    info.session.delete(classroom.query.filter_by(Name=id).first())
    info.session.commit()
    return CreateJson(classroom.query.all())

if __name__ == '__main__':
    app.run()