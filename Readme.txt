# Я использую OS Windows 10 x64
# Сначала делаем миграцию базы данных
# убедитесь что у вас нет DB "orders" и в ней нет таблицы order_table 
# и вы не используете такую же в другом проекте
# Я использую пользователя postgres с паролем postgres
# создал и использую пустую DB "orders", измените на вашу
# Поменять базу данных, пользователя и пароль
# вы можете в файле ./curr_conv/Config.py в строке 4

pip install Flask-Migrate==2.6.0
python Migrate db init
python Migrate db migrate
python Migrate db upgrade


1. Сборка доккер образов
    # Перед сборкой не забудьте поменять данные для базы в файле curr_conv/Config.py
    # Поменяйте localhost на host.docker.internal в строке 4
    # Чтобы заменить пользователя телеграм, которому отправляется сообщение
    # В файле curr_conv/Config.py замените параметр chat_id в 15 строке
    # который вы можете получить у бота @getmyid_bot отправив /start

    # Убедитесь, что Docker Desktop включён и выполните команду 
    docker build curr_conv .

    # Убедитесь что в файле pg_hba.conf вашего postgres присутствует следующая строка

host    all             all             0.0.0.0/0            md5

    # я разрешаю доступ всем устройствам к базе , так что это не очень безопасно, после работы с приложением
    # уберите.

    docker run --add-host host.docker.internal:host-gateway -p 2000:2000 curr_conv

    # Теперь переходим в папку с web страницой на реакте
    cd frontend

    # Устанавливаем зависимости react:
    npm i react react-dom socket.io-client react-table reactstrap react-table
    # Либо по очереди
    npm i react
    npm i react-dom
    ...
    # если не хватило какого-то пакета, просто скачайте его по ошибке в консоли

    # делаем docker build
    docker build frontend . 
    docker run -p 3000:3000 frontend
    # Нажмите на консоль и Enter пару раз, если консоль зависла

    # Затем перейдите на страницу http://127.0.0.1:3000/
    # Таблица может загрузиться не сразу, подождите некоторое время
    # Дальше перейдите по ссылке https://docs.google.com/spreadsheets/d/1wCa9s91PxlkQPDS6pxIsR7-2xB7NMDvvmo1VPhaV0Co/edit?usp=sharing

    # и поменяйте какие нибудь значения в таблице


2. Запуск исходников
    # Устанавливаем зависимости python
    pip install requirements.txt
    
    # Устанавливаем свой chat_id в 15 строке curr_conv/Config.py
    # chat_id получаем у бота @getmyid_bot
    
    # Запускаем
    # python run.py
    
    # переходим в директорию ./frontend
    # npm должен быть установлен
    # Устанавливаем зависимости react:
    npm i react react-dom socket.io-client react-table reactstrap react-table
    # Либо по очереди
    npm i react
    npm i react-dom
    ...
    # если не хватило какого-то пакета, просто скачайте его по ошибке в консоли

    # Затем запустите приложение
    npm start
    # Нажмите на консоль и Enter пару раз, если ненадолго зависнет

    # Затем перейдите на страницу http://127.0.0.1:3000/
    # Таблица может загрузиться не сразу, подождите некоторое время
    # Дальше перейдите по ссылке https://docs.google.com/spreadsheets/d/1wCa9s91PxlkQPDS6pxIsR7-2xB7NMDvvmo1VPhaV0Co/edit?usp=sharing

    # и поменяйте какие нибудь значения в таблице
    # подождите пока Google сохранит данные в таблице

    # Перейдите на страницу и вы увидите, что данные изменяются достаточно быстро

    # Можете попробовать писать некорректные данные и пробовать "сломать" приложение

    # Надеюсь, у вас не получится:)

    # Если появятся ошибки пишите мне в телеграм @Goodguy111


3. Запуск готовых доккер образов (доккер образы фронта и бэка весят в общем 2 гб и можете получить их у меня)
    # Вы можете загрузить готовый образ:
    docker load -i curr_conv.zip

    # Убедитесь что в файле pg_hba.conf вашего postgres присутствует следующая строка

host    all             all             0.0.0.0/0            md5

    # я разрешаю доступ всем устройствам к базе , так что это не очень безопасно, после работы с приложением
    # уберите.

    # Чтобы заменить пользователя телеграм, которому отправляется сообщение
    # В файле curr_conv/Config.py замените параметр chat_id в 15 строке
    # который вы можете получить у бота @getmyid_bot отправив /start
    # заменить текст в доккер контейнере вы можете с помощью Vscode - extensions - Remote - Containers
    # вот инструкция: https://www.howtogeek.com/devops/how-to-edit-code-in-docker-containers-with-visual-studio-code/
    # затем нужно сделать docker commit curr_conv curr_convimage:version1
    # и запустить образ

    # Таким же образом можно поменять пользователя базы данных/пароль в строке 4

    # Запустите бэк
    docker run --add-host host.docker.internal:host-gateway -p 2000:2000 curr_conv

    # Загрузите frontend
    docker load -i frontend.zip

    # Запустите 
    docker run -p 3000:3000 frontend
    # Нажмите на консоль и Enter пару раз, если консоль зависла

    # Затем перейдите на страницу http://127.0.0.1:3000/
    # Таблица может загрузиться не сразу, подождите некоторое время
    # Дальше перейдите по ссылке https://docs.google.com/spreadsheets/d/1wCa9s91PxlkQPDS6pxIsR7-2xB7NMDvvmo1VPhaV0Co/edit?usp=sharing

    # и поменяйте какие нибудь значения в таблице

