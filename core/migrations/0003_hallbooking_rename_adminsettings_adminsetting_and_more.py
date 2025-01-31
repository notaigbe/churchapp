# Generated by Django 5.1 on 2024-09-20 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_weddingbookings_weddingbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='HallBooking',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('book_date', models.CharField(db_column='Book_Date', max_length=25)),
                ('book_time', models.CharField(blank=True, db_column='Book_Time', max_length=10, null=True)),
                ('hall', models.CharField(db_column='Hall', max_length=25)),
                ('customer_name', models.CharField(max_length=50)),
                ('amount_paid', models.DecimalField(db_column='Amount_Paid', decimal_places=5, max_digits=10)),
                ('balance', models.DecimalField(db_column='Balance', decimal_places=5, max_digits=10)),
                ('phone', models.CharField(db_column='Phone', max_length=11)),
                ('discount', models.IntegerField(db_column='Discount')),
                ('actual_book_date', models.DateTimeField(db_column='Actual_Book_Date')),
            ],
            options={
                'db_table': 'hall_booking',
            },
        ),
        migrations.RenameModel(
            old_name='AdminSettings',
            new_name='AdminSetting',
        ),
        migrations.RenameModel(
            old_name='ChurchGroups',
            new_name='ChurchGroup',
        ),
        migrations.RenameModel(
            old_name='ChurchGroupDetails',
            new_name='ChurchGroupDetail',
        ),
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
        migrations.RenameModel(
            old_name='Parishioners',
            new_name='Parishioner',
        ),
        migrations.DeleteModel(
            name='Bookings',
        ),
        migrations.AlterModelTable(
            name='adminsetting',
            table='admin_setting',
        ),
        migrations.AlterModelTable(
            name='churchgroup',
            table='church_group',
        ),
        migrations.AlterModelTable(
            name='churchgroupdetail',
            table='church_group_detail',
        ),
        migrations.AlterModelTable(
            name='item',
            table='item',
        ),
        migrations.AlterModelTable(
            name='parishioner',
            table='parishioner',
        ),
        migrations.AlterModelTable(
            name='weddingbooking',
            table='wedding_booking',
        ),
    ]
