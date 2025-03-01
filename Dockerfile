# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt /app/requirements.txt

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . /app

# command to run on container start
# CMD [ "python", "main_flask_server.py" ]

ENTRYPOINT [ "python" ]

CMD [ "main_flask_server.py" ]