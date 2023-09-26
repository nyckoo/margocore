import os
from appwrite.client import Client
from appwrite.services.databases import Databases


class AppwriteInstance:
    def __init__(self):
        self.client = Client() \
            .set_endpoint(os.environ["HOST"]) \
            .set_project(os.environ["APPWRITE_PROJECT_ID"]) \
            .set_key(os.environ["APPWRITE_API_KEY"])
        self.db = Databases(self.client)
        self.database_id = os.environ["APPWRITE_DB_ID"]
