# Docker Build with some nice services (Workers, DB, SMTP Server, Cron Manager, ...)
> A set of services that can be used in a Python projects for example

The services integrated in this project:
* ElasticSearch
* Kibana
* APM-Server
* Faktory
* Portainer as containers monitoring
* maildev as the SMTP and mail client for development
* Oracle 21c XE for the database 
* Cronicle for the crontab management

## Screenshots
![Screenshot](https://user-images.githubusercontent.com/17100228/170528694-83580adf-6800-4dc1-a50e-a85ee220637d.png)


## Services:

|Services| Hosts |
|--|--|
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
git clone https://github.com/pycodebe/docker-services.git

cd docker-services

docker-compose --file docker-compose-dev.yml up --build --remove-orphans -d
```


## Contributing

1. Fork it (<https://github.com/pycodebe/docker-services.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request