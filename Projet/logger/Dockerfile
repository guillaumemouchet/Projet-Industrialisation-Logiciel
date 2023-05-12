FROM python:3.10

RUN addgroup --system nonroot && adduser --system --ingroup nonroot nonroot

WORKDIR /app/backend

COPY Projet/logger/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY Projet/logger/. .

#ENV FLASK_DEBUG=true

ENV FLASK_APP="logger.py"
ENV FLASK_RUN_PORT=8000
USER nonroot

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]