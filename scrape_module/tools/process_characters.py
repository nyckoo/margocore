from appwrite_instance import AppwriteInstance


class ProcessCharactersDataAppwriteDB:
    collection_id = "64b028e01471e23a370b"

    def __init__(self):
        self.appwrite = AppwriteInstance()

    def save_characters_eq_data(self, fetched_json: dict):
        item_stats = fetched_json.values()['stat'].split(";")
        stats_dict = dict(stat.split("=") for stat in item_stats if '=' in stat)

