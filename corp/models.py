from django.db import models

class IndustryCategory(models.Model):
    """
    大分類の業界カテゴリを管理します。
    """
    name = models.CharField(max_length=255, unique=True, verbose_name="大分類名")
    
    def __str__(self):
        return self.name

class Industry(models.Model):
    """
    中分類の業界を管理します。
    """
    name = models.CharField(max_length=255, unique=True, verbose_name="中分類名")
    category = models.ForeignKey(IndustryCategory, on_delete=models.CASCADE, related_name='industries', verbose_name="大分類")
    
    def __str__(self):
        return self.name

class Company(models.Model):
    """
    企業情報を管理します。
    """
    name = models.CharField(max_length=255, verbose_name="企業名")
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='companies', verbose_name="業界")
    description = models.TextField(blank=True, null=True, verbose_name="説明")
    established_date = models.DateField(blank=True, null=True, verbose_name="設立日")
    employees = models.PositiveIntegerField(blank=True, null=True, verbose_name="従業員数")
    revenue = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, verbose_name="収益")
    website = models.URLField(blank=True, null=True, verbose_name="ウェブサイト")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="電話番号")
    email = models.EmailField(blank=True, null=True, verbose_name="メールアドレス")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="住所")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="市区町村")
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name="都道府県")
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="国")
    postal_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="郵便番号")

    def __str__(self):
        return self.name

class Contact(models.Model):
    """
    企業の連絡先情報を管理します。
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contacts', verbose_name="企業")
    first_name = models.CharField(max_length=100, verbose_name="名")
    last_name = models.CharField(max_length=100, verbose_name="姓")
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name="役職")
    email = models.EmailField(blank=True, null=True, verbose_name="メールアドレス")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="電話番号")
    mobile_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="携帯番号")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Note(models.Model):
    """
    企業に関するメモやノートを管理します。
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='notes', verbose_name="企業")
    content = models.TextField(verbose_name="内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    def __str__(self):
        return f"Note for {self.company.name} on {self.created_at}"

class Tag(models.Model):
    """
    企業にタグを付けるためのモデルです。
    """
    name = models.CharField(max_length=50, unique=True, verbose_name="タグ名")
    companies = models.ManyToManyField(Company, related_name='tags', verbose_name="企業")

    def __str__(self):
        return self.name
