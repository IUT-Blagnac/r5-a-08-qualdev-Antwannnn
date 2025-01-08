# J'utilise un docker pour exécuter les tests pour être sûr que ça marche partout
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY password_generator.py .
COPY features/ ./features/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["behave", "--format", "pretty"] 