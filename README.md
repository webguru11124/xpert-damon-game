
### 👉 Set Environment

1. Install Python = 3.11

2. Install NPM v16

3. Run powershell.exe as administator and Execute follow command
 
Set-ExecutionPolicy RemoteSigned -Force


### 👉 Start Project

> **1.Setup virtual environment & Install Requirements**

```bash
$ python -m venv env
$ .\env\Scripts\activate.ps1
$ pip install -r requirements.txt
```

> **2.Migrate Database**

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> **3.Start Server**

```bash
$ python manage.py runserver
```