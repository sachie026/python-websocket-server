# Getting Started with Python websocket server app

### Modules used

**asyncio:** Asynchronous IO.\
**random :** generate random numbers.\
**websockets :** To create a webscoket connection.

## Available Scripts

In the project directory, you can run:

### 👇️ in a virtual environment or using Python 2

pip install -r requirements.txt

### 👇️ if you use Python 3 outside a virtual environment

pip3 install -r requirements.txt

### 👇️ if you don't have pip in your PATH environment variable

python -m pip install -r requirements.txt

### 👇️ for python 3 (could also be pip3.10 depending on your version)

python3 -m pip install -r requirements.txt

### `python/python3 server.py`

Runs the app in the development mode.\
Open Postman and create new request in socket.io mode with [ws://localhost:7890](ws://localhost:7890)

On successful connection you will see **Connected to ws://localhost:7890** in Postman app.
And you will see **A client just connected** on the terminal where you started your server from.
