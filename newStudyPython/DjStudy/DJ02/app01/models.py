from django.db import models

# Create your models here.
class userInfo(models.Model):
    id = models.AutoField(primary_key=True)    #创建一个自增的主键字段
    name = models.CharField(null=False,max_length=255)        #创建一个varchar不能为空

    def __str__(self):
        return "<{}------{}>".format(self.id,self.name)

class Persion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,max_length=255)

    def __str__(self):
        return "<{}-----{}>".format(self.id,self.name)

# 自定义 char 类型数据类型
class FixedCharField(models.Field):
    """
    自定义的char类型的字段类
    """
    def __init__(self, max_length, *args, **kwargs):
        super().__init__(max_length=max_length, *args, **kwargs)
        self.length = max_length

    def db_type(self, connection):
        """
        限定生成数据库表的字段类型为char，长度为length指定的值
        """
        return 'char(%s)' % self.length

class newPersion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,max_length=255)
    # 整形
    age = models.IntegerField(default=18)
    # 日期,auto_now_add=True,新建数据的时候自动添加时间
    create_time = models.DateField(auto_now_add=True)
    # auto_now=True每次修改的时候都更新时间
    update_time = models.DateTimeField(auto_now=True)
    chars = FixedCharField(max_length=32,default="chars")
    # 不常用数据类型
    '''
    AutoField(Field)
        - int自增列，必须填入参数 primary_key=True

    BigAutoField(AutoField)
        - bigint自增列，必须填入参数 primary_key=True

        注：当model中如果没有自增列，则自动会创建一个列名为id的列
        from django.db import models

        class UserInfo(models.Model):
            # 自动创建一个列名为id的且为自增的整数列
            username = models.CharField(max_length=32)

        class Group(models.Model):
            # 自定义自增列
            nid = models.AutoField(primary_key=True)
            name = models.CharField(max_length=32)

    SmallIntegerField(IntegerField):
        - 小整数 -32768 ～ 32767

    PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)
        - 正小整数 0 ～ 32767
    IntegerField(Field)
        - 整数列(有符号的) -2147483648 ～ 2147483647

    PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)
        - 正整数 0 ～ 2147483647

    BigIntegerField(IntegerField):
        - 长整型(有符号的) -9223372036854775808 ～ 9223372036854775807

    BooleanField(Field)
        - 布尔值类型

    NullBooleanField(Field):
        - 可以为空的布尔值

    CharField(Field)
        - 字符类型
        - 必须提供max_length参数， max_length表示字符长度

    TextField(Field)
        - 文本类型

    EmailField(CharField)：
        - 字符串类型，Django Admin以及ModelForm中提供验证机制

    IPAddressField(Field)
        - 字符串类型，Django Admin以及ModelForm中提供验证 IPV4 机制

    GenericIPAddressField(Field)
        - 字符串类型，Django Admin以及ModelForm中提供验证 Ipv4和Ipv6
        - 参数：
            protocol，用于指定Ipv4或Ipv6， 'both',"ipv4","ipv6"
            unpack_ipv4， 如果指定为True，则输入::ffff:192.0.2.1时候，可解析为192.0.2.1，开启此功能，需要protocol="both"

    URLField(CharField)
        - 字符串类型，Django Admin以及ModelForm中提供验证 URL

    SlugField(CharField)
        - 字符串类型，Django Admin以及ModelForm中提供验证支持 字母、数字、下划线、连接符（减号）

    CommaSeparatedIntegerField(CharField)
        - 字符串类型，格式必须为逗号分割的数字

    UUIDField(Field)
        - 字符串类型，Django Admin以及ModelForm中提供对UUID格式的验证

    FilePathField(Field)
        - 字符串，Django Admin以及ModelForm中提供读取文件夹下文件的功能
        - 参数：
                path,                      文件夹路径
                match=None,                正则匹配
                recursive=False,           递归下面的文件夹
                allow_files=True,          允许文件
                allow_folders=False,       允许文件夹

    FileField(Field)
        - 字符串，路径保存在数据库，文件上传到指定目录
        - 参数：
            upload_to = ""      上传文件的保存路径
            storage = None      存储组件，默认django.core.files.storage.FileSystemStorage

    ImageField(FileField)
        - 字符串，路径保存在数据库，文件上传到指定目录
        - 参数：
            upload_to = ""      上传文件的保存路径
            storage = None      存储组件，默认django.core.files.storage.FileSystemStorage
            width_field=None,   上传图片的高度保存的数据库字段名（字符串）
            height_field=None   上传图片的宽度保存的数据库字段名（字符串）

    DateTimeField(DateField)
        - 日期+时间格式 YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]

    DateField(DateTimeCheckMixin, Field)
        - 日期格式      YYYY-MM-DD

    TimeField(DateTimeCheckMixin, Field)
        - 时间格式      HH:MM[:ss[.uuuuuu]]

    DurationField(Field)
        - 长整数，时间间隔，数据库中按照bigint存储，ORM中获取的值为datetime.timedelta类型

    FloatField(Field)
        - 浮点型

    DecimalField(Field)
        - 10进制小数
        - 参数：
            max_digits，小数总长度
            decimal_places，小数位长度

    BinaryField(Field)
        - 二进制类型

    字段合集
    '''

    '''
    字段参数
    null
    用于表示某个字段可以为空。
    
    unique
    如果设置为unique=True 则该字段在此表中必须是唯一的 。
    
    db_index
    如果db_index=True 则代表着为此字段设置数据库索引。
    
    default
    为该字段设置默认值。
    
    外键类型在ORM中用来表示外键关联关系，一般把ForeignKey字段设置在 '一对多'中'多'的一方。

    ForeignKey可以和其他表做关联关系同时也可以和自身做关联关系。
    
    字段参数
    to
    设置要关联的表
    
    to_field
    设置要关联的表的字段
    
    related_name
    反向操作时，使用的字段名，用于代替原反向查询时的'表名_set'。
    
    例如：
    
    class Classes(models.Model):
        name = models.CharField(max_length=32)
    
    class Student(models.Model):
        name = models.CharField(max_length=32)
        theclass = models.ForeignKey(to="Classes")
    当我们要查询某个班级关联的所有学生（反向查询）时，我们会这么写：
    
    models.Classes.objects.first().student_set.all()
    当我们在ForeignKey字段中添加了参数 related_name 后，
    
    class Student(models.Model):
        name = models.CharField(max_length=32)
        theclass = models.ForeignKey(to="Classes", related_name="students")
    当我们要查询某个班级关联的所有学生（反向查询）时，我们会这么写：
    
    models.Classes.objects.first().students.all()
    related_query_name
    反向查询操作时，使用的连接前缀，用于替换表名。
    
    on_delete
    当删除关联表中的数据时，当前表与其关联的行的行为。
    
    models.CASCADE
    删除关联数据，与之关联也删除
    
    
    models.DO_NOTHING
    删除关联数据，引发错误IntegrityError
    
    
    models.PROTECT
    删除关联数据，引发错误ProtectedError
    
    
    models.SET_NULL
    删除关联数据，与之关联的值设置为null（前提FK字段需要设置为可空）
    
    
    models.SET_DEFAULT
    删除关联数据，与之关联的值设置为默认值（前提FK字段需要设置默认值）
    
    
    models.SET
    
    删除关联数据，
    a. 与之关联的值设置为指定值，设置：models.SET(值)
    b. 与之关联的值设置为可执行对象的返回值，设置：models.SET(可执行对象)
    
    def func():
        return 10
    
    class MyModel(models.Model):
        user = models.ForeignKey(
            to="User",
            to_field="id"，
            on_delete=models.SET(func)
        )
        
    db_constraint
    是否在数据库中创建外键约束，默认为True。
    
    元信息
    ORM对应的类里面包含另一个Meta类，而Meta类封装了一些数据库的信息。主要字段如下:
    
    db_table
    ORM在数据库中的表名默认是 app_类名，可以通过db_table可以重写表名。
    
    index_together
    联合索引。
    
    unique_together
    联合唯一索引。
    
    ordering
    指定默认按什么字段排序。
    
    只有设置了该属性，我们查询到的结果才可以被reverse()。
    
    '''


    def __str__(self):
        return "<{}-----{}>".format(self.id,self.name)

    class Meta:
        # 自定义表名，跟元信息联合使用
        db_table = "test_newPersion"
