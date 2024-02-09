users = [
    {"username": "callmecposu", "password": "qwerty123"},
    {"username": "vlad_guzli", "password": "zalchik"}
]

def argument_wrapper(username, password):
    def authorization_decorator(func):
        def wrapper(*args, **kwargs):
            if (users.count({"username": username, "password": password}) > 0):
                result  = func(*args, **kwargs)
                return result
            else:
                raise Exception('Unauthorized Access')
        return wrapper
    return authorization_decorator

def doSmth():
    print('You have done something!')

unAuthorised_doSmth = argument_wrapper('1', '2')(doSmth)
authorised_doSmth = argument_wrapper('callmecposu', 'qwerty123')(doSmth)
try:
    unAuthorised_doSmth()
except Exception as e:
    print(e)
authorised_doSmth()