FROM python:3.10-slim

WORKDIR /app

COPY app /app/app
COPY start.sh /app/start.sh

RUN pip install --upgrade pip
RUN pip install -r /app/app/requirements.txt

RUN chmod +x /app/start.sh

EXPOSE 8000 8501

ENTRYPOINT ["/app/start.sh"]
