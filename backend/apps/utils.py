import jwt
from rest_framework.views import Request

SECRET_KEY = "114514"
ALGORITHM = ['HS256']
user_id_now = [0]


# 将id转化成长度为8的字符串,用于生成id
def get_new_user_id():
    # 将整数转换为长度为8的字符串，左侧用零填充
    user_id_now[0] = user_id_now[0] + 2
    return '{:08d}'.format(user_id_now[0])


def gen_token(email: str):
    dict = {
        'email': email
    }
    token = jwt.encode(dict, SECRET_KEY, algorithm=ALGORITHM)
    return token


def get_header_token(req: Request):
    if req.headers.get('token'):
        return req.headers['token']


def decode_token(token):
    try:
        dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    except Exception:
        return None
    return dict
