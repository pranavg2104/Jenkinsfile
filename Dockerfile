FROM python:3.7-alpine

COPY helloworld.py

CMD ["python", "helloworld.py"]
