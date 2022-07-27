# Generated by Django 4.0.6 on 2022-07-27 04:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(help_text='Phone number must be entered in the format: 000-000-0000.', max_length=17, null=True, validators=[django.core.validators.RegexValidator(regex='^([0-9]{3}[\\-]{1}[0-9]{3}[\\-]{1}[0-9]{4})$')])),
                ('email', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, help_text='Phone number must be entered in the format: 000-000-0000.', max_length=17, validators=[django.core.validators.RegexValidator(regex='^([0-9]{3}[\\-]{1}[0-9]{3}[\\-]{1}[0-9]{4})$')])),
                ('type', models.CharField(choices=[('DOG', 'Dog'), ('CAT', 'Cat'), ('PET', 'Other')], default='DOG', max_length=3)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('comments', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('LOST', 'Lost'), ('FOUND', 'Found')], default='LOST', max_length=5)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.member')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='https://lostandhound.s3.us-west-2.amazonaws.com/noPhoto.png/', max_length=200)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pet')),
            ],
        ),
    ]
