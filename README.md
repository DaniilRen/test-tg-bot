# tg bot on Aiogram

This telegram bot can apply one of few filters to a photo. [User guide](#user-guide)

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

## User guide

1. Use `start/` command to start a dialog
2. Send your photo
3. Choose filter
4. Choose rate
