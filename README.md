# morse-api
Repository with an example of Morse encode/decode commands in Flask/Python

The project has the following structure:

```bash
.
├── app.py
├── controller
│   ├── controller.py
│   └── encoding
│       └── encoding_controller.py
├── services
│   ├── encoding
│   │   ├── encoders
│   │   │   ├── encoder.py
│   │   │   └── morse
│   │   │       └── morse_encoder.py
│   │   └── encoding_service.py
│   └── service.py
├── templates
│   └── index.html

```

This archtecture allows shared responsability, dividing in controllers and services, and uses patterns which permits extensionability and reuse of code such as creating more services and, in encoder service, creating more encoders. The morse encode logic used was a lib called morse3 (https://pypi.org/project/morse3/) but the archtecture permits change the implementation easilly with a decoupled code.

Usually, I would use some testing framework to do unit and integration tests but it will be added in the next refactor release. Such as, creating some pipeline of integration and deploy. I would deploy this project in a servless platform such as cloud function or cloud run of GCP to allows robustness and scalability.

This web app has one ux in index.html which collect the text and select the mode (encode or decode) and showing the result as illustrated by the figure below:

![image](https://user-images.githubusercontent.com/961104/144882145-d0b13ed1-659a-480f-b57c-4d53cf3c9b7b.png)

## run

The project was done using python3 and needed to install some dependencies such as flask framework and morse lib:
```
$pip install Flask
$pip install morse
```
The commands to set env variables and run the project is:
```
$export FLASK_APP=src/app.py
$export FLASK_ENV=development (used to development environment)
$flask run
```
