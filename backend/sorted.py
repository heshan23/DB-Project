# 假设帖子数据存储在一个字典中，键为帖子ID，值为标签列表和点赞量
posts = {
    1: {'tags': ['python', 'data-science'], 'likes': 10},
    2: {'tags': ['machine-learning', 'python'], 'likes': 15},
    4: {'tags': ['machine-learning', 'python'], 'likes': 15},
    5: {'tags': ['machine-learning', 'python'], 'likes': 15},
    6: {'tags': ['machine-learning', 'python'], 'likes': 15},
    7: {'tags': ['machine-learning', 'python'], 'likes': 15},
    8: {'tags': ['machine-learning', 'python'], 'likes': 15},
    9: {'tags': ['machine-learning', 'python'], 'likes': 15},
    10: {'tags': ['machine-learning', 'python'], 'likes': 15},
    11: {'tags': ['machine-learning', 'python'], 'likes': 15},
    12: {'tags': ['machine-learning', 'python'], 'likes': 15},
    13: {'tags': ['machine-learning', 'python'], 'likes': 15},
    14: {'tags': ['machine-learning', 'python'], 'likes': 15},
    15: {'tags': ['machine-learning', 'python'], 'likes': 15},
    16: {'tags': ['machine-learning', 'python'], 'likes': 15},
    17: {'tags': ['machine-learning', 'python'], 'likes': 15},
    18: {'tags': ['machine-learning', 'python'], 'likes': 15},

    # 其他帖子...
}

# 用户的收藏数据，假设存储在一个字典中，键为标签，值为数量
user_favorites = {'python': 2, 'data-science': 1}

# 计算用户对每个标签的兴趣权重
user_interests = {}
for post_id, post_data in posts.items():
    for tag in post_data['tags']:
        if tag in user_favorites:
            user_interests[tag] = user_interests.get(tag, 0) + user_favorites[tag]

# 对帖子按照用户兴趣权重和点赞量进行排序
recommended_posts = sorted(posts.items(),
                           key=lambda x: (sum(user_interests.get(tag, 0) for tag in x[1]['tags']), x[1]['likes']),
                           reverse=True)

# 获取前5个推荐帖子
top5_recommendations = recommended_posts[:5]

# 输出推荐帖子
for post_id, post_data in top5_recommendations:
    print(f"Post ID: {post_id}, Tags: {post_data['tags']}, Likes: {post_data['likes']}")
