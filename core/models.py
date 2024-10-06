# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.conf import settings
from django.db import models


class AdminInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=10, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50)  # Field name made lowercase.
    pword = models.CharField(db_column='Pword', max_length=50)  # Field name made lowercase.
    post = models.CharField(db_column='Post', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'admin_info'


class AdminSetting(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hall1 = models.DecimalField(db_column='Hall1', max_digits=10,
                                decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    hall2 = models.DecimalField(db_column='Hall2', max_digits=10,
                                decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        db_table = 'admin_setting'


class HallBooking(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    book_date = models.CharField(db_column='Book_Date', max_length=25)  # Field name made lowercase.
    book_time = models.CharField(db_column='Book_Time', max_length=10, blank=True,
                                 null=True)  # Field name made lowercase.
    hall = models.CharField(db_column='Hall', max_length=25)  # Field name made lowercase.
    customer_name = models.CharField(max_length=50)  # Field name made lowercase.
    amount_paid = models.DecimalField(db_column='Amount_Paid', max_digits=10,
                                      decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    balance = models.DecimalField(db_column='Balance', max_digits=10,
                                  decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    phone = models.CharField(db_column='Phone', max_length=11)  # Field name made lowercase.
    discount = models.IntegerField(db_column='Discount')  # Field name made lowercase.
    actual_book_date = models.DateTimeField(db_column='Actual_Book_Date')  # Field name made lowercase.

    class Meta:
        db_table = 'hall_booking'


class Calendar(models.Model):
    date_of_event = models.DateTimeField(db_column='Date of Event', blank=True,
                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    event_name = models.CharField(db_column='Event Name', blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    event_type = models.CharField(db_column='Event Type', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'calendar'


class ChurchGroupDetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_number = models.CharField(db_column='ID_Number', max_length=11, blank=True,
                                 null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    other_names = models.CharField(db_column='Other_Names', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    date_of_reg = models.DateTimeField(db_column='Date_Of_Reg', blank=True, null=True)  # Field name made lowercase.
    post_held = models.CharField(db_column='Post_Held', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    status_phone = models.CharField(db_column='Status_Phone', max_length=11, blank=True,
                                    null=True)  # Field name made lowercase.
    praesidium_committee = models.CharField(db_column='Praesidium_Committee', max_length=25, blank=True,
                                            null=True)  # Field name made lowercase.
    church_group = models.CharField(db_column='Church_Group', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'church_group_detail'


class ChurchGroup(models.Model):
    id_number = models.CharField(db_column='ID_Number', unique=True, max_length=11)  # Field name made lowercase.
    ppc = models.BooleanField(db_column='PPC', blank=True, null=True)  # Field name made lowercase.
    pfc = models.BooleanField(db_column='PFC', blank=True, null=True)  # Field name made lowercase.
    laity_council = models.BooleanField(db_column='Laity_Council', blank=True, null=True)  # Field name made lowercase.
    cmo = models.BooleanField(db_column='CMO', blank=True, null=True)  # Field name made lowercase.
    cwo = models.BooleanField(db_column='CWO', blank=True, null=True)  # Field name made lowercase.
    cyon = models.BooleanField(db_column='CYON', blank=True, null=True)  # Field name made lowercase.
    cgo = models.BooleanField(db_column='CGO', blank=True, null=True)  # Field name made lowercase.
    cba = models.BooleanField(db_column='CBA', blank=True, null=True)  # Field name made lowercase.
    choir = models.BooleanField(db_column='Choir', blank=True, null=True)  # Field name made lowercase.
    frsc = models.BooleanField(db_column='FRSC', blank=True, null=True)  # Field name made lowercase.
    legion_of_mary = models.BooleanField(db_column='Legion_of_Mary', blank=True,
                                         null=True)  # Field name made lowercase.
    blue_army = models.BooleanField(db_column='Blue_Army', blank=True, null=True)  # Field name made lowercase.
    sacred_heart = models.BooleanField(db_column='Sacred_Heart', blank=True, null=True)  # Field name made lowercase.
    block_rosary = models.BooleanField(db_column='Block_Rosary', blank=True, null=True)  # Field name made lowercase.
    saint_jude = models.BooleanField(db_column='Saint_Jude', blank=True, null=True)  # Field name made lowercase.
    infant_jesus = models.BooleanField(db_column='Infant_Jesus', blank=True, null=True)  # Field name made lowercase.
    purgatorian = models.BooleanField(db_column='Purgatorian', blank=True, null=True)  # Field name made lowercase.
    divine_mercy = models.BooleanField(db_column='Divine_Mercy', blank=True, null=True)  # Field name made lowercase.
    pages = models.BooleanField(db_column='Pages', blank=True, null=True)  # Field name made lowercase.
    saint_anthony = models.BooleanField(db_column='Saint_Anthony', blank=True, null=True)  # Field name made lowercase.
    saint_vincent_de_paul = models.BooleanField(db_column='Saint_Vincent_De_Paul', blank=True,
                                                null=True)  # Field name made lowercase.
    ccrn = models.BooleanField(db_column='CCRN', blank=True, null=True)  # Field name made lowercase.
    lectors = models.BooleanField(db_column='Lectors', blank=True, null=True)  # Field name made lowercase.
    church_warden = models.BooleanField(db_column='Church_Warden', blank=True, null=True)  # Field name made lowercase.
    holy_family = models.BooleanField(db_column='Holy_Family', blank=True, null=True)  # Field name made lowercase.
    saint_michael = models.BooleanField(db_column='Saint_Michael', blank=True, null=True)  # Field name made lowercase.
    precious_blood = models.BooleanField(db_column='Precious_Blood', blank=True,
                                         null=True)  # Field name made lowercase.
    holy_spirit = models.BooleanField(db_column='Holy_Spirit', blank=True, null=True)  # Field name made lowercase.
    altar_servers = models.BooleanField(db_column='Altar_Servers', blank=True, null=True)  # Field name made lowercase.
    christian_mothers = models.BooleanField(db_column='Christian_Mothers', blank=True,
                                            null=True)  # Field name made lowercase.
    revered_mothers = models.BooleanField(db_column='Revered_Mothers', blank=True,
                                          null=True)  # Field name made lowercase.
    jdpc = models.BooleanField(db_column='JDPC', blank=True, null=True)  # Field name made lowercase.
    cbiu = models.BooleanField(db_column='CBIU', blank=True, null=True)  # Field name made lowercase.
    nurses_guild = models.BooleanField(db_column='Nurses_Guild', blank=True, null=True)  # Field name made lowercase.
    sno = models.AutoField(db_column='SNo', unique=True, primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'church_group'


class ExpenditureAppraisal(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sno = models.CharField(db_column='SNo', max_length=10)  # Field name made lowercase.
    particulars = models.CharField(db_column='Particulars', max_length=100)  # Field name made lowercase.
    approved_expenditure = models.DecimalField(db_column='Approved Expenditure', max_digits=10, decimal_places=5,
                                               blank=True,
                                               null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    actual_expenditure = models.DecimalField(db_column='Actual Expenditure', max_digits=10, decimal_places=5,
                                             blank=True,
                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    savings = models.DecimalField(db_column='Savings', max_digits=10, decimal_places=5, blank=True,
                                  null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    excess = models.DecimalField(db_column='Excess', max_digits=10, decimal_places=5, blank=True,
                                 null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.

    class Meta:
        db_table = 'expenditure_appraisal'


class IncomeAppraisal(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sno = models.CharField(db_column='SNo', max_length=10)  # Field name made lowercase.
    income_subhead = models.CharField(db_column='Income Subhead',
                                      max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    approved_income = models.DecimalField(db_column='Approved Income', max_digits=10, decimal_places=5, blank=True,
                                          null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    actual_income = models.DecimalField(db_column='Actual Income', max_digits=10, decimal_places=5, blank=True,
                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    surplus = models.DecimalField(db_column='Surplus', max_digits=10, decimal_places=5, blank=True,
                                  null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    shortfall = models.DecimalField(db_column='Shortfall', max_digits=10, decimal_places=5, blank=True,
                                    null=True)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'income_appraisal'


class Item(models.Model):
    title = models.CharField(blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    owner = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'item'


class Journal(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    actual_date = models.DateTimeField(db_column='Actual_Date')  # Field name made lowercase.
    entry_date = models.CharField(db_column='Entry_Date', max_length=50)  # Field name made lowercase.
    entry = models.CharField(db_column='Entry', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'journal'


class Parishioner(models.Model):
    id_number = models.CharField(db_column='ID_Number', unique=True, max_length=11)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    other_names = models.CharField(db_column='Other_Names', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=50)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=10)  # Field name made lowercase.
    date_of_birth = models.DateTimeField(db_column='Date_Of_Birth', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marital_status = models.CharField(db_column='Marital_Status', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=11, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=11, blank=True, null=True)  # Field name made lowercase.
    phone3 = models.CharField(db_column='Phone3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    zone = models.CharField(db_column='Zone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    occupation = models.CharField(db_column='Occupation', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    baptised = models.BooleanField(db_column='Baptised', blank=True, null=True)  # Field name made lowercase.
    communicant = models.BooleanField(db_column='Communicant', blank=True, null=True)  # Field name made lowercase.
    confirmed = models.BooleanField(db_column='Confirmed', blank=True, null=True)  # Field name made lowercase.
    date_of_baptism = models.DateTimeField(db_column='Date_Of_Baptism', blank=True,
                                           null=True)  # Field name made lowercase.
    place_of_baptism = models.CharField(db_column='Place_Of_Baptism', max_length=50, blank=True,
                                        null=True)  # Field name made lowercase.
    baptised_by = models.CharField(db_column='Baptised_By', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    date_of_communion = models.DateTimeField(db_column='Date_Of_Communion', blank=True,
                                             null=True)  # Field name made lowercase.
    place_of_communion = models.CharField(db_column='Place_Of_Communion', max_length=50, blank=True,
                                          null=True)  # Field name made lowercase.
    communion_by = models.CharField(db_column='Communion_By', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    date_of_confirmation = models.DateTimeField(db_column='Date_Of_Confirmation', blank=True,
                                                null=True)  # Field name made lowercase.
    place_of_confirmation = models.CharField(db_column='Place_Of_Confirmation', max_length=50, blank=True,
                                             null=True)  # Field name made lowercase.
    confirmed_by = models.CharField(db_column='Confirmed_By', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    date_of_marriage = models.DateTimeField(db_column='Date_Of_Marriage', blank=True,
                                            null=True)  # Field name made lowercase.
    place_of_marriage = models.CharField(db_column='Place_Of_Marriage', max_length=50, blank=True,
                                         null=True)  # Field name made lowercase.
    solemnized_by = models.CharField(db_column='Solemnized_By', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.
    yr = models.IntegerField(db_column='Yr')  # Field name made lowercase.
    deceased = models.BooleanField(db_column='Deceased')  # Field name made lowercase.
    sno = models.AutoField(db_column='SNo', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    family_name = models.CharField(db_column='Family_Name', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    family_id = models.IntegerField(db_column='Family_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'parishioner'


class Sacrament(models.Model):
    sno = models.IntegerField(db_column='SNo')  # Field name made lowercase.
    lb_num = models.CharField(db_column='LB_Num', unique=True, max_length=13)  # Field name made lowercase.
    baptismal_name = models.CharField(db_column='Baptismal_Name', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.
    other_names = models.CharField(db_column='Other_Names', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date_of_birth = models.DateTimeField(db_column='Date_of_Birth', blank=True, null=True)  # Field name made lowercase.
    place_of_birth = models.CharField(db_column='Place_of_Birth', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.
    hometown = models.CharField(db_column='Hometown', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    father = models.CharField(db_column='Father', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mother = models.CharField(db_column='Mother', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date_of_baptism = models.DateTimeField(db_column='Date_of_Baptism', blank=True,
                                           null=True)  # Field name made lowercase.
    place_of_baptism = models.CharField(db_column='Place_of_Baptism', max_length=50, blank=True,
                                        null=True)  # Field name made lowercase.
    solemn = models.BooleanField(db_column='Solemn')  # Field name made lowercase.
    private = models.BooleanField(db_column='Private')  # Field name made lowercase.
    godfather = models.CharField(db_column='Godfather', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    godmother = models.CharField(db_column='Godmother', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    minister1 = models.CharField(db_column='Minister1', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    date_of_communion = models.DateTimeField(db_column='Date_of_Communion', blank=True,
                                             null=True)  # Field name made lowercase.
    place_of_communion = models.CharField(db_column='Place_of_Communion', max_length=50, blank=True,
                                          null=True)  # Field name made lowercase.
    minister2 = models.CharField(db_column='Minister2', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    confirmation_name = models.CharField(db_column='Confirmation_Name', max_length=50, blank=True,
                                         null=True)  # Field name made lowercase.
    date_of_confirmation = models.DateTimeField(db_column='Date_of_Confirmation', blank=True,
                                                null=True)  # Field name made lowercase.
    place_of_confirmation = models.CharField(db_column='Place_of_Confirmation', max_length=50, blank=True,
                                             null=True)  # Field name made lowercase.
    sponsor = models.CharField(db_column='Sponsor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    minister3 = models.CharField(db_column='Minister3', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    lm_num = models.CharField(db_column='LM_Num', max_length=10, blank=True, null=True)  # Field name made lowercase.
    spouse = models.CharField(db_column='Spouse', max_length=25, blank=True, null=True)  # Field name made lowercase.
    date_of_marriage = models.DateTimeField(db_column='Date_of_Marriage', blank=True,
                                            null=True)  # Field name made lowercase.
    place_of_marriage = models.CharField(db_column='Place_of_Marriage', max_length=50, blank=True,
                                         null=True)  # Field name made lowercase.
    witness1 = models.CharField(db_column='Witness1', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    witness2 = models.CharField(db_column='Witness2', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    witness3 = models.CharField(db_column='Witness3', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    minister4 = models.CharField(db_column='Minister4', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    sn = models.AutoField(db_column='SN', primary_key=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.baptismal_name} {self.surname}"

    class Meta:
        db_table = 'sacrament'
        ordering = ['sno']


class Users(models.Model):
    email = models.CharField(unique=True, blank=True, null=True)
    hashed_password = models.CharField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'users'


class WeddingBooking(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    book_date = models.CharField(db_column='Book_Date', max_length=50)  # Field name made lowercase.
    book_time = models.CharField(db_column='Book_Time', max_length=10, blank=True,
                                 null=True)  # Field name made lowercase.
    sponsus = models.CharField(db_column='Sponsus', max_length=50)  # Field name made lowercase.
    sponsa = models.CharField(db_column='Sponsa', max_length=50)  # Field name made lowercase.
    sponsus_phone = models.CharField(db_column='Sponsus_Phone', max_length=11)  # Field name made lowercase.
    sponsa_phone = models.CharField(db_column='Sponsa_Phone', max_length=11)  # Field name made lowercase.
    minister = models.CharField(db_column='Minister', max_length=50)  # Field name made lowercase.
    actual_book_date = models.DateTimeField(db_column='Actual_Book_Date')  # Field name made lowercase.

    class Meta:
        db_table = 'wedding_booking'


TITLES = (
('1', 'Very Rev. Fr.'), ('2', 'Rev. Fr.'), ('3', 'Catechist'), ('4', 'Brother'), ('5', 'Deacon'), ('6', 'Rev.'), ('7', 'Mr.'), ('8', 'Mrs.'), ('9', 'Miss'))
POSITIONS = (('1', 'Parish Priest'), ('2', 'Assistant Parish Priest'), ('3', 'Priest in Residence'), ('4', 'Catechist'),
             ('5', 'Seminarian'), ('6', 'Chairman, Laity Council'), ('7', 'Chairman, Parish Pastoral Council'), ('8', 'Chairman, Parish Finance Council'))
ROLES = (('1', 'Admin'), ('2', 'Priest'), ('3', 'Announcer'), ('4', 'Super Admin'))


class PriestProfile(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, choices=TITLES)  # Field name made lowercase.
    role = models.CharField(max_length=10, choices=ROLES)  # Field name made lowercase.
    firstname = models.CharField(max_length=50)  # Field name made lowercase.
    othernames = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
    lastname = models.CharField(max_length=11)  # Field name made lowercase.
    phone = models.CharField(max_length=11)  # Field name made lowercase.
    position = models.CharField(max_length=50, choices=POSITIONS)  # Field name made lowercase.
    date_of_birth = models.DateField()  # Field name made lowercase.
    photo = models.ImageField(upload_to='sfbc/profiles/',
                              default='sfbc/profiles/default.jpg')  # Field name made lowercase.

    class Meta:
        db_table = 'priest_profile'

    def __str__(self):
        return f"{self.get_title_display()} {self.firstname} {self.lastname}"
    
    
class AdminProfile(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, choices=TITLES, null=True, blank=True)  # Field name made lowercase.
    role = models.CharField(max_length=10, blank=True, null=True, choices=ROLES)  # Field name made lowercase.
    firstname = models.CharField(max_length=50)  # Field name made lowercase.
    othernames = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
    lastname = models.CharField(max_length=11)  # Field name made lowercase.
    phone = models.CharField(max_length=11)  # Field name made lowercase.
    position = models.CharField(max_length=50, choices=POSITIONS, null=True, blank=True)  # Field name made lowercase.
    photo = models.ImageField(upload_to='sfbc/profiles/',
                              default='sfbc/profiles/default.jpg')  # Field name made lowercase.

    class Meta:
        db_table = 'admin_profile'

    def __str__(self):
        return f"{self.get_title_display()} {self.firstname} {self.lastname}"


class Homily(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    author = models.ForeignKey(PriestProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)  # Field name made lowercase.
    content = models.TextField()  # Field name made lowercase.
    highlight = models.CharField(max_length=150)  # Field name made lowercase.
    entry_date = models.DateField()  # Field name made lowercase.
    photo = models.ImageField(upload_to='sfbc/homily/', default='sfbc/homily/default.jpg')  # Field name made lowercase.

    class Meta:
        db_table = 'homily'
        verbose_name_plural = 'homilies'

    def __str__(self):
        return f"{self.title} by {self.author.firstname} {self.author.lastname}"
    
    
class Announcement(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    author = models.ForeignKey(AdminProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)  # Field name made lowercase.
    content = models.TextField()  # Field name made lowercase.
    highlight = models.CharField(max_length=150)  # Field name made lowercase.
    entry_date = models.DateField()  # Field name made lowercase.
    photo = models.ImageField(upload_to='sfbc/announcements/', default='sfbc/announcements/default.jpg')  # Field name made lowercase.

    class Meta:
        db_table = 'announcement'


    def __str__(self):
        return f"{self.title} by {self.author.firstname} {self.author.lastname}"


class Event(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    author = models.ForeignKey(AdminProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)  # Field name made lowercase.
    content = models.TextField()  # Field name made lowercase.
    highlight = models.CharField(max_length=150)  # Field name made lowercase.
    entry_date = models.DateField()  # Field name made lowercase.
    event_date = models.DateField()  # Field name made lowercase.
    entry_time = models.TimeField()  # Field name made lowercase.
    venue = models.DateField()  # Field name made lowercase.
    photo = models.ImageField(upload_to='sfbc/events/', default='sfbc/events/default.jpg')  # Field name made lowercase.

    class Meta:
        db_table = 'event'


    def __str__(self):
        return f"{self.title} by {self.author.firstname} {self.author.lastname}"

MEMBER_TITLES = (('1', 'Catechist'), ('2', 'Mr.'), ('3', 'Mrs.'), ('4', 'Miss'), ('5', 'Chief'), ('6', 'Dr.'), ('7', 'Pharm.'), ('4', 'Engr.'))    
GROUP_POSITIONS = (('1', 'President'), ('2', 'Vice President'), ('3', 'Secretary'), ('4', 'Assistant Secretary'), ('5', 'Treasurer'), ('6', 'Financial Secretary'), ('7', 'Assistant Financial Secretary'), ('8', 'Public Relations Officer I'), ('9', 'Public Relations Officer II'), ('10', 'Director of Socials'), ('11', 'Provost'), ('12', 'Member'))
class GroupMember(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    # username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, choices=MEMBER_TITLES, null=True, blank=True)  # Field name made lowercase.
    # role = models.CharField(max_length=10, blank=True, null=True, choices=ROLES)  # Field name made lowercase.
    firstname = models.CharField(max_length=50)  # Field name made lowercase.
    othernames = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
    lastname = models.CharField(max_length=11)  # Field name made lowercase.
    phone = models.CharField(max_length=11)  # Field name made lowercase.
    position = models.CharField(max_length=50, choices=GROUP_POSITIONS, null=True, blank=True)  # Field name made lowercase.
    email = models.EmailField(max_length=60, null=True, blank=True)  # Field name made lowercase.
    address = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
    occupation = models.CharField(max_length=50, null=True, blank=True)  # Field name made lowercase.
    photo = models.ImageField(upload_to='sfbc/profiles/',
                              default='sfbc/profiles/default.jpg')  # Field name made lowercase.


    def __str__(self):
        return f"{self.get_title_display()} {self.firstname} {self.lastname}"
