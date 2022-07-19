FROM python:3.9.7
	
WORKDIR /test_app
	
# Устанавливем pip
RUN pip install --upgrade pip

# Открываем порты
EXPOSE 3000
EXPOSE 2000

# Копируем файл миграции
COPY requirements.txt .

# Устанавливем зависимости
Run pip install --upgrade setuptools
RUN pip install -r requirements.txt

# Копируем приложение
COPY . .

# Делаем миграции
CMD [python", "Migratedb.py", "db", "init"]
CMD [python", "Migratedb.py", "db", "migrate"]
CMD [python", "Migratedb.py", "db", "upgrade"]

# запускаем наше фласк приложение
CMD ["python", "run.py"]