# TermProject - FormHub

## Members and Contributions
### 6441142126 Punyachart Phorkathong (Pun)
- Set up the backbone for the project including:
    - Split the application by its functionality.
    - Initialized Django models in each application's models.py file.
    - Configured the path of the template and static directories
    - Connected the application's database to local PostgreSQL
- Completed the core functionality of creating and answering the surveys which mainly on JavaScript.
- Completed the functionality of exporting the survey responses in MS Excel file utilizing xlsx CDN.
- Created the seed.py to initialize the sample data for the web application.

### 6441055226 Chindanai Rungrotkittisin (Bank)
- Designed UI, create HTML and CSS for redeem, user profile, and registration
- Reviseed models related to Redeem module
- Initialised both front and back end for Redeem, and User Profile sharing tasks with Title

### 6441093026 Thananchai Pariyavatkul (Title)
- Back-end userprofile: upload pic, edit user info coding in views.py and javascript.
- Back-end Redeem: Show current point, Record point that redeem in database, alert & hide button when click redeem discount&prize, coding in views.py and javascript.
- Upload pic & show when create a form.
- A little bit front-end in Redeem & userprofile sharing tasks with Bank

## Features
### Core Functionalities:
- Authentication:
    - Register and Login system with various form validation
    - One account can both create and answer forms
- Index Page: shows open forms
- Answering surveys
- User Profile: show user's forms, and purchased datasets
- Redeem Page:
    - Deducting points to convert to cash, redeem discounts, and win the prizes
    - Showing only the redemptions that haven’t used
    - Showing only selling datasets
### Additional functionalities (not taught in the course):
- Creating Forms: Employed Java Script to dynamicly add new sections and choices
- Uploading pictures to database (user profile, and form header picture)
- Storing answers as JSON format
- Downloading Datasets as Microsoft Excel file

## Setting up the project
1. Clone the repository and change directory into the root of the project
```shell
git clone https://github.com/ChindanaiR/FormHubProject.git
cd FormHubProject
```

2. Set up the virtual environment

**For Windows**
```shell
python -m venv .venv
```
**For Mac**
```shell
python3 -m venv .venv
```

3. activate the virtual environment

**For Windows**
```shell
./.venv/scripts/activate
```
**For Mac**
```shell
source ./.venv/bin/activate
```

4. Install the required packages
```shell
pip install -r requirements.txt
```

5. Create and set up the `.env` file in the root directory of the project.
```text
DB_HOST="localhost"
DB_USER="postgres"
DB_PASS="yourpassword"
DB_NAME="your databasename"
DB_PORT="5432"
SECRET="thesecretkey"
```

6. Migrate the database models.

**For Windows**
```shell
python manage.py migrate
```
**For Mac**
```shell
python3 manage.py migrate
```

7. Run `seed.py` to initilize data.

**For Windows**
```shell
python seed.py
```
**For Mac**
```shell
python3 seed.py
```

8. Lastly, Run server!
```shell
python manage.py runserver
```

### Framework documentation

- Django 5.0.3 [[Click here](https://docs.djangoproject.com/en/5.0/)]
- Bootstrap 5.0.2 [[Click here](https://getbootstrap.com/docs/5.0/components/navbar/)]
- Font Awesome 6 [[Click here](https://fontawesome.com/icons)]
