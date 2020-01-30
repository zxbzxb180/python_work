import tornado.web
from tornado.escape import json_encode
from models.user import UserModel


class UserListHandler(tornado.web.RequestHandler):
    def get(self):
        users = UserModel.get_all()
        self.write(json_encode(users))

    def post(self):
        name = self.get_argument('name')
        age = self.get_argument('age')
        UserModel.create(name, age)
        response = {'status': True, 'msg': 'create success'}
        self.write(json_encode(response))

class UserHandler(tornado.web.RequestHandler):

    def get(self, user_id):
        try:
            user = UserModel.get(int(user_id))
        except KeyError:
            return self.set_status(404)
        self.write(json_encode(user))

    def put(self, user_id):
        age = self.get_argument('age')
        UserModel.update(int(user_id), age)
        response = {'status': True, 'msg': 'update success'}
        self.write(json_encode(response))

    def delete(self, user_id):
        UserModel.delete(int(user_id))
        response = {'status': True, 'msg': 'delete success'}
        self.write(json_encode(response))
