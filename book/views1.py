from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
from book.models import BookInfo

"""
视图
1.就是python函数
2.函数的第一个参数就是请求,和请求相关的，它是HTTPRequest的实例对象
3.函数必须返回一个响应，响应是HTTPResponse的实力对象或子类实例对象
"""


def index(request):
    name = '菊花'
    # return HttpResponse('index')
    # request,template_name,context=None
    # 参数1 当前的请求
    # 参数2 模板文件
    # 参数3 传递参数
    context = {
        'name': name,
    }
    return render(request, 'index.html', context=context)


# def index(request):
#     # 1.到数据库中查询书籍
#     books = BookInfo.objects.all()
#     # 2.组织数据
#     context = {
#         'name': books,
#     }
#     # 3.传递给模板
#     render(request,)
#     return HttpResponse('index')

####################################新增数据####################################
# python manage.py shell
# 方式1
from book.models import BookInfo

book = BookInfo(name='python', pub_date='2000-01-01')
book.save()
# 方式2
BookInfo.objects.create(name='java', pub_date='2021-5-10')

####################################更新数据####################################
# 方式1
# 1.查询数据
book = BookInfo.objects.get(id=1)
# 2.修改属性
book.readcount = 20
# 3.保存
book.save()
# 方式2
BookInfo.objects.filter(id=1).update(readcount=100, commentcount=100)
#################################### filter \get \exclude ####################################
"""
filter筛选过滤，返回n个结果(n=0/1/n)
get             返回1个结果
exclude排出掉符合条件剩下的结果，相当于not
语法形式
    以filter(字段名_运算符=值)为例
"""
# 查询编号为1的图书
# exact 精确的准确的就是等于
BookInfo.objects.get(id=1)
BookInfo.objects.get(id__exact=1)
BookInfo.objects.filter(id__exact=1)  # 返回的是列表
# 查询书名包含‘湖’的图书
BookInfo.objects.filter(name__contains='湖')
# 查询书名以‘部’结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1, 3, 5])
# 查询编号大于3的图书
# gt 大于
# gte 大于等于
# lt 小于
# lte小于等于
BookInfo.objects.filter(id__gte=3)
# 查询编号不等于3的图书
BookInfo.objects.exclude(id__exact=3)
BookInfo.objects.exclude(id=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year='1980')
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')
#################################### F对象 ####################################
# 两个属性怎么比较
"""
F对象的语法形式
filter(字段名__运算符=F('字段名'))
查询阅读量大于评论量的图书
"""
from django.db.models import F

# 查询阅读量大于评论量的图书
BookInfo.objects.filter(readcount__gt=F('commentcount'))
# 查询阅读量大于评论量2倍的图书
BookInfo.objects.filter(readcount__gt=F('commentcount') * 2)

#################################### Q对象 ####################################
# 查询id大于2且阅读量大于20的图书
# 方式1
# filter().filter()
BookInfo.objects.filter(id__gt=2).filter(readcount__gt=20)
# 方式2
# filter(条件1,条件2)
BookInfo.objects.filter(id__gt=2, readcount__gt=20)

"""
Q对象语法形式
Q(字段名__运算符=值)
或者 Q()|Q()
并且 Q()&Q()
not ~Q()
"""
from django.db.models import Q

# 查询id大于2或者阅读量大于20的图书
BookInfo.objects.filter(Q(id__gt=2) | Q(readcount__gt=20))
# 查询编号部位3的图书
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))
#################################### 聚合函数 ####################################
"""
Sum,Max,Min,Avg,Count
聚合函数需要使用aggregate
语法形式是aggregate(Xxx('字段'))
"""
# 当前数据的阅读总量
from django.db.models import Sum, Avg, Max, Min, Count

BookInfo.objects.aggregate(Sum('readcount'))
#################################### 排序 ####################################
BookInfo.objects.all().order_by('readcount')
BookInfo.objects.all().order_by('-readcount')
#################################### 关联查询 ####################################
"""
语法形式
    通过书籍查询人物信息（已知主表数据，关联查询从表数据）
    主表模型（实例对象）.关联模型类名小写_set.all()
    
    通过人物查询书籍信息（已知从表数据，关联查询主表数据）
    从表模型（实例对象）.外键
"""

# 查询书籍为1的所有人物信息
# 通过书籍查人物
# 1.查询书籍
book = BookInfo.objects.get(id=1)
# 2.根据书籍关联人物信息
book.peopleinfo_set.all()

from book.models import PeopleInfo

# 查询人物为1的书籍信息
# 根据人物查书籍
# 1.查询人物
person = PeopleInfo.objects.get(id=1)
# 2.根据人物关联查询书籍
person.book.name
#################################### 关联查询的筛选 ####################################
"""
书籍和人物的关系是1：n
书籍中没有 任何关于人物的字段（不要考虑隐藏的哪个字段）
人物中有关于书籍的字段book 外键
语法形式
    我们需要的是书籍信息，已知条件是人物信息
    我们需要的是主表数据，已知条件是从表信息
    
    filter(关联模型类名小写__字段__运算符=值)
    
    我们需要的是人物信息，已知条件是书籍信息
    我们需要的是从表信息，已知条件是主表信息
    
    filter(外键__字段__运算符=值)
"""

# 查询图书，要求图书人物为“郭靖”
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
BookInfo.objects.filter(peopleinfo__name='郭靖')
# 查询图书，要求图书人物的描述包含“八”
BookInfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为“天龙八部”的所有人物信息
PeopleInfo.objects.filter(book__name='天龙八部')
PeopleInfo.objects.filter(book__name__exact='天龙八部')
# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=50)

#################################### 分页 ####################################
from django.core.paginator import Paginator

books = BookInfo.objects.all()
# object_list 结果集/列表
# per_page 没页多少条记录
# object_list,per_page
p = Paginator(books, 2)

# 获取第几页数据
p.page(1)
