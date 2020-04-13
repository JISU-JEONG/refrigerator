# Generated by Django 3.0.5 on 2020-04-09 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeBasicInfo',
            fields=[
                ('basic_code', models.IntegerField(primary_key=True, serialize=False)),
                ('basic_name', models.CharField(blank=True, max_length=2000, null=True)),
                ('basic_intro', models.CharField(blank=True, max_length=5000, null=True)),
                ('basic_typecode', models.IntegerField(blank=True, null=True)),
                ('basic_type', models.CharField(blank=True, max_length=100, null=True)),
                ('basic_classcode', models.IntegerField(blank=True, null=True)),
                ('basic_class', models.CharField(blank=True, max_length=100, null=True)),
                ('basic_time', models.CharField(blank=True, max_length=100, null=True)),
                ('basic_kcal', models.CharField(blank=True, max_length=100, null=True)),
                ('basic_volume', models.CharField(blank=True, max_length=100, null=True)),
                ('basic_diff', models.CharField(blank=True, max_length=100, null=True)),
                ('basic_materialclass', models.CharField(blank=True, max_length=100, null=True)),
                ('basic_price', models.CharField(blank=True, max_length=100, null=True)),
                ('basic_imgurl', models.CharField(blank=True, max_length=2000, null=True)),
                ('basic_detailurl', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'recipe_basic_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecipeMaterialInfo',
            fields=[
                ('recipe_material_id', models.AutoField(primary_key=True, serialize=False)),
                ('material_number', models.IntegerField(blank=True, null=True)),
                ('material_name', models.CharField(blank=True, max_length=2000, null=True)),
                ('material_volume', models.CharField(blank=True, max_length=2000, null=True)),
                ('material_typecode', models.IntegerField(blank=True, null=True)),
                ('material_type', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'recipe_material_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecipeProcessInfo',
            fields=[
                ('recipe_process_id', models.AutoField(primary_key=True, serialize=False)),
                ('process_order', models.IntegerField(blank=True, null=True)),
                ('process_info', models.CharField(blank=True, max_length=5000, null=True)),
                ('process_imgurl', models.CharField(blank=True, max_length=2000, null=True)),
                ('process_tip', models.CharField(blank=True, max_length=5000, null=True)),
            ],
            options={
                'db_table': 'recipe_process_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_number', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=30)),
                ('user_id', models.CharField(max_length=50)),
                ('user_pw', models.CharField(max_length=50)),
                ('user_date', models.DateTimeField()),
                ('user_delete', models.IntegerField()),
                ('user_auth', models.IntegerField()),
            ],
            options={
                'db_table': 'user_info',
                'managed': False,
            },
        ),
    ]
