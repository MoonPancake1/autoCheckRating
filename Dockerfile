FROM python:3.11.3

WORKDIR /auto_check_vuz_ratings
ADD requirements.txt /auto_check_vuz_ratings

RUN pip3 install -r requirements.txt

ADD . /auto_check_vuz_ratings

ENTRYPOINT ["python3", "main.py"]