import os
from pathlib import Path

from settings.config.base import BaseConfig


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///%s" % os.path.join(Path(__file__).resolve(strict=True).parent.parent.parent, "database", "umba.sqlite3")