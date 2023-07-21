import scrapy
import requests


class ProfileSpider(scrapy.Spider):
    name = "profile_spider"
    allowed_domains = ["margonem.pl", "mec.garmory-cdn.cloud"]
    request_url = "https://www.margonem.pl/profile/view,"
    garmory_cdn_url = "https://mec.garmory-cdn.cloud/pl/"

    def __init__(self, profile_id='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.profile_id = profile_id.split("=")[-1]

    def start_requests(self):
        yield scrapy.Request(
            url=f"{self.request_url}{self.profile_id}",
            callback=self.parse_characters_stats
        )

    def parse_characters_stats(self, response):
        public_world_characters_info = response.xpath('//div[@class="character-list"]')[0].xpath('.//li')
        for character in public_world_characters_info:
            if int(character.attrib["data-lvl"]) < 25:
                continue
            char_id = character.attrib["data-id"]
            world = character.attrib["data-world"]
            collection_id = int(char_id) % 128
            params_construct = f"{world[1:]}/{collection_id}/{char_id}.json"
            content_json = requests.get(f"{self.garmory_cdn_url}{params_construct}").json()
            self.logger.info(f"url: '{self.garmory_cdn_url}{params_construct}'")
            for item in content_json.values():
                yield {
                    'global_id': item['tpl'],
                    'name': item['name'],
                    'icon_url': item['icon'],
                    'type': item['cl'],
                    'stats': item['stat']
                }
