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
docker run -p 15672:15672 -p 5672:5672 -t -i -v $(pwd):/data rabbitmq:3-management-alpine
```

To build and run the consumer image individually, cd into the consumer folder:

```
docker build -t async-pub-sub_consumer .
docker run -t -i -v $(pwd):/data async-pub-sub_consumer:latest
```

To build and run the producer image individually, cd into the producer folder:

```
docker build -t async-pub-sub_producer .
docker run -p 5100:5100 -t -i -v $(pwd):/data async-pub-sub_producer:latest
```

Note: an application connecting to RabbitMQ from another container, shall use host=host.docker.internal
