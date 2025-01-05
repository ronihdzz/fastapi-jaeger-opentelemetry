# FastAPI with OpenTelemetry and Jaeger

![Jaeger](docs/architecture.png)

This project is a test of how to integrate OpenTelemetry and Jaeger into a FastAPI application.

## Prerequisites

- Docker
- Docker Compose (to run jaeger)
- Python (to run the API)
- virtualenv or venv (to create the virtual environment)

## Run jaeger with docker-compose

```
docker-compose up jaeger
```

## Create the virtual environment

To install the necessary dependencies, a virtual environment must be created with python.

* Below is how to do it with venv

```
python -m venv nombre_del_entorno
```

* An alternative to venv is virtualenv, below is how to do it with virtualenv with a python 3.11

```
virtualenv nombre_del_entorno -p=3.11
```

## Activate the virtual environment

To activate the virtual environment, from your console in linux or mac, execute the following command:

```
source nombre_del_entorno/bin/activate
```

## Install the dependencies

To install the necessary dependencies, execute the following command:

```
pip install -r requirements_with_versions.txt
```


## Different ways to run the project

### Run the project from console:

To run the project, execute the following command:

```
uvicorn main:app --port 9000 --reload
```

### Run the project from docker-compose:

To run the project, execute the following command:

```
docker-compose up troni-api
```

### Run the project with vscode debugger

You must have vscode installed and the python debugger installed.

In the left tab, in the "Debug" section, click on the "Run and Debug" icon and select "Python Debugger: FastAPI" this configuration is in the .vscode/launch.json file



## Test that it works

To test the integration, you must make requests to the API, below I show different ways to do it.

### API request

With the help of curl, you can make requests to the API from the console, for example:

```
curl http://localhost:9000/health
```

If you don't have curl installed, you can simply visit the following url in your browser:

```
http://localhost:9000/health
```

If you prefer to make requests in a more visual way, you can visit the following url that fastapi generates: http://localhost:9000/docs and from the documentation that is displayed with swagger you can test the API endpoints

### View the data in Jaeger

After making several requests to the API, you should see the data in Jaeger. To do this, you can visit the following URL:

```
http://localhost:16686/
```

