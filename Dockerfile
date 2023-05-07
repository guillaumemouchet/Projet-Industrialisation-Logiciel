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

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
