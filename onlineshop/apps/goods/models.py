from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField  # 支持python3的富文本框
# Create your models here.
class GoodsCategory(models.Model):
    """
    商品类别
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目")
    )
    name = models.CharField(max_length=30, default="", verbose_name="类别名", help_text="类别名")
    code = models.CharField(max_length=30, default="", verbose_name="类别code",help_text="类别code")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True,
                                        verbose_name="父类目级", related_name="sub_cat")  # 建立目录树，一个表包含多个类别
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = verbose_name_plural = "商品类别"

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    品牌名
    """
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
    desc = models.TextField(default="", max_length=200, verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brand/images/")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory, null=True, blank=True, verbose_name="商品类目")
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    name = models.CharField(max_length=300, verbose_name="商品名")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    shop_price = models.FloatField(default=0, verbose_name="本店价格")
    goods_brief = models.CharField(max_length=500, verbose_name="商品简短描述")
    goods_desc = UEditorField(verbose_name="内容", imagePath="goods/images/", width=1000, height=500,
                              filePath="goods/files/", default="")
    ship_free = models.BooleanField(default=False, verbose_name="是否承担运费")
    goods_front_image = models.ImageField(upload_to="", null=True, blank=True)
    goods_front_image_url = models.CharField(max_length=300, default="", verbose_name="封面图链接")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = verbose_name_plural = "商品轮"

    def __str__(self):
        return self.name



class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods)
    image = models.ImageField(upload_to="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = verbose_name_plural = "商品轮播图"

    def __str__(self):
        return self.goods.name