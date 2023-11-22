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


class Image(models.Model):
    img = models.ImageField(upload_to='images/', default='')

    class Meta:
        db_table = 'tb_images'


# 要有id，但是id不向前端透明
class User(models.Model):
    user_name = models.CharField(max_length=USER_NAME_LENGTH, verbose_name="user_name")
    email = models.CharField(max_length=EMAIL_LENGTH, verbose_name="email")
    password = models.CharField(max_length=PASSWORD_LENGTH, verbose_name="password")
    # open_date = models.DateField(verbose_name="open_date")
    avatar = models.ForeignKey(verbose_name="avatar", to=Image, null=True,
                               on_delete=models.SET_NULL, default=None)

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
    user = models.ForeignKey(verbose_name="user_poster_id", to=User,
                             on_delete=models.CASCADE, default=1)
    image = models.ForeignKey(verbose_name="post_image", to=Image, null=True,
                              on_delete=models.SET_NULL, default=None)

    class Meta:
        db_table = "posts"
        verbose_name = "post"

    def __str__(self):
        return str(self.id) + " " + str(self.title)


class PostLike(models.Model):
    user = models.ForeignKey(verbose_name="user_id", to=User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(verbose_name="post_id", to=Post, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = "like"
        verbose_name = "like"
        unique_together = ("user", "post")


class Collection(models.Model):
    user = models.ForeignKey(verbose_name="user_id", to=User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(verbose_name="post_id", to=Post, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = "collection"
        verbose_name = "collection"
        unique_together = ("user", "post")


class Comment(models.Model):
    user = models.ForeignKey(verbose_name="user_id", to=User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(verbose_name="post_id", to=Post, on_delete=models.CASCADE, default=1)
    content = models.TextField(verbose_name="text")
    res_comment = models.IntegerField(verbose_name="res_to_comment_id", default=-1)
    create_date = models.DateField(verbose_name="create_date")

    # 当然，对一个帖子可以有多个评论
    class Meta:
        db_table = "comment"
        verbose_name = "comment"


class CommentLike(models.Model):
    user = models.ForeignKey(verbose_name="user_id", to=User, on_delete=models.CASCADE, default=1)
    comment = models.ForeignKey(verbose_name="comment_id", to=Comment, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = "likes_comment"
        verbose_name = "like_comment"
        unique_together = ("user", "comment")


class Tag(models.Model):
    name = models.CharField(verbose_name="tag_name", max_length=8)

    class Meta:
        db_table = "tags"
        verbose_name = "tag"


class TagPost(models.Model):
    tag = models.ForeignKey(verbose_name="tag", to=Tag, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(verbose_name="post", to=Post, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = "tags_post"
        verbose_name = "tag_post"


class Board(models.Model):
    name = models.CharField(verbose_name="board_name", max_length=16)

    class Meta:
        db_table = "board"
        verbose_name = "board"


class BoardPost(models.Model):
    board = models.ForeignKey(verbose_name="board", to=Board, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(verbose_name="post", to=Post, on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = "board_post"
        verbose_name = "board_post"


# 公告
class Ann(models.Model):
    create_date = models.DateField(verbose_name="create_date")
    content = models.TextField(verbose_name="content")

    class Meta:
        db_table = "tb_Ann"
        verbose_name = "Ann"


class Notice(models.Model):
    create_date = models.DateField(verbose_name="create_date")
    content = models.TextField(verbose_name="content")
    user = models.ForeignKey(verbose_name="receiver",
                             to=User, on_delete=models.CASCADE)

    class Meta:
        db_table = "tb_Notice"
        verbose_name = "notice"


'''
class Report(models.Model):
    contengt =models.TextField()
    user = models.ForeignKey(verbose_name="reporter",to=User,)
    '''
