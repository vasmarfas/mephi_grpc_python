FROM python:3.10-slim
RUN ls

# Устанавливаем рабочую директорию в контейнере
WORKDIR /usermanager
# Копируем файлы приложения в контейнер
COPY . /usermanager
RUN ls -l /usermanager

# Устанавливаем зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Указываем порт, который будет открыт
EXPOSE 5000
# Команда для запуска прило
CMD ["python", "usermanager_server.py"]
