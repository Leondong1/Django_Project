from django.db import models

# Create your models here.

# 自定义管理器类
# class BookInfoManager(models.Manager):
#     def all(self):
#         return super(BookInfoManager, self).filter(is_delete = False)


# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    # ImageFiled 字段告诉咱们上传的是文件或者图片
    logo = models.ImageField(upload_to='booktest', verbose_name='图片', null=True)

    # 默认的表名：booktest_bookinfo
    class Meta:
        db_table = 'tb_books'
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称
    # 目的：在咱们的admin站点里面 列表信息添加咱们自己定义的字段
    def pub_date(self):
        # 记住这个方法将咱们的时间转化为字符串的形式
        return self.bpub_date.strftime('%Y年%m月%d日')

    # 相当于给咱们的函数添加一个属性
    pub_date.short_description = '发型日期'
    pub_date.admin_order_field = 'bpub_date'


    def __str__(self):
        return self.btitle
    # 补充自定义的管理器对象，模型类将不会在存在 objects
    # query = BookInfoManager()

#定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    # 咱这里可以使用  related_name='heros'  自定义关联查询的名称
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    # 关联查询里面限制咱们只能通过get得到单一的值
    # 外键实际上在我们的数据库中的存储形式是以 形如：hbook_id 得到
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def read(self):
        return self.hbook.bread

    read.short_description = '图书阅读量'



    def __str__(self):
        return self.hname
