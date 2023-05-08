FROM python:3.10

WORKDIR /app

COPY Projet/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./Projet .

#ENV FLASK_DEBUG=true

#- FLASK_APP=main.py flask run --debug &
#- cd logger
#- export FLASK_RUN_PORT=8000
#- FLASK_APP=logger.py flask run --debug &
#- cd ..
RUN FLASK_APP=main.py
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]

RUN FLASK_APP=logger.py
RUN cd logger
RUN export FLASK_RUN_PORT=8000
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
