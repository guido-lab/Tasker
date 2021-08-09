# Tasker

## Tasker - Requirements
1. "Tasker" is a server that will run tasks by requests it will get from clients.
2. Each request will contain a task name and parameters.
3. There quest will be"sendandforget"-meaning the client doesn't expect a result immediately when running the task, only the UUID of the new task.
4. The result of a task should be written to a DB with some meta data (taskname and parameters, ip of the requester and timestamp)
5. Supported tasks:
- Sum two numbers
- Multiple three numbers
#
## Clone Project:
Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/guido-lab/Tasker.git
```
#
## Setup with Docker 
Build the app with the specified name "tasker"
```bash
sudo docker build -t tasker .
```

After the build have been finieshd successfully, run the container by specifying the name or CONTAINER_ID
```bash
sudo docker run tasker
```
The app is now running and available under the docker host. 
```bash
http://DOCKER_IP:8000/
```
To find your docker IP you can use one of the below commands
```bash
sudo docker network inspect bridge | grep "Gateway"
```
```bash
sudo docker inspect CONTAINER_ID | grep "IPAddress"
```
#
## Setup Manually 
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

#
## How to use it


There are only two tasks as example available "SumTwoNumbers" and "MultipleThreeNumbers"

The below Endpoint allows you to make a POST request the task name and task parameters as a body payload and the as the result is expected a UUID

```bash
http://host:8000/api/core/tasker/
```
Method "POST" , params as body(Postman):
```
{
    "task_name": "SumTwoNumbers",
    "params": {
            "num_one": 5,
            "num_two": 5
        }
}
```

```
{
    "task_name": "MultipleThreeNumbers",
    "params": {
            "num_one": 5,
            "num_two": 5,
            "num_three": 5
        }
}
```

The user will receive a unique UUID of the task that he executed. The user is able to check the task execution and the result by filtering in the endpoint 
```
http://HOST:8000/api/core/task-results/?task_uuid=<YOUR_UUID>
```
The available parameters to filter the executed tasks are `id=&task=&task_uuid=&requester_ip=`

#
There is also possible to add new functions as well by creating the function under the `helperScripts/taskFunctions.py` and registering the task by accessing the Django Admin page `http://HOST:8000/admin/core/task/`


