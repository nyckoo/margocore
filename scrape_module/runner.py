import settings
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from tools.profile_spider import ProfileSpider


if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(crawler_settings)

    profile_id = "2309424"
    process.crawl(ProfileSpider, f"-a profile_id={profile_id}")
    process.start()
