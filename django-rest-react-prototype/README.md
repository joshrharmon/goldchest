## Simple test application for React and Django REST

Tutorial from https://www.valentinog.com/blog/drf/
<br/>

To run this, you will need a python environment with djangorestframework <br/>
Activate your virtual environment and run
```pip install djangorestframework```

<br/>
<br/>

To build the frontend, navigate to the frontend directory run
```npm install && npm run dev```

<br/>

Once that is done, with your environment activated, run
```python manage.py runserver```

<br/>

Any time changes are made to the server, navigate to frontend directory and run
```npm run dev```

<br/>

Note: if you are encountering problems with installing the build, try deleting
frontend/node_modules and do
```npm install && npm run dev```
