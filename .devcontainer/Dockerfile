FROM python:3.11-slim

ENV TZ=Europe/Moscow

# system deps
RUN apt-get update && apt-get install -y \
    curl \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Node.js 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

WORKDIR /workspace
