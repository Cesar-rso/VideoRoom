FROM nginx:1.23.0-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /VideoRoom
RUN addgroup -S app && adduser -S app -G app

COPY . .
RUN apk update
RUN apk add python3
RUN apk add py3-pip
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN chmod +x ./startup.sh

# USER app

CMD ["./startup.sh"]