from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.forms import formset_factory
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Agent
from .forms import *
from django.shortcuts import render

# def amange_view(request):
#     AgentFormSet = formset_factory(AgentForm)
#     LocationFormSet = formset_factory(LocationForm)
#     AddressFormSet = formset_factory(AddressForm)
#
#     if request.method == 'POST':
#         agent

class AgentList(ListView):
    model = Agent


class AgentCreate(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence', 'agent_notes']


class AgentLocationCreate(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence',
              'agent_notes']
    success_url = reverse_lazy('agent-list')

    def get_context_data(self, **kwargs):
        data = super(AgentLocationCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['location'] = LocationFormSet(self.request.POST)
        else:
            data['location'] = LocationFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        location = context['location']
        with transaction.atomic():
            self.object = form.save()

            if location.is_valid():
                location.instance = self.object
                location.save()
        return super(AgentLocationCreate, self).form_valid(form)


class AgentAddressCreate(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence',
              'agent_notes']
    success_url = reverse_lazy('agent-list')

    def get_context_data(self, **kwargs):
        data = super(AgentAddressCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['address'] = AddressFormSet(self.request.POST)
        else:
            data['address'] = AddressFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        address = context['address']
        with transaction.atomic():
            self.object = form.save()

            if address.is_valid():
                address.instance = self.object
                address.save()
        return super(AgentAddressCreate, self).form_valid(form)




class AgentUpdate(UpdateView):
    model = Agent
    success_url = '/'
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence',
              'agent_notes']




class AgentLocationUpdate(UpdateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence',
              'agent_notes']
    success_url = reverse_lazy('agent-list')

    def get_context_data(self, **kwargs):
        data = super(AgentLocationUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['location'] = LocationFormSet(self.request.POST, instance=self.object)
        else:
            data['location'] = LocationFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        location = context['location']
        with transaction.atomic():
            self.object = form.save()

            if location.is_valid():
                location.instance = self.object
                location.save()
        return super(AgentLocationUpdate, self).form_valid(form)


class AgentAddressUpdate(UpdateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experence',
              'agent_notes']
    success_url = reverse_lazy('agent-list')

    def get_context_data(self, **kwargs):
        data = super(AgentAddressUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['address'] = AddressFormSet(self.request.POST, instance=self.object)
        else:
            data['address'] = AddressFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        address = context['address']
        with transaction.atomic():
            self.object = form.save()

            if address.is_valid():
                address.instance = self.object
                address.save()
        return super(AgentAddressUpdate, self).form_valid(form)



class AgentDelete(DeleteView):
    model = Agent
    success_url = reverse_lazy('agent-list')



