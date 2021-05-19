#! /bin/bash
cd backend && python3 backendStart.py &
cd django-rest-react-prototype && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
