FROM python:3.11-alpine

COPY requirements.txt requirements.txt
COPY .env .env
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python3", "bot.py"]