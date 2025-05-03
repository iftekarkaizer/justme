FROM python:3.10-slim

WORKDIR /app/myapp

RUN apt-get update -y
RUN apt-get upgrade -y 
RUN apt-get install gcc libpq-dev -y
RUN rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
