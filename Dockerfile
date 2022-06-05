FROM python:3.7.3

RUN git pull https://github.com/Nivispluma/Feuerwehr_Website.git

WORKDIR /app
COPY . .


RUN pip install -r requirements.txt


ENTRYPOINT ["python"]
CMD ["app.py"]