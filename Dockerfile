FROM python:3.7-alpine
RUN pip install requests
COPY helloworld.py
CMD ["python", "helloworld.py"]
