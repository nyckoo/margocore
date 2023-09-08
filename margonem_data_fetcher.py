import requests
import re
from appwrite_instance import AppwriteInstance


class ProcessItemsDataAppwriteDB:

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
        ...
