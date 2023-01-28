# Where To Go (WTG):
A website for the tourists in Armenia where they can find an interesting places to visit.

### Where is the website?
Just click [here](http://ash28.pythonanywhere.com/).

### How to add more content?
- Move to the [admin](http://127.0.0.1:8000/admin) panel and log in:

<img src="repo_images/img.png" width="300" alt="img">

- After log in go to Places:

<img src="repo_images/img1.png" width="300" alt="img">

- Then you can find the location in the search field or choose from the list and add
a new place clicking on Add place on the right side of the admin panel:

<img src="repo_images/img3.png" width="300" alt="img">

After all this steps you can manage post. Note that you can swap uploaded images:

<img src="repo_images/gif.gif" width="400" alt="img">

To add a new user with access to manage data go to Users catalog and create a new user,
then in Permissions add Staff status and set User permissions.


### How to execute:

- Download or clone [repo](https://github.com/Ash2803/where-to-go.git)
- You must have Python 3.9 or higher already installed;
- Create the virtual environment using command:
```
python3 -m venv venv
```
- Install the requirements using command:
```
pip install -r requirements.txt
```
- Create `.env` file and set environment variables `SECRET KEY` and `DEBUG` = default is False.
- Then create a DB by running `makemigrations` and `migrate` command:
```
python manage.py makemigrations
python manage.py migrate
```
- Create superuser and put your login, email and password:
```
python manage.py createsuperuser
```
- Run the server:
```
python manage.py runserver
```

Read the section ["How to add more content?"](#how-to-add-more-content) to find out how to add new data to website.

### Project Goals

The projects made for educational purposes at online-course for web-developers [dvmn.org](https://dvmn.org/)
