FROM python:2.7.13-alpine
LABEL maintainer="9to5, ktk0011-dev@gmail.com"
LABEL repository="https://github.com/9to6/slackbot"

ADD src /app

WORKDIR /app
RUN ls
RUN pip install -r ./requirements.txt

ENTRYPOINT ["python", "run.py"]

