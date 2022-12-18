from flask import Flask, render_template, request
from flask_cors import CORS

import json
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/grades', methods = ['GET'])
def get_grades():
    grades = json.load(open('grades.json'))
    return grades

@app.route('/grades/<id>', methods = ['GET'])
def get_student(id):
    grades = json.load(open('grades.json'))
    if id in grades:
        return {id: grades[id]}

@app.route('/grades' , methods = ['POST'])
def add_student():
    submission = request.get_json()
    grades = json.load(open('grades.json'))
    grades[submission['name']] = submission['grade']
    add_json = open("grades.json", "w")
    json.dump(grades, add_json)
    add_json.close()
    return grades

@app.route('/grades/<id>', methods = ['PUT'])
def update_grade(id):
    grades = json.load(open('grades.json'))
    if id in grades:
        submission = request.get_json()
        grades[id] = submission['grade']
        add_json = open("grades.json", "w")
        json.dump(grades, add_json)
        add_json.close()
        return grades

@app.route('/grades/<id>', methods = ['DELETE'])
def delete_student(id):
    grades = json.load(open('grades.json'))
    if id in grades:
        del grades[id]
        add_json = open("grades.json", "w")
        json.dump(grades, add_json)
        add_json.close()
        return grades

if __name__ == '__main__':
    app.run()