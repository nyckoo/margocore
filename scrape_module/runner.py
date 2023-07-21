import logging
import time

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import settings
from scrape_tools.profile_spider import ProfileSpider


logger = logging.getLogger("profile_scraper")
logger.setLevel(logging.DEBUG)

file_logger = logging.FileHandler("scraper.log")
file_logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s', '%Y-%m-%d %H:%M:%S')
logging.Formatter.converter = time.gmtime
file_logger.setFormatter(formatter)

logger.addHandler(file_logger)


if __name__ == "__main__":
    logger.info("start profile_scraper")
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(crawler_settings)

    profile_id = "2309424"
    profile_spider = ProfileSpider
    process.crawl(ProfileSpider, f"-a profile_id={profile_id}")
    process.start()
