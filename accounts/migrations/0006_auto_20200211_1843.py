# Generated by Django 3.0.1 on 2020-02-11 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200210_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='expected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans1', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='testcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_input', models.CharField(max_length=100)),
                ('expected_output', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.expected')),
            ],
        ),
    ]
