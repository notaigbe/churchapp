# Generated by Django 5.1 on 2024-09-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_date_homily_entry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='homily',
            name='highlight',
            field=models.CharField(default='Et vero doloremque tempore voluptatem ratione vel aut. Deleniti sunt animi aut. Aut eos aliquam doloribus minus autem quos.', max_length=150),
            preserve_default=False,
        ),
    ]
