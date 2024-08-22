# Generated by Django 5.0.6 on 2024-05-20 03:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_user_isadmin_user_userrole_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('due_date', models.DateField()),
                ('Borrowing_Status', models.BooleanField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.user')),
            ],
        ),
    ]
