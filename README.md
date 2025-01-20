docker-compose up -d --build












Объяснение:

docker-compose.yaml

version: "3.9":

Указывает версию формата docker-compose.yaml.
services::

Определяет сервисы (контейнеры) в вашем приложении.
backend::

build::
context: .: указывает, что Dockerfile находится в текущем каталоге.
dockerfile: Dockerfile: указывает имя вашего Dockerfile.
ports::
"8000:8000": пробрасывает порт 8000 из контейнера на порт 8000 хоста.
networks:
backend-network: Привязывает контейнер к сети backend-network.
nginx::

image: nginx:latest: использует последний образ Nginx из Docker Hub.
ports::
"80:80": пробрасывает порт 80 из контейнера на порт 80 хоста.
volumes::
./nginx.conf:/etc/nginx/conf.d/default.conf: монтирует ваш локальный nginx.conf в контейнер Nginx.
depends_on::
backend: гарантирует, что Nginx запустится после того, как запустится контейнер backend.
networks:
backend-network: Привязывает контейнер к сети backend-network.
networks:

backend-network: Определяет пользовательскую сеть, в которую будут включены оба контейнера.
nginx.conf

server { ... }: Определяет блок конфигурации сервера.
listen 80;: Указывает Nginx слушать на порту 80.
server_name localhost;: Замените localhost на ваше доменное имя или IP-адрес.
location / { ... }: Определяет правила для запросов к корневому пути /.
proxy_pass http://backend:8000;: перенаправляет все запросы на FastAPI приложение, которое работает в контейнере backend на порту 8000.
proxy_set_header ...: настраивает передачу важных заголовков.
Как это работает:

docker-compose up -d --build: запускает сборку и запуск контейнеров.
Docker Compose создает сеть backend-network, к которой подключаются оба контейнера.
Docker Compose собирает образ backend на основе вашего Dockerfile.
Docker Compose запускает контейнер backend с вашим FastAPI приложением.
Docker Compose запускает контейнер nginx и перенаправляет запросы к http://backend:8000.
Когда вы открываете ваш IP-адрес в браузере, Nginx перенаправляет запрос к FastAPI приложению.
Отличия от предыдущего примера:

Базовый образ: Вы используете ubuntu:24.04 как базовый образ для вашего контейнера, а не python:3.9-slim.
Установка Python: Вместо использования готового образа Python, вы сами устанавливаете Python, venv и pip через apt-get внутри контейнера.
CMD: в вашем Dockerfile у вас указан запуск uvicorn с хостом 0.0.0.0 и портом 8000, поэтому мы можем использовать ports в docker-compose.yaml, что бы пробросить порт 8000 из контейнера.
Как использовать:

Сохраните docker-compose.yaml и nginx.conf в одной директории с вашим Dockerfile, requirements.txt и main.py.
Выполните docker-compose up -d --build в терминале в этой директории.
Откройте браузер и перейдите по адресу http://localhost (или http://<ваш_ip_адрес>, если вы запустили на удаленном сервере).
Примечания:

Убедитесь, что ваш файл requirements.txt содержит все зависимости, необходимые для вашего приложения FastAPI.
В nginx.conf замените localhost на ваше доменное имя или IP-адрес при необходимости.
Этот docker-compose.yaml вместе с вашим Dockerfile и nginx.conf должен успешно запустить ваше FastAPI приложение и Nginx. Если что-то пойдет не так, проверьте логи Docker Compose и обратитесь к сообщениям об ошибках.

 
Ask ChatGPT
Не выбран ни один файл


