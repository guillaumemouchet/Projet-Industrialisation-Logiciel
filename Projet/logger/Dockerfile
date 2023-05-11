FROM python:3.10

RUN addgroup --system nonroot && adduser --system --ingroup nonroot nonroot

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN pip install Flask
#ENV FLASK_DEBUG=true

ENV FLASK_APP="logger.py"
ENV FLASK_RUN_PORT=8000
USER nonroot

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]