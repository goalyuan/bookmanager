from django.db import models

# Create your models here.
"""
1.定义模型表
2.模型迁移
    2.1 python manage.py makemigrations 生成迁移文件不会生成表
    2.2 python manage.py migrate 迁移成功
3.操作数据表 
"""


class BookInfo(models.Model):
    """
    1.主键当前会自动生成
    2.属性复制
    属性名不要使用python或mysql关键字，不要使用连续下划线__
    属性类型和mysql类型类似
    选项charfield必须设置max_length
    null 是否为空
    unique是否唯一
    default设置默认值
    verbose_name主要是admin后台显示
    """
    # 属性名=属性类型(选项)
    name = models.CharField(max_length=10, unique=True, verbose_name='名字')
    # 发布日期
    pub_date = models.DateField(null=True, verbose_name='发布日期')
    # 阅读量
    readcount = models.IntegerField(default=0)
    # 评论量
    commentcount = models.IntegerField(default=0)
    # 是否逻辑删除
    is_delete = models.BooleanField(default=False)

    class Meta:
        # 改表名
        db_table = 'bookinfo'
        # 修改后台admin的信息信息配置
        verbose_name = 'admin'

    def __str__(self):
        return self.name


"""
insert into bookinfo(name,pub_date,readcount,commentcount,is_delete) values
('射雕英雄传','1980-5-1',12,34,0),
('天龙八部','1986-7-24',36,40,0),
('笑傲江湖','1995-12-24',20,80,0),
('雪山飞狐','1987-11-11',58,24,0);
"""


class PeopleInfo(models.Model):
    # 有序字典
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=10, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    # 外键 on_delete=操作models.CASCADE级联操作
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='')
    description = models.CharField(max_length=200, null=True, verbose_name='描述')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name


"""
insert into peopleinfo(name,gender,book_id,description,is_delete) values
('郭靖',1,1,'降龙十八掌',0),
('黄蓉',0,1,'打狗棍法',0),
('黄药师',1,1,'弹指神功',0),
('欧阳锋',1,1,'哈默功',0),
('梅超风',0,1,'九阴白骨爪',0),
('乔峰',1,2,'降龙十八掌',0),
('段誉',1,2,'弹指神功',0),
('虚竹',1,2,'天山六阳掌',0),
('王语嫣',0,2,'姐姐',0),
('令狐冲',1,3,'独孤九剑',0),
('任盈盈',0,3,'弹指神功',0),
('岳不群',1,3,'弹指神功',0),
('东方不败',0,3,'弹指神功',0),
('胡斐',1,4,'弹指神功',0),
('苗若兰',0,4,'弹指神功',0),
('程灵素',0,4,'弹指神功',0),
('袁紫衣',0,4,'弹指神功',0);
"""
