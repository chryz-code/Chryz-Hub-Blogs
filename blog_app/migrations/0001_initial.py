# Generated by Django 3.2.4 on 2022-09-26 13:25

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=160)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profile_pics')),
                ('website_url', models.CharField(blank=True, max_length=250, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=250, null=True)),
                ('github_url', models.CharField(blank=True, max_length=250, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=250, null=True)),
                ('dribble_url', models.CharField(blank=True, max_length=250, null=True)),
                ('figma_url', models.CharField(blank=True, max_length=250, null=True)),
                ('codepen_url', models.CharField(blank=True, max_length=250, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=250, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='images/header_image')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('snippet', models.CharField(max_length=70)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.category')),
                ('likes', models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog_app.post')),
            ],
        ),
    ]
