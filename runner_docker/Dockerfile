FROM python:3.9

WORKDIR /home

COPY ./requirements.txt /run/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /run/requirements.txt

ADD ./DataPane-clone /home/datapane/

COPY ./report_runner.py /run/report_runner.py

RUN pip install --no-cache-dir /home/datapane

CMD ["python3", "/run/report_runner.py"]

