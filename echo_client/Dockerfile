FROM python:3.13-alpine

EXPOSE 8501
WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app .

CMD ["streamlit", "run", "main.py"]