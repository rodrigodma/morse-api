# morse-api
Repository with an example of Morse encode/decode commands in Flask/Python

The project has the following structure:

root
+-- controller
|   +-- encoding
|   |   +-- encoding_controller.py
|   +-- controller.py
+-- services
|   +-- encoding
|   |   +-- encoders
|   |   |   +-- morse
|   |   |   |   +-- morse_encoder.py
|   |   |   +-- encoder.py
|   |   +-- encoding_service.py
|   +-- service.py

This structure allows share responsability and uses patterns which permits extensionability and reuse of code.
