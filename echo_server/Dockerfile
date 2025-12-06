FROM python:3.13-alpine

EXPOSE 8000
WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app .

CMD ["python","main.py"]