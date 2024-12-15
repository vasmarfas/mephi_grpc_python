FROM python:3.10-slim
# Устанавливаем рабочую директорию в контейнере
WORKDIR /ekassa
# Копируем файлы приложения в контейнер
COPY . /ekassa
# Устанавливаем зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Указываем порт, который будет открыт
EXPOSE 5000
# Команда для запуска прило
CMD ["python", "ekassa_server.py"]
