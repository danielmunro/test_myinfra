FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN apk add --no-cache --update python3
RUN apk add --no-cache gcc linux-headers musl-dev
RUN pip install -r requirements.txt
CMD ["python", "app.py"]