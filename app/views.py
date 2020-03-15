"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import datetime 


from app import app
from flask import render_template, request, redirect, url_for, flash
from .profileform import AddProfileForm
from werkzeug.utils import secure_filename


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


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    """Render the website's profile page"""
    profileform = AddProfileForm()

    # if request.method == 'POST' and browsephoto.validate_on_submit():
    #     # Get file data and save to your uploads folder
    #     photo = profilephoto.photo.data

    #     filename = secure_filename(photo.filename)
    #     photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
    #     return render_template('profile.html', form=browsephoto)    
    if request.method == 'POST' and  profileform.validate_on_submit():
        firstname = profileform.firstname.data
        lastname = profileform.lastname.data
        gender = profileform.gender.data
        email = profileform.email.data
        location = profileform.location.data
        biography = profileform.biography.data
        profilephoto = profilephoto.profilephoto.data

    
    return render_template('profile.html', form=profileform)

###
# The functions below should be applicable to all Flask apps.
###

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
    ## Format the date to return only month and year date
    return "Joined " + date_joined.strftime("%B, %Y") 


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
