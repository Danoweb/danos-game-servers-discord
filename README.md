# danos-game-servers-discord
A discord bot for managing game servers (containers, etc) from Discord chat commands

# ENV file

* From a terminal inside this project folder.
* Assure you have a `.env` file, and it has values for these properties:
- `DISCORD_TOKEN=` - The Auth Token for the Bot to use with Discord Services
- `DISCORD_CLIENT_ID=` - The ID of the Discord User/Profile this bot should use
- `DISCORD_GUILD_ID=` - The ID for the Discord community to connect to
- `GUILD_PERMITTED_ROLE=` The name of the user Role on the discord server that can issue commands/actions to the bot

# Ecosystem
This tool is for managing game server deployed on the same host.
- Docker and Docker Compose are required for container/server start/stop management!

- Minecraft
  - Bedrock - A discord container running the bedrock server. update `BEDROCK_SERVER_PATH` in main.py to folder location of container
  - CreateMod - A discord container running the bedrock server. update `CREATEMOD_SERVER_PATH` in main.py to folder location of container

# Installation
- Once configured and the `.env` file is setup (see `.env.example` for example values).  Copy the service file to the folder and enable it.
- Quick example:
  - `cp game-servers.service /etc/systemd/system/game-servers.service`
  - `systemctl start game-servers`
  - `systemctl status game-servers`
  - _You should see a green line in the output that says "active". if not review your configuration!_
  - `systemctl enable game-servers` - (Optional) makes it a service that runs on startup of the Host. 