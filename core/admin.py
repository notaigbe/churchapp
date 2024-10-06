from django.contrib import admin

from core.models import AdminInfo, AdminSetting, HallBooking, ChurchGroupDetail, ChurchGroup, ExpenditureAppraisal, \
    IncomeAppraisal, Item, Journal, Parishioner, Sacrament, WeddingBooking, PriestProfile, Homily, Announcement, AdminProfile, Event

# Register your models here.
admin.site.register(AdminInfo)
admin.site.register(AdminSetting)
admin.site.register(HallBooking)
admin.site.register(ChurchGroupDetail)
admin.site.register(ChurchGroup)
admin.site.register(ExpenditureAppraisal)
admin.site.register(IncomeAppraisal)
admin.site.register(Item)
admin.site.register(Journal)
admin.site.register(Parishioner)
admin.site.register(Sacrament)
admin.site.register(WeddingBooking)
admin.site.register(PriestProfile)
admin.site.register(AdminProfile)
admin.site.register(Announcement)
admin.site.register(Homily)
admin.site.register(Event)
