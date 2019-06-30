from pickle import dumps, loads
from .WeixinRequest import WeixinRequest
from redis import StrictRedis
from .setting import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY

class RedisQuere():
    def __init__(self):
        """
        初始化Redis
        """
        self.db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

    def add(self,request):
        """
        向队列添加序列化后的Request
        :param request: 请求对象
        :param fail_time: 失败对象
        :return: 添加结果
        """
        if isinstance(request, WeixinRequest):
            return loads(self.db.lpop(REDIS_KEY))
        else:
            return False

    def empty(self):
        return self.db.llen(REDIS_KEY) == 0


