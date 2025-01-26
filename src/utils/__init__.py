from src.constants import MONGODB_DATABASE_NAME
from src.cloud_io import MongoIO
from src.exception import customexception
import os,sys

def fetch_product_name_from_cloud():
    try:
        mongo = MongoIO()
        collection_names = mongo.mongo_ins.mongo_operation_connect_database.list_collection_names()

        return [collection_names.replace('_',' ')
                for collection_name in collection_names]
    except Exception as e:
        raise customexception(e,sys)
    