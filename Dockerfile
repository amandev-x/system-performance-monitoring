FROM python:3.11-slim AS build 
WORKDIR /app 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
COPY . .

FROM python:3.11-slim AS runtime 
WORKDIR /app 
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /app /app 
EXPOSE 5001 
CMD ["python", "monitor.py"]