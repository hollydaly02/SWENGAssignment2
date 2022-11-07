# init a base image
FROM python:3.9.1
# update pip to minimize dependency errors
RUN pip install --upgrade pip
# define the present working directory
WORKDIR /docker-flask-test
# copy the contents into the working dir
ADD . /docker-flask-test
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# declare environment variable
ENV FLASK_APP=Calculator.py
# define ports
EXPOSE 5000
# configures container to run as exectutable
ENTRYPOINT ["flask"]
# define the command to start the container
CMD ["run", "--host=0.0.0.0", "-p", "5000"]
