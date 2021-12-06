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

This structure allows share responsability and uses patterns which permits extensionability and reuse of code.
