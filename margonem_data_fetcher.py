import json
import uuid

import requests
import re
from datetime import datetime
from appwrite.client import AppwriteException

from appwrite_instance import AppwriteInstance


class ProcessItemsDataAppwriteDB:
    items_collection_id = "64baf7919f817203ebb6"
    rarity_to_lvl = {'unique': 2, 'heroic': 1}

    def __init__(self):
        self.appwrite = AppwriteInstance()

    @staticmethod
    def request_items_stats_by_preview(profile_id: str, chash: str, body: str) -> list[str]:
        url = "https://www.margonem.pl/ajax/previewProfile"
        headers = {
            "Cookie": f"chash={chash}; user_id={profile_id}; hs3={chash[0:3]};",
            "Origin": "https://www.margonem.pl",
            "Referer": "https://www.margonem.pl",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        full_body = f"profile={body}&h2={chash[0:3]}&security=true"
        response = requests.post(
            url=url,
            headers=headers,
            data=full_body
        )
        regex_pattern = '{\"hid\".*}'
        return re.findall(regex_pattern, response.json()['profile'])

    def extract_and_parse_items_data(self, items_list: list[str]):
        for item_str in items_list:
            item_data = json.loads(item_str)
            item_stats = item_data['stat'].split(";")
            stats_dict = dict(stat.split("=") for stat in item_stats if '=' in stat)

            item_lvl = stats_dict['lvl']
            rarity = stats_dict['rarity']
            if stats_dict.get('enhancement_upgrade_lvl', None):
                continue
            if stats_dict.get('low_req', None):
                item_lvl = int(stats_dict['lvl']) + self.rarity_to_lvl[rarity]
            record = {
                'tpl_id': None,
                'name': item_data['name'],
                'lvl': item_lvl,
                'sort': rarity,
                'profession': stats_dict.get('reqp', 'mptwbh'),
                'accessory_id': item_data['cl'],
                'stats': json.dumps(obj=stats_dict, ensure_ascii=False),
                'img_source': item_data['icon'],
                'in_game_source': [],
                'updated': str(datetime.utcnow())
            }
            try:
                self.appwrite.db.create_document(
                    database_id=self.appwrite.database_id,
                    collection_id=self.items_collection_id,
                    document_id=uuid.uuid1().hex,
                    data=record
                )
            except AppwriteException as e:
                print(f"CODE: {e.code}, {e.message}")
