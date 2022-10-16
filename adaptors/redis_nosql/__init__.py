import os
from adaptors.redis_nosql.config import Config

os.environ["REDIS_OM_URL"] = Config().get_db_url()
