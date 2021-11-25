# async-pub-sub

## Application start

On a machine with Docker installed, the stack is started through the command:

```
docker-compose up --remove-orphans
```

Then, the web-app is accessible at:
```
http://localhost:5000
```

## Side commands

To run the RabbitMQ image individually:

```
winpty docker run -p 15672:15672 -p 5672:5672 -t -i -v C:\\Users\\Utente\\Documents:/data rabbitmq
```

Note: an application connecting to RabbitMQ from another container, shall use host=host.docker.internal

To generally build and run an image:

```

docker build -t ubuntu .
winpty docker run -t -i -v C:\\Users\\Utente\\Documents:/data ubuntu# async-pub-sub
```
