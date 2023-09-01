# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import uuid
from appwrite.client import AppwriteException
from appwrite_instance import AppwriteInstance


class SaveItemsAppwriteDB:
    collection_id = "64baf7919f817203ebb6"

    def __init__(self):
        self.appwrite = None

    def open_spider(self, spider):
        self.appwrite = AppwriteInstance()

    def process_item(self, item, spider):
        try:
            self.appwrite.db.create_document(
                database_id=self.appwrite.database_id,
                collection_id=self.collection_id,
                document_id=uuid.uuid1().hex,
                data=item
            )
        except AppwriteException as e:
            print(f"CODE: {e.code}, {e.message}")
        return item
