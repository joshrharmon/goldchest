## Simple test application for React and Django REST

Tutorial from https://www.valentinog.com/blog/drf/
<br/>

To run this, you will need a python environment <br/>
Activate your virtual environment and run
```python -m pip install -r requirements.txt```

<br/>

To build the frontend, navigate to the frontend directory run
```npm install```
then run ```npm run dev```

<br/>

Any time changes are made to the server, navigate to frontend directory and run
```npm run dev```

<br/>

Note: if you are encountering problems with installing the build, try deleting
frontend/node_modules and run
```npm install```
then run ```npm run dev```
<br/>

To start the backend server, go back to goldchest and into backend directory and run
```python backendStart.py```

If you run into CORS error, please install this extention
https://chrome.google.com/webstore/detail/moesif-origin-cors-change/digfbfaphojjndkpccljibejjbppifbc?hl=en-US

<br/>

Once that is done, go into django-rest-react-prototype folder, with your environment activated, run
```python manage.py runserver```

