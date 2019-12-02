# Generated by Django 2.2.6 on 2019-12-02 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_delete_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(max_length=30)),
                ('restaurant_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('date_written', models.DateTimeField(verbose_name='date written')),
                ('review_text', models.CharField(max_length=250)),
                ('star_rating', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
    ]
