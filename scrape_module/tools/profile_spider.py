import json
import scrapy
import requests

from scrape_module.tools.spider_logger_conf import apply_file_logger


class ProfileSpider(scrapy.Spider):
    """
        Scrape profile info when new user registers.
        Insert/update new items and player characters' eqs.
    """
    name = "profile_spider"
    logger = apply_file_logger("profile_spider.log")
    allowed_domains = ["margonem.pl", "mec.garmory-cdn.cloud", "margoworld.pl"]
    profile_url = "https://www.margonem.pl/profile/view,"
    garmory_cdn_url = "https://mec.garmory-cdn.cloud/pl/"
    margoworld_url = "https://margoworld.pl/"

    def __init__(self, profile_id='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.profile_id = profile_id.split("=")[-1]

    def start_requests(self):
        yield scrapy.Request(
            url=f"{self.profile_url}{self.profile_id}",
            callback=self.parse
        )

    def parse(self, response, **kwargs):
        public_world_characters_info = response.xpath('//div[@class="character-list"]')[0].xpath('.//li')
        for character in public_world_characters_info:
            if int(character.attrib["data-lvl"]) < 25:
                continue
            char_id = character.attrib["data-id"]
            world = character.attrib["data-world"]
            collection_id = int(char_id) % 128
            query_params = f"{world[1:]}/{collection_id}/{char_id}.json"
            url_parametrized = f"{self.garmory_cdn_url}{query_params}"
            self.logger.info(f"URL: '{url_parametrized}'")
            content_json = requests.get(url_parametrized).json().values()
            tpl_collector = []
            for item in content_json:
                if int(item['st']) in range(1, 9):
                    tpl_collector.append(str(item['tpl']))
                    # compose eq with items grabbed from cdn
                    # save it to characters' db collection

            tpl_params = ','.join(tpl_collector)
            url_construct = f"{self.margoworld_url}item/set/{tpl_params}"
            self.logger.info(f"URL: '{url_construct}'")
            yield scrapy.Request(
                url=url_construct,
                callback=self.parse_base_items
            )

    def parse_base_items(self, response):
        for nr in range(1, 9):
            item_info = response.xpath(f'//span[@class="itemborder item-slot-{nr}"]//img')
            item_data = json.loads(item_info.attrib['tip'])
            item_data.pop('version', 'version not found')
            item_data.pop('tags', 'tags  not found')
            item_data.pop('extendedID', 'extendedID not found')
            in_game_source = item_data.pop('loot', [])
            item_stats = item_data['stat'].split(";")
            stats_dict = dict(stat.split("=") for stat in item_stats if '=' in stat)
            item_lvl = stats_dict.pop('lvl')
            item_sort = stats_dict.pop('rarity')
            item_profession = stats_dict.pop('reqp', 'mptwbh')
            stats_dict.pop('created', 'created not found')
            stats_dict.pop('tags', 'tags not found')

            yield {
                'tpl_id': item_data['id'],
                'name': item_data['name'],
                'lvl': item_lvl,
                'sort': item_sort,
                'profession': item_profession,
                'accessory_id': item_data['cl'],
                'stats': json.dumps(obj=stats_dict, ensure_ascii=False),
                'img_source': item_data['icon'],
                'in_game_source': in_game_source
            }
