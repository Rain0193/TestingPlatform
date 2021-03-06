from django.db import models
from datetime import datetime


# Create your models here.
class TestDataConfig(models.Model):
    """
    环境数据配置
    """
    TYPE = (
        ("test", "测试环境"),
        ("gld", "灰度环境"),
        ("pro", "生产环境")
    )
    name = models.CharField(max_length=30, verbose_name="名称")
    type = models.CharField(max_length=30, choices=TYPE, verbose_name="类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    class Meta:
        verbose_name = "环境配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UrlDataConfig(models.Model):
    """
    url数据配置
    """
    test_data_config = models.ForeignKey(TestDataConfig, related_name="urls", verbose_name="环境数据配置")
    name = models.CharField(max_length=30, verbose_name="名称")
    keyword = models.CharField(max_length=30, verbose_name="关键字")
    url = models.CharField(max_length=300, verbose_name="域名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    class Meta:
        verbose_name = "url数据配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class DataBaseConfig(models.Model):
    """
    数据库
    """
    test_data_config = models.ForeignKey(TestDataConfig, related_name="data_bases", verbose_name="环境数据配置")
    name = models.CharField(max_length=30, verbose_name="名称")
    keyword = models.CharField(max_length=30, verbose_name="关键字")
    database_host = models.CharField(max_length=100, verbose_name="数据库链接")
    database_port = models.CharField(max_length=10, verbose_name="数据库端口")
    database_user = models.CharField(max_length=100, verbose_name="数据库用户名")
    database_password = models.CharField(max_length=100, verbose_name="数据库密码")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    class Meta:
        verbose_name = "数据库配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
