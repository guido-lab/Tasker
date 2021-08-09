# Tasker

## Tasker - Requirements
1. "Tasker" is a server that will run tasks by requests it will get from clients.
2. Each request will contain a task name and parameters.
3. There quest will be"sendandforget"-meaning the client doesn't expect a result immediately when running the task, only the UUID of the new task.
4. The result of a task should be written to a DB with some meta data (taskname and parameters, ip of the requester and timestamp)
5. Supported tasks:
- Sum two numbers
- Multiple three numbers

## Clone Project:
Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/guido-lab/Tasker.git
```

## Setup with Docker 
Build the app with the specified name "tasker"
```bash
sudo docker build -t tasker .
```

After the build have been finieshd successfully, run the container by specifying the name or CONTAINER_ID
```bash
sudo docker run tasker
```
The app is now running and available under the docker host. To find your docker IP you can use one of the below commands
```bash
sudo docker network inspect bridge | grep "Gateway"
```
```bash
sudo docker run tasker
```
The following command creates a new virtual environment named venv in the current directory:

```bash
$ python -m venv env
```

Activate virtual environment:

```bash
(Mac/Linux) $ source env/bin/activate
```

```bash
(Windows) $ source env/Scripts/activate
```

Install Dependencies:

```
$ pip install -r requirements.txt
```

Set Database (Make Sure you are in the same directory as manage.py):
```
$ python manage.py makemigrations
$ python manage.py migrate
```
Create SuperUser:
```
$ python manage.py createsuperuser
```

Run the development server:

```bash
$ python manage.py runserver
```


The project is runing at: **http://127.0.0.1:8000/**

Access admin pannel: **http://127.0.0.1:8000/admin**
