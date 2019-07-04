FROM python:3.6

WORKDIR /usr/src/app
ENV FLASK_APP server.py
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"

COPY . .

RUN apt-get update
RUN apt-get install bluetooth libbluetooth-dev -y
RUN pip install --no-cache-dir pipenv
RUN pipenv install

EXPOSE 5000
CMD ["pipenv", "run", "flask", "run", "-host=0.0.0.0"] 