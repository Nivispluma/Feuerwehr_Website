FROM python:3.7.3

WORKDIR /app
COPY . .

RUN git pull https://github.com/Nivispluma/Feuerwehr_Website.git
RUN pip install -r requirements.txt


ENTRYPOINT ["python"]
CMD ["app.py"]