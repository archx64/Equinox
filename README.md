# Social Network with Facial Authentication

## Project Description 

This project focuses mainly facial recognition using Deep learning

Django framework is used for backend and Bootstrap4 is used for frontend.

Redis server is used for chat.

The face_recognition by [Adam](https://github.com/ageitgey/face_recognition) is used for recognize users and identify them. 

Thanks to Corey Schafer for helping me learn Django

It's better if you have a CUDA compatible GPU so identifying users will be faster.

### Required Python packages

`
face_recognition
dlib
channels
channels-redis
django
django-crispy-forms
django-extensions
opencv-python
`

Redis server must be running for asynchronous programming

### How to deploy

Clone this repository. Find the settings.py. Set your external ip as allowed hosts.

Go to root directory and type `python manage.py runserver 0.0.0.0:8000` to run 


### Contribution

Opinion mining, suggestions and improved chat is in development and not ready to implement. Your contributions will be very helpful.
