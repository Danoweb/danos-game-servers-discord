import datetime

# Get Server stats from server/status.json
server_stats = {}

embed = {
        "color": "0x009900",
        "title": 'Server Status',
        #url: 'https://discord.js.org',
        "author": {
            "name": f"{server_status['server_name']}",
            #icon_url: 'https://i.imgur.com/AfFp7pu.png',
            #url: 'https://discord.js.org',
        },
        "description": f"{server_stats['error']}",
        # thumbnail: {
        #     url: 'https://i.imgur.com/AfFp7pu.png',
        # },
        "fields": [
            {
                "name": 'Online Player Count:',
                "value": f"{server_stats['player_count']}",
                "inline": True,
            },
            {
                "name": 'Server Type:',
                "value": f"{server_stats['server_type']}",
                "inline": True,
            },
            {
                "name": '\u200b',
                "value": '\u200b',
                "inline": False,
            },
            {
                "name": 'Players',
                "value": f"{server_stats['players']}",
                "inline": False,
            },
            
        ],
        # image: {
        #     url: 'https://i.imgur.com/AfFp7pu.png',
        # },
        "timestamp": datetime.utc.now(),
        "footer": {
            "text": 'Server Manager - https://www.github.com/danoweb/',
            #icon_url: 'https://i.imgur.com/AfFp7pu.png',
        },
    }