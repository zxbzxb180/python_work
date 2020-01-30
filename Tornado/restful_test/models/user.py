class UserModel():
    users = {
        1: {'name': 'chenxi', 'age': '21'},
        2: {'name': 'liuqi', 'age': '22'},
        3: {'name': 'lifanghui', 'age': '23'},
        4: {'name': 'dengyuhui', 'age': '24'},
    }
    @classmethod
    def get(cls, user_id):
        return cls.users[user_id]

    @classmethod
    def get_all(cls):
        return list(cls.users.values())

    @classmethod
    def create(cls, name, age):
        user_dict = {'name': name, 'age': age}
        id = max(cls.users.keys())+1
        cls.users[id] = user_dict

    @classmethod
    def update(cls, user_id, age):
        cls.users[user_id]['age'] = age

    @classmethod
    def delete(cls, user_id):
        if user_id in cls.users:
            return cls.users.pop(user_id)