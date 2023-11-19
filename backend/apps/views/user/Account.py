import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import *
from apps.utils import *


def check_email_exist(email):
    try:
        User.objects.get(email=email)
        return True
    except User.DoesNotExist:
        return False
    # 未注册返回0,注册返回1


class Login(APIView):
    def post(self, request):
        value, reason = 200, ""
        user = None
        try:
            user_id = str(request.data["user_id"])
            password = str(request.data["password"])
        except KeyError:
            value, reason = 400, "keyError,请检查发送的信息是否有user_id,password"
            return Response({"value": value, "reason": reason})
        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            value, reason = 404, "无该用户信息"
        if password != user.password:
            value, reason = 114, "密码错误"
        return Response({"value": value, "reason": reason})


class UserSignUp(APIView):
    def post(self, request):
        value, reason = 200, ""
        ret_data = []
        try:
            email = request.data["email"]
            user_name = request.data["user_name"]
            password = request.data["password"]
        except KeyError:
            print(request.data)
            value, reason = 400, "keyError,请检查发送的信息是否有email,user_name,password"
            return Response({"value": value, "reason": reason})
        if check_email_exist(email):
            value, reason = 114, "该email已经注册过账户"
            return Response({"value": value, "reason": reason, "data": []})
        try:
            user = User.objects.create(
                user_id="00000007",
                user_name=user_name,
                password=password,
                avatar=114,
            )
            user.save()
            # 返回注册的id
            ret_data = user.user_id
        except Exception as e:
            print(e)
        return Response({"value": value, "reason": reason, "data": ret_data})


# 展示账户界面的基本信息
class YourAccountMessage(APIView):
    def get(self, request):
        value, reason = 200, ""
        ret_data = []
        try:
            print(request.GET)
            user_id = request.GET["user_id"]
        except KeyError:
            value, reason = 1, "keyError,请检查发送的信息是否有user_id"
            return Response({"value": value, "reason": reason})
        try:
            user = User.objects.get(user_id=user_id)
            ret_data = {
                "user_name": user.user_name,
                "user_email": user.email,
                #'open_date': user.open_date.strftime('%Y-%m-%d %H:%I:%S'),
                "avatar": user.avatar,
            }
        except User.DoesNotExist:
            value, reason = 404, "不存在该账户"
        return Response({"value": value, "reason": reason, "data": ret_data})


class TryAutoReg(APIView):
    def get(self, request):
        try:
            user = User.objects.create(
                user_id=get_new_user_id(),
                user_name="hlq",
                password="114151",
                # open_date=datetime.datetime,
                avatar=1,
            )
            user.save()
        except Exception as e:
            print(e)
            return Response({"value": 114, "reason": "创建"})
        return Response({"value": 200, "reason": "成功创建"})
