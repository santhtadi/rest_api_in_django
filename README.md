# rest_api_in_django
a REST api developed using Django-rest-framework

## Requirements
1. django
2. djangorestframework
3. opencv-python
4. pillow

## Instructions to test the working
1. pip install django, djangorestframework, opencv-python, pillow
2. cd to project repo and run 
```python manage.py runserver -p 8975```
3. fire up postman or something similar and send a post request to ```127.0.0.1:8975/SendImage/``` with image attached as file with key value ```image```


