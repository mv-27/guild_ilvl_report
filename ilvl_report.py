import requests
import json
import logging
import argparse
from typing import Dict, Optional

# Configuration
API_KEY = 'your_api_key'
SECRET_KEY = 'your_secret_key'

# Class dictionary for WoW classes
class_dict: Dict[int, str] = {
    1: ':warrior:',
    2: ':paladin:',
    3: ':hunter:',
    4: ':rogue:',
    5: ':priest:',
    6: ':deathknight:',
    7: ':shaman:',
    8: ':mage~1:',
    9: ':warlock:',
    10: ':monk:',
    11: ':druid:'
}

def TauriAPI_Request(url: str, params: Dict[str, str]) -> Dict:
    """Send a POST request to the API and return the JSON response."""
    try:
        payload = {
            'secret': SECRET_KEY,
            'url': url,
            'params': params
        }
        response = requests.post(
            f'https://characters-api.stormforge.gg/v1/?apikey={API_KEY}',
            data=json.dumps(payload)
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return {}

def FindItemLevel(name: str, realm: str) -> Optional[Dict[str, int]]:
    """Find and calculate the average item level of a character."""
    try:
        items = TauriAPI_Request(
            url='character-sheet',
            params={'r': realm, 'n': name}
        ).get('response', {}).get('characterItems', [])

        ilvl_sum = 0
        count = 0

        for item in items:
            if 'ilevel' in item and item['ilevel'] > 100:
                ilvl_sum += item['ilevel']
                count += 1

        if count > 0:
            average_ilvl = round(ilvl_sum / count)
            if average_ilvl > 460:
                return {name: average_ilvl}
    except Exception as e:
        logging.error(f"Error in FindItemLevel: {e}")

    return None

def ListGuildItemLevels(realm: str, guild_name: str):
    """List guild members sorted by item level."""
    try:
        guild_list = TauriAPI_Request(
            url='guild-info',
            params={'r': realm, 'gn': guild_name}
        ).get('response', {}).get('guildList', {})

        raid_list = {}
        for key, member in guild_list.items():
            if member['level'] == 90 and member['rank_name'] != 'unknown':
                raid_player = FindItemLevel(member['name'], realm)
                if raid_player:
                    player_name, item_level = next(iter(raid_player.items()))
                    player_class = class_dict.get(member["class"], 'Unknown')
                    raid_list[f'{player_class} {player_name}'] = item_level

        sorted_raid_list = dict(sorted(raid_list.items(), key=lambda item: item[1], reverse=True))

        for rank, (player, ilvl) in enumerate(sorted_raid_list.items(), start=1):
            print(f'{rank}. {player} - {ilvl} ilvl')

    except Exception as e:
        logging.error(f"Error in ListGuildItemLevels: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch and list guild members sorted by item level.')
    parser.add_argument('--realm', required=True, help='The realm name.')
    parser.add_argument('--guild', required=True, help='The guild name.')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    ListGuildItemLevels(args.realm, args.guild)
