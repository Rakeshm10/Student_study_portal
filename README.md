A Student Study portal is a web-based platform designed to enhance the educational experience for students.
The platform aims to create a complete and effective learning ecosystem by combining key tools such as digital note-taking, Assignment management, Schedule, and integration of external resources such as Google Wikipedia, e-books, and YouTube.
In conclusion, the Student Learning Portal represents a state-of-the-art solution that provides students with the tools they need to succeed academically.
By providing a comprehensive and integrated platform, this initiative aims to redefine how students engage in their studies, ultimately contributing to more enriching and effective learning.





first, we need to create a virtual environment for this project using the command
mkvirtualenv Student_study_portal  


After successfully creating a virtual environment install Django  :
pip install Django


To create a project:
django-admin startproject student_study_portal


After creating a project go inside the project directory
cd Student_study_portal

To run a project now use the command python manage.py runserver

To create a superuser use the command python manage.py createsuperuser

After successfully changing any classes in the database run the commands 
python manage.py makemigrations
and python manage.py migrate






