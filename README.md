# Student's marks telegram bot
### [Link](https://t.me/my_temperaturebot) to the bot

## Deployment
The project is aimed to be deployed on Heroku.
So you need to configure data in initial_data directory.

Insert your chat id in [admins.json](./initial_data/admins.json) file.
You can also configure students in [students.json](./initial_data/students.json) file.

After that, setup following environment variables:
- TELEGRAM_BOT_TOKEN
- DATABASE_URL

About [technical requirements](./docs/technical_requirements.md).
