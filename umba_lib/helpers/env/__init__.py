import environ, os

env = environ.Env()


class Environ:
    @staticmethod
    def read(env_dir):
        if os.path.exists(env_dir):
            env.read_env(env_dir)
