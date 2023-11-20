from django.db import models

# 参数
ID_LENGTH = 8  # CHAR 8
# ------------------------------------------------------
# 用户参数
EMAIL_LENGTH = 127  # VARCHAR 127
USER_NAME_LENGTH = 10  # VARCHAR 10
PASSWORD_LENGTH = 10  # VARCHAR 10
OPEN_DATE = []  # DATE
AVATAR_ID_LENGTH = 10  # INT 10
# -------------------------------------------------------
# 帖子参数
TITLE_SIZE = 32  # VARCHAR 32
CONTENT_TYPE = "TEXT"
CREATE_DATE = "DATE"
# USER_ID ------外键
BOARD_ID_LENGTH = 8  # CHAR 8


# 要有id，但是id不向前端透明
class User(models.Model):
    user_name = models.CharField(max_length=USER_NAME_LENGTH, verbose_name="user_name")
    email = models.CharField(max_length=EMAIL_LENGTH, verbose_name="email")
    password = models.CharField(max_length=PASSWORD_LENGTH, verbose_name="password")
    # open_date = models.DateField(verbose_name="open_date")
    avatar = models.IntegerField()

    class Meta:
        db_table = 'users'
        verbose_name = 'user'

    def __str__(self):
        return str(self.id) + " " + str(self.user_name)


# django 如果在设定的时候就没有设定primary_key,那么会自动生成一个id域,可以用这个确定
# 当然，这个id也不会显示的展示出来
class Post(models.Model):
    title = models.CharField(max_length=TITLE_SIZE, verbose_name="title")
    content = models.TextField(verbose_name="text")
    create_date = models.DateField(verbose_name="created_date")
    user_id = models.ForeignKey(verbose_name="user_poster_id", to=User,
                                on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = "posts"
        verbose_name = "post"

    def __str__(self):
        return str(self.id) + " " + str(self.title)
