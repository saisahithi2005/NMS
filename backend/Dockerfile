FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


FROM python:3.9
WORKDIR /app

COPY requirements.txt .  
RUN pip install -r requirements.txt  
COPY . .



CMD ["python", "main.py"]
