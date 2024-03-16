# tg bot on Aiogram

## Create the project

```bash
mkdir tgbot
cd tgbot
```

## Set your bot token

go to `.env` file and change BOT_TOKEN from '' to your token

## Build and run docker container

Optionally you can change `tgbot` to another name

```bash
docker build -t tgbot .
docker run -ti tgbot
```

## Stop and remove docker container

use `docker ps ` to see container id and then remove it

```
docker rm -f id
```
