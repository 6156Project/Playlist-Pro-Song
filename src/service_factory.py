import os
from resources.rds_data_service import RDSDataService
from resources.songs_resource import SongsResource
from api.musixmatch import Musixmatch

# DATABASE CONFIGS
class RDSDataServiceConfig:
    def __init__(self, db_user, db_pw, db_host, db_port):
        self.db_user = db_user
        self.db_pw = db_pw
        self.db_host = db_host
        self.db_port = db_port


# RESOURCES CONFIGS
class SongsResourceConfig:
    def __init__(self, data_service, collection_name):
        self.data_service = data_service
        self.collection_name = collection_name

# API CONFIGS
class MusixmatchApiConfig:
    def __init__(self, key):
        self.key = key 

class ServiceFactory:
    def __init__(self):
        self.rds_svc_config = RDSDataServiceConfig(
            os.environ.get("RDS_USERNAME"),
            os.environ.get("RDS_PASSWORD"),
            os.environ.get("RDS_HOSTNAME"),
            os.environ.get("RDS_PORT")
        )
        self.rds_service = RDSDataService(self.rds_svc_config)
        # connect songs resource to rds
        self.songs_service_config = SongsResourceConfig(self.rds_service, "PlaylistPro.Song")
        self.songs_resource = SongsResource(self.songs_service_config)

        self.musixmatch_config = MusixmatchApiConfig(
            os.environ.get("MUSIXMATCH")
        )
        self.musixmatch_service = Musixmatch(self.musixmatch_config)

    def get(self, resource_name, default):
        if resource_name == "songs":
            result = self.songs_resource
        elif resource_name == "search":
            result = self.musixmatch_service
        else:
            result = default
        return result
