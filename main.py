from settings.config import app
from umba_lib.models import ModelUtilities
from app.v1 import api_v1


app.register_blueprint(api_v1)


ModelUtilities.start()

if __name__ == "__main__":
    app.run()
