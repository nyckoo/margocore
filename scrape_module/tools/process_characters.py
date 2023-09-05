from appwrite_instance import AppwriteInstance


class ProcessCharactersDataAppwriteDB:
    user_collection_id = "64b028d330da51888851"
    character_collection_id = "64b028e01471e23a370b"
    character_sets_collection_id = "64f4a59a22af3cbc6629"
    character_items_collection_id = "64f4f9d10d774e627575"

    def __init__(self):
        self.appwrite = AppwriteInstance()

    def extract_and_save_characters_data(self, json_items: dict):
        tpl_collector = []
        for item in json_items:
            if int(item['st']) in range(1, 9):
                tpl_collector.append(str(item['tpl']))
                item_stats = item['stat'].split(";")
                stats_dict = dict(stat.split("=") for stat in item_stats if '=' in stat)

