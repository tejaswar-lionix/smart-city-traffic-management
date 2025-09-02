FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends git nodejs npm curl && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY package.json package-lock.json ./
RUN npm install || true
COPY . .
EXPOSE 8000 3000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
