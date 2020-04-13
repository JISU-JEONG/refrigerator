# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RecipeBasicInfo(models.Model):
    basic_code = models.IntegerField(primary_key=True)
    basic_name = models.CharField(max_length=2000, blank=True, null=True)
    basic_intro = models.CharField(max_length=5000, blank=True, null=True)
    basic_typecode = models.IntegerField(blank=True, null=True)
    basic_type = models.CharField(max_length=100, blank=True, null=True)
    basic_classcode = models.IntegerField(blank=True, null=True)
    basic_class = models.CharField(max_length=100, blank=True, null=True)
    basic_time = models.CharField(max_length=100, blank=True, null=True)
    basic_kcal = models.CharField(max_length=100, blank=True, null=True)
    basic_volume = models.CharField(max_length=100, blank=True, null=True)
    basic_diff = models.CharField(max_length=100, blank=True, null=True)
    basic_materialclass = models.CharField(max_length=100, blank=True, null=True)
    basic_price = models.CharField(max_length=100, blank=True, null=True)
    basic_imgurl = models.CharField(max_length=2000, blank=True, null=True)
    basic_detailurl = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe_basic_info'


class RecipeMaterialInfo(models.Model):
    recipe_material_id = models.AutoField(primary_key=True)
    material_code = models.ForeignKey(RecipeBasicInfo, models.DO_NOTHING, db_column='material_code')
    material_number = models.IntegerField(blank=True, null=True)
    material_name = models.CharField(max_length=2000, blank=True, null=True)
    material_volume = models.CharField(max_length=2000, blank=True, null=True)
    material_typecode = models.IntegerField(blank=True, null=True)
    material_type = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe_material_info'


class RecipeProcessInfo(models.Model):
    recipe_process_id = models.AutoField(primary_key=True)
    process_code = models.ForeignKey(RecipeBasicInfo, models.DO_NOTHING, db_column='process_code')
    process_order = models.IntegerField(blank=True, null=True)
    process_info = models.CharField(max_length=5000, blank=True, null=True)
    process_imgurl = models.CharField(max_length=2000, blank=True, null=True)
    process_tip = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe_process_info'


class UserInfo(models.Model):
    user_number = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    user_id = models.CharField(max_length=50)
    user_pw = models.CharField(max_length=50)
    user_date = models.DateTimeField()
    user_delete = models.IntegerField()
    user_auth = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_info'
