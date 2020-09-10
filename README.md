## ATA Freight | Python Web Development


## How to create a virtual environment in your system


first install the virtualenv library

`pip install virtualenv`

to create virtual environment name "venv"


`virtualenv venv `

to activate it 

`venv\Scripts\activate.bat`     in windows

now install the requirements 

`pip install -r requirements.txt`

now run the local server to see things working fine 


`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

- go to the browser open up the url [localhost:8000](http://localhost:8000/)
- Sign up ( Manager, Admin, Employee)
- Login
- Employee can create the leave application with leave start date, end date, description and total leaves available (Default=30)
- Manager Can approve the application including detail view of application.
- Admin can acess the adminstrator site where can only change application status and View all things , Won't be able to add anything. Except View of everything.
- On approval from Manager , Number of leave will de decducted from employee total available leave
