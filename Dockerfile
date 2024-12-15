FROM python:3.10-slim
# Устанавливаем рабочую директорию в контейнере
WORKDIR /app
# Копируем файлы приложения в контейнер
COPY . /app
COPY /ekassa/ekassa_pb2_grpc.py /app/ekassa_pb2_grpc.py
COPY /usermanager/usermanager_pb2_grpc.py /app/usermanager_pb2_grpc.py
COPY /ekassa/ekassa_pb2.py /app/ekassa_pb2.py
COPY /usermanager/usermanager_pb2.py /app/usermanager_pb2.py

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Устанавливаем зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Указываем порт, который будет открыт
EXPOSE 5000
# Команда для запуска прило
CMD ["python", "main.py"]
