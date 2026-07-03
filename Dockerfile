FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader stopwords punkt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]