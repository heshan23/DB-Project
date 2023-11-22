from rest_framework.response import Response
from rest_framework.views import APIView

from apps.views.user.Images import image_url
from apps.models import *


# Response默认第一个参数是data

default_avatar_url = image_url + "media/images/oo.jpg"


def check_user_name_exist(username):
    try:
        User.objects.get(user_name=username)
        return True
    except User.DoesNotExist:
        return False
    # 未注册返回0,注册返回1


class UserSignIn(APIView):
    def post(self, request):
        try:
            user_name = str(request.data["user_name"])
            password = str(request.data["password"])
        except KeyError:
            return Response(
                {"reason": "keyError,请检查发送的信息是否有user_name,password"}, status=422
            )
        try:
            user = User.objects.get(user_name=user_name)
        except User.DoesNotExist:
            return Response({"reason": "该用户名未被注册"}, status=404)
        if password != user.password:
            return Response({"reason": "密码错误"}, status=400)
        if user.avatar is None:
            avatar = default_avatar_url
        else:
            avatar = user.avatar.img.url
        ret = {"user_name": user.user_name, "avatar": avatar, "email": user.email}
        return Response({"reason": "登录成功", "user": ret}, status=200)


class UserSignUp(APIView):
    def post(self, request):
        try:
            email = request.data["email"]
            user_name = request.data["user_name"]
            password = request.data["password"]
        except KeyError:
            return Response(
                {"reason": "keyError,请检查发送的信息是否有email,user_name,password"}, status=422
            )
        if check_user_name_exist(user_name):
            return Response({"reason": "该用户名已经被注册"}, status=400)
        try:
            user = User.objects.create(
                user_name=user_name,
                password=password,
                email=email,
            )
            user.save()
            # 返回注册的用户名
        except Exception as e:
            print(e)
        return Response({"reason": "创建成功"}, status=200)


# 编辑个人信息,一般是password和username和avatar
class EditProfile(APIView):
    def post(self, request):
        try:
            before_name = request.data["before_name"]
            new_name = request.data["new_name"]
            new_password = request.data["new_password"]
        except KeyError:
            return Response({"reason": "keyError,请检查发送的信息"}, status=422)
        if check_user_name_exist(new_name):
            return Response({"reason": "该新用户名已被注册"}, status=400)
        try:
            user = User.objects.get(user_name=before_name)
            user.user_name = new_name
            user.password = new_password
            user.save()
        except Exception as e:
            print(e)
            return Response({"reason": str(e)}, status=500)
        return Response({"reason": "修改成功"}, status=200)


# 展示账户界面的基本信息
class YourAccountMessage(APIView):
    def get(self, request):
        try:
            print(request.GET)
            user_name = request.GET["user_name"]
        except KeyError:
            return Response({"reason": "keyError,请检查发送的信息是否有user_id"}, status=422)
        try:
            user = User.objects.get(user_name=user_name)
            if user.avatar is None:
                avatar = default_avatar_url
            else:
                avatar = user.avatar.img.url
            ret_data = {
                "user_name": user.user_name,
                "user_email": user.email,
                "avatar": avatar,
            }
        except User.DoesNotExist:
            return Response({"reason": "不存在该账户"}, status=404)
        return Response({"reason": "", "data": ret_data}, status=200)
