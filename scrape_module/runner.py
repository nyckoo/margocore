import os
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

import scrape_module.settings as settings
from tools.profile_spider import ProfileSpider


if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(crawler_settings)

    chash = os.environ["CHASH"]
    profile_id = "2309424"
    process.crawl(ProfileSpider, f"-a profile_id={profile_id}")
    process.start()
