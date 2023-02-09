# danos-game-servers-discord
A discord bot for managing game servers (containers, etc) from Discord chat commands

# ENV file

* From a terminal inside this project folder.
* Assure you have a `.env` file, and it has values for these properties:
- `DISCORD_TOKEN=` - The Auth Token for the Bot to use with Discord Services
- `DISCORD_CLIENT_ID=` - The ID of the Discord User/Profile this bot should use
- `DISCORD_GUILD_ID=` - The ID for the Discord community to connect to
- `GUILD_PERMITTED_ROLE=` The name of the user Role on the discord server that can issue commands/actions to the bot