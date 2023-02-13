import redis
import pickle
import docker
import os
import uuid
import time
from autoredis.object_redis import ObjectRedis


class AutoRedis(ObjectRedis):
    def __init__(self, pwd = None, *args, **kwargs):
        self.client = docker.from_env()
        if pwd is None:
            pwd = os.path.dirname(__file__)
        psw = uuid.uuid4().hex
        kwargs["password"] = psw
        self.container_name = "redis"
        self.clear()
        self.redis_container = self.client.containers.run(
            image="redis:7.0",
            name=self.container_name,
            volumes=[f"{pwd}/redis.conf:/etc/redis/redis.conf:ro",
                     f"{pwd}/redis_data:/data"],
            command=f"redis-server /etc/redis/redis.conf --requirepass {psw}",
            ports={"6379/tcp": 6379},
            remove=True,
            detach=True,
            privileged=False
        )
        time.sleep(1)
        super().__init__(*args, **kwargs)

    def clear(self):
        try:
            running_container = self.client.containers.get(self.container_name)
            running_container.stop()
            try:
                running_container.remove()
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

    def __enter__(self):
        return super().__enter__()

    def __exit__(self, type, value, traceback):
        self.redis_container.stop()
        return super().__exit__(type, value, traceback)

    def __del__(self) -> None:
        return super().__del__()
