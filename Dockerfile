# Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# default command runs the GUI app (note: GUI inside container may not display without X forwarding)
CMD ["python", "aceest_fitness/app_v1_3.py"]
