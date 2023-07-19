import json
import scrapy


class ProfileSpider(scrapy.Spider):
    name = "profile_spider"
    allowed_domains = ["margonem.pl"]
    request_url = "https://www.margonem.pl/profile/view,"
    profile_id = None

    def start_requests(self):
        response = scrapy.Request(f"{self.request_url}{self.profile_id}")
        public_world_characters_info = response.xpath('//div[@class="character-list"]')[0].xpath('.//li')

        for character in public_world_characters_info:
            char_id = character.attrib["data-id"]
            world = character.attrib["data-world"]
            character_str = f"#char_{char_id},{world[1:]}"
            yield scrapy.Request(f"{self.request_url}{self.profile_id}{character_str}", self.parse)

    def parse(self, response):
        items = response.xpath('//div[@class="eq-background"]')[0].xpath('//div[@class="eq-item"]')
        for item in items:
            try:
                item_stats = item.attrib["tip"]
                json.loads(item_stats)
            except KeyError as e:
                self.logger.info("Item slot is empty.")
