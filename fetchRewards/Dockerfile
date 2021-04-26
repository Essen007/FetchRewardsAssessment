FROM python:3.6-alpine
WORKDIR /project
ADD . /project
RUN pip3 install -r requirements.txt
EXPOSE 3000
CMD [ "python3","api.py" ]