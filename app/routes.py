from app import app
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/index')
def index():
    hobbies = ['Skiing', 'Music', 'Basketball', 'Xbox']

    return render_template('index.html', title='Home', hobbies=hobbies)

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html', name='Ben Gilman', title='About Me', description='Toward the end of college I knew I wanted to work in some field of engineering. I like working on projects, solving problems, and using computers. I spent a lot of time on the internet looking at career paths trying to figure out what would be right for me. Everything I found seemed to point to software. Software is used in our everyday lives and it is basically taking over the world. I knew a few kids who were programmers, some with a CS degree and others who went to bootcamps. They gave me a few websites to practice on (for example FreeCodeCamp), and after playing around on those sites for a few months I applied to Coding Temple. It can definitely be frustrating and it will be difficult to learn, but it seems that once you get the hang of it the possibilities will be endless.')
