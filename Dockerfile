FROM python:3.11-slim

WORKDIR /myapp

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /myapp/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /myapp/requirements.txt

COPY . /myapp/

# Make the entrypoint script executable
COPY entrypoint.sh /myapp/
RUN chmod +x /myapp/entrypoint.sh

ENTRYPOINT [ "/myapp/entrypoint.sh" ]
