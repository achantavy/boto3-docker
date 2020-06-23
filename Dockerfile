FROM python:3.7-slim

ENV HOME /home

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["pip", "freeze"]
