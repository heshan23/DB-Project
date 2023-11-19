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


class User(models.Model):
    user_id = models.CharField(max_length=ID_LENGTH, verbose_name="user_id", primary_key=True)
    email = models.CharField(max_length=EMAIL_LENGTH, verbose_name="email")
    user_name = models.CharField(max_length=USER_NAME_LENGTH, verbose_name="user_name")
    password = models.CharField(max_length=PASSWORD_LENGTH, verbose_name="password")
    # open_date = models.DateField(verbose_name="open_date")
    avatar = models.IntegerField(max_length=10)

    class Meta:
        db_table = 'db_users'
        verbose_name = 'user'

    def __str__(self):
        return self.user_id + " " + self.user_name


class Post(models.Model):
    post_id = models.CharField(max_length=ID_LENGTH, verbose_name="post_id", primary_key=True)
    title = models.CharField(max_length=TITLE_SIZE, verbose_name="title")
    content = models.TextField(verbose_name="text")
    create_date = models.DateField(verbose_name="created_date")
    user_id = models.ForeignKey(max_length=ID_LENGTH,
                                verbose_name="user_poster_id", to=User, on_delete=models.CASCADE)
