# tg bot on Aiogram

## Setting environment variables
go to .env file and set your bot token : BOT_TOKEN=<your_token>

## Building docker container
```
docker build -t tgbot .
```

## Running docker container
```
docker run -ti tgbot
```

## Exiting docker container
```
docker ps // to see container id
docker rm -f id
```

## P.S: optionally you can change "tgbot" to another name
