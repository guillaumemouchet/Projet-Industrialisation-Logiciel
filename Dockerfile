FROM python:3.10

WORKDIR /app

COPY Projet/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./Projet .

#ENV FLASK_DEBUG=true

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
