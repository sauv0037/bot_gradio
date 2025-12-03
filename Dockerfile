FROM python:3.11

WORKDIR /app

COPY ./gradio .

RUN pip install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]
