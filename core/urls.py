from django.urls import path

from core.views import HomeView, HomilyView, HomilyDetailView, AboutView, AnnouncementView, EventView, SacramentView, \
    SacramentDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('homily/', HomilyView.as_view(), name='homilies'),
    path('homily/<int:id>/', HomilyDetailView.as_view(), name='homily-detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('announcements/', AnnouncementView.as_view(), name='announcements'),
    path('events/', EventView.as_view(), name='events'),
    path('sacraments/', SacramentView.as_view(), name='sacraments'),
    path('sacrament/<str:lb_num>/', SacramentDetailView.as_view(), name='sacrament-detail'),
]
