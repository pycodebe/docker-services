# Docker Build with some services working for a Django project
> A set of services used through a Django Framework project

The services integrated in this project:
* Python - Django project
* Nginx as a web server | Reverse Proxy
* ElasticSearch
* Kibana
* APM-Server
* Faktory
* Faktory workers
* Portainer as containers monitoring
* maildev as the SMTP and mail client for development
* Oracle 21c XE for the database 
* Cronicle for the crontab management

## Screenshots
![Screenshot](https://user-images.githubusercontent.com/17100228/167437443-9aba3427-e87f-4e35-857d-db07f1062584.png)


## Modules
* Django==3.2.13
* djangorestframework==3.13.1
* faktory==0.5.1
* python==3.7.13
* django-debug-toolbar==3.2.4
* gunicorn==20.1.0
* whitenoise==5.3.0

## Services:

|Services| Hosts |
|--|--|
| Nginx | http://localhost:80 |
| Faktory | http://localhost:7420
| Kibana | http://localhost:5601
| ElasticSearch | http://localhost:9200
| APM | http://localhost:8200
| Cronicle | http://localhost:3012
| Maildev | http://localhost:1080
| Portainer | http://localhost:9000


## Prerequisite
You need Docker and Docker compose to be installed


## Usage example

```
git clone https://github.com/pycodebe/docker-django-elastic-faktory.git

cd docker-django-elastic-faktory

docker-compose --file docker-compose-dev.yml up --build --remove-orphans -d
```


## Contributing

1. Fork it (<https://github.com/pycodebe/docker-django-elastic-faktory.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request