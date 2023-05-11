FROM python:3.10

RUN addgroup --system nonroot && adduser --system --ingroup nonroot nonroot

WORKDIR /app

COPY Projet/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./Projet .

#ENV FLASK_DEBUG=true
ENV FLASK_APP="main.py"

USER nonroot

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
