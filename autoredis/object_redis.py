import redis
import pickle


class ObjectRedis(redis.Redis):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_obj(self, key: str, obj):
        return self.set(key, pickle.dumps(obj))

    def get_obj(self, key: str):
        obj = self.get(key)
        try:
            return pickle.loads(obj)
        except:
            return obj
