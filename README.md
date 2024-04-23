# TermProjectProject

### Setting up the project
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
