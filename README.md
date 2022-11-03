#RL Backend

## This service is used to store and retrieve kinematic data of a body.


#Running RL Backend:

## Clone repository and create a .env file in the root


## Fill in details of .env file

```
SECRET_KEY=django-insecure-728k0bs%91o$^sp%aa_ji@2fmtwpdk7r1na#*$%l2+%)7tnpo3
DB_NAME=rlbackend
DB_USER=db_user
DB_PASSWORD=password123
DB_HOST=localhost
DB_PORT=5432
```

## Create python venv with Python3

## source or activeate venv

```
pip install requirements.txt

python manage.py migrate
```

## Run tests with:

```
python manage.py test

python manage.py runserver

```



## API endpoint:: localhost:8000/data
