# rest_api_in_django
a REST api developed using Django-rest-framework

## Requirements
1. django
2. djangorestframework
3. pillow
4. opencv-python (optional)

## Instructions to test the working
1. pip install django, djangorestframework, pillow, opencv-python(optional)
2. cd to project repo and run 
```python manage.py runserver 8975```
3. fire up postman or something similar and send a post request to ```127.0.0.1:8975/restApi/sendImage/``` with image attached as file with key value ```image```
![instructions in postman image](https://github.com/santhtadi/rest_api_in_django/blob/master/readme_images/tutorial.png)

