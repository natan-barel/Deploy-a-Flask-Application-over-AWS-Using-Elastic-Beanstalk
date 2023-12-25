from flask import Blueprint, render_template
from .models import Course
from . import db
import json
from flask import request
auth = Blueprint('auth', __name__)

@auth.route('/')
def login():
    query = request.args.get('query')
    print(query)
    if query:
        courses = Course.query.filter(Course.title.contains(query)) or Course.overview.contains(query)
        print(courses)
    else:
        courses = Course.query.all()
    return render_template('login.html', course=courses)

@auth.route('/loaddata')
def signup(): 
    # Opening JSON file
    f = open('courses.json')

    # Load JSON object as an dictionary
    courses = json.load(f)

    # Importing Coruse Model
    from .models import Course
    
    # Adding all courses to the database
    for course in courses:
        # Creating a new Course
        new_course = Course(title=course['title'], author=course['author'], overview=course['overview'], image=course['img'], url=course['url'])
        # Adding course to database
        db.session.add(new_course)
        db.session.commit()
    # Closing File
    f.close()
    # Success Message
    return "Data Loaded Successfully"