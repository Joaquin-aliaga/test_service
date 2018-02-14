FROM python:2.7.14-stretch

WORKDIR /app
COPY python .

RUN python --version
RUN pwd
RUN pip install -r requirements.txt
CMD cd test && pytest