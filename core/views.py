from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView

from core.models import PriestProfile, Homily, Event, Announcement, Sacrament
from datetime import datetime
import re


# Create your views here.
# Home view
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = "Home"
        context['index'] = "active"
        context['priests'] = PriestProfile.objects.all()
        context['homilies'] = Homily.objects.all()[:5]

        return context


# About view
class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = "active"
        context['page'] = "About"
        return context


# Blog listing view
class HomilyView(TemplateView):
    template_name = 'homily.html'

    # You can add context if needed
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homily'] = "active"
        context['page'] = "Homily"
        context['homilies'] = Homily.objects.all()
        return context


# Blog detail view
class HomilyDetailView(DetailView):
    model = Homily  # Uncomment and modify based on your Blog model
    template_name = 'homily-single.html'

    context_object_name = 'homily'  # Name used in the template

    # If not using the model, you can manually get the object
    def get_object(self):
        homily_id = self.kwargs.get('id')
        print(homily_id)
        return get_object_or_404(Homily, id=homily_id)
        #return {'id': blog_id}  # Example for context

        # You can add context if needed

    def get_context_data(self, **kwargs):
        homily_id = self.kwargs.get('id')
        context = super().get_context_data(**kwargs)
        context['page'] = f"Homily - {Homily.objects.values_list('title', flat=True).get(id=homily_id)}"
        return context


# Blog listing view
class AnnouncementView(TemplateView):
    template_name = 'announcements.html'

    # You can add context if needed
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcement'] = "active"
        context['page'] = "Announcements"
        context['announcements'] = Announcement.objects.all()
        return context


# Blog listing view
class EventView(TemplateView):
    template_name = 'announcements.html'

    # You can add context if needed
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = "active"
        context['page'] = "Events"
        context['events'] = Event.objects.all()
        return context


# Blog listing view
class SacramentView(TemplateView):
    template_name = 'inner-page.html'

    target_date = datetime(1753, 1, 1)

    # You can add context if needed
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = "active"
        context['page'] = "Sacraments"
        # Sacrament.objects.filter(minister2__contains="REV. FR. A. D. NZEMEKE").update(
        #     minister2="REV. FR. A. D. NZEMEKE")
        # Sacrament.objects.filter(date_of_marriage=datetime(1753, 1, 1)).update(date_of_marriage=None)
        context['sacrament_register'] = Sacrament.objects.all()
        return context

    # def get(self, request, *args, **kwargs):
    #     # Fetch all records from the Sacrament model
    #     instances = Sacrament.objects.all()
    #
    #     # List of fields to clean
    #     fields_to_clean = [
    #         'sponsor', 'place_of_baptism',
    #     ]
    #
    #     # Iterate over all records
    #     for instance in instances:
    #         for field in fields_to_clean:
    #             # Get the raw value from each field
    #             raw_value = getattr(instance, field)
    #
    #             if raw_value:
    #                 # Step 1: Remove everything before and including "TRIAL-"
    #                 cleaned_value = re.sub(r'^.*TRIAL-', '', raw_value)
    #
    #                 # Step 2: Remove trailing numbers and the preceding space
    #                 cleaned_value = re.sub(r'\s\d+$', '', cleaned_value)
    #
    #                 # Update the field with the cleaned value
    #                 setattr(instance, field, cleaned_value)
    #
    #         # Save the updated instance
    #         instance.save()
    #
    #     # After updating, redirect to a success page
    #     return redirect('sacraments')


class SacramentDetailView(DetailView):
    model = Sacrament  # Uncomment and modify based on your Blog model
    template_name = 'card.html'

    context_object_name = 'parishioner'  # Name used in the template

    # If not using the model, you can manually get the object
    def get_object(self):
        sacrament_id = self.kwargs.get('lb_num')
        print(sacrament_id)
        return get_object_or_404(Sacrament, lb_num=sacrament_id)
        # return {'id': blog_id}  # Example for context

        # You can add context if needed

    def get_context_data(self, **kwargs):
        sacrament_id = self.kwargs.get('lb_num')
        context = super().get_context_data(**kwargs)
        context['page'] = f"Baptismal Card" # - {Sacrament.objects.values_list('baptismal_name', flat=True).get(
        # lb_num=sacrament_id)}"
        return context
