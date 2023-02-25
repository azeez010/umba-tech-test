from flask import Flask
from umba_lib.helpers.env import Environ, env
from pathlib import Path
import os


def create_app(is_test=False):
    flask_app = Flask(__name__)

    Environ.read(os.path.join(Path(__file__).resolve(strict=True).parent.parent, "env", ".env"))

    allowed_application: list = env.list("ALLOWED_APPLICATION", default=("development.DevelopmentConfig",))
    application_config: str = env.str("APPLICATION_CONFIG", "development.DevelopmentConfig")

    if application_config not in allowed_application:
        raise ValueError("%s not in ALLOWED_APPLICATION(%s)" % application_config, allowed_application)

    if is_test:
        flask_app.config.from_object('settings.config.test.TestConfig')
    else:
        flask_app.config.from_object('settings.config.%s' % application_config)

    return flask_app


app = create_app()
