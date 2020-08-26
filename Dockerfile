FROM tensorflow:nightly-py3-jupyter

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3","app.py"]