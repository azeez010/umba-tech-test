from settings.config.base import BaseConfig
from umba_lib.helpers.env import env
import os
from pathlib import Path


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = env.str("SQLALCHEMY_DATABASE_URI", "sqlite:///%s" % os.path.join(Path(__file__).resolve(strict=True).parent.parent.parent, "database", "umba.sqlite3"))


