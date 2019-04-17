import os
curent_path = os.path.abspath(os.path.dirname(__file__))
os.system('python ' + curent_path + '/manage.py runserver 0.0.0.0:8000')