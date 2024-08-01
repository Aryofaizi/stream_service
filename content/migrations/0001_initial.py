# Generated by Django 5.0.7 on 2024-08-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('category', models.CharField(choices=[('MOV', 'Movie'), ('TVS', 'TV Show'), ('MIN', 'Mini-Series'), ('ANT', 'Anthology Series'), ('WEB', 'Web Series'), ('DOC', 'Documentary'), ('SPE', 'Special'), ('ANI', 'Animated Film'), ('REA', 'Reality Show'), ('TAL', 'Talk Show'), ('VAR', 'Variety Show')], default='MOV', max_length=3)),
                ('rate', models.IntegerField(choices=[(5, 'EXCELLENT'), (4, 'GOOD'), (3, 'NOT BAD'), (2, 'BAD'), (1, 'VERY BAD')])),
                ('price', models.PositiveIntegerField()),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('genre', models.ManyToManyField(to='content.genre')),
            ],
        ),
    ]
