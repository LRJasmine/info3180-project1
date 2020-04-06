"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
from datetime import datetime

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from .profileform import AddProfileForm
from werkzeug.utils import secure_filename
from .models import UserProfile


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/profile', methods=["POST", "GET"])
def profile():
    """Render the website's profile page"""
    profileform = AddProfileForm()
    

    if request.method == "POST":
        
        if profileform.validate_on_submit():
            
            if profileform.gender.data=='default':
                flash('Please select gender')
                
            firstname = profileform.firstname.data
            lastname = profileform.lastname.data
            gender = profileform.gender.data
            email = profileform.email.data
            location = profileform.location.data
            biography = profileform.biography.data
            profilephoto = profileform.profilephoto.data
            date_created = datetime.utcnow()
            print(gender)
            photofilename = secure_filename(profilephoto.filename)
            profilephoto.save(os.path.join(app.config['UPLOAD_FOLDER'], photofilename))
        
            user = UserProfile(firstname,lastname,gender,email,location,biography,photofilename,date_created)
            db.session.add(user)
            db.session.commit()
        
            flash('Profile was sucessfully added', 'success')
            return redirect(url_for('profiles'))
            
    return render_template('profile.html', form=profileform)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/profiles', methods=['POST', 'GET'])
def profiles():
    users = UserProfile.query.all()
        
    return render_template('profiles.html', users=users)

@app.route('/profile/<userid>', methods=['POST'])
def oneprofilepage(userid):

    user = UserProfile.query.filter_by(id=userid).first()
    userdate = format_date_joined(user.date_joined)
    

    return render_template('oneprofilepage.html', profile=user, userdate=userdate)

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


def format_date_joined(date_joined):
    ## Format the date to return day, month and year date
    return "Joined on " + date_joined.strftime("%A %B %d, %Y") 


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
