# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import uuid
from appwrite.client import Client
from appwrite.services.databases import Databases


class SaveProfileInfoToAppwriteDB:
    db_id = "64b01ce78dac14ef765b"
    collection_id = "64baf7919f817203ebb6"

    def open_spider(self, spider):
        self.client = Client()\
            .set_endpoint(os.environ["HOST"])\
            .set_project(os.environ["APPWRITE_PROJECT_ID"])\
            .set_key(os.environ["APPWRITE_API_KEY"])
        self.db = Databases(self.client)

    def process_item(self, item, spider):
        self.db.create_document(
            database_id=self.db_id,
            collection_id=self.collection_id,
            document_id=uuid.uuid1().hex,
            data=item
        )
        return item
