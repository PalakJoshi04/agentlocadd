from django.forms import ModelForm, inlineformset_factory
from .models import Agent, Location, Address

class AgentForm(ModelForm):
    class Meta:
        model = Agent
        exclude = ()


class LocationForm(ModelForm):
    class Meta:
        model = Location
        exclude = ()


class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ()

LocationFormSet = inlineformset_factory(Agent, Location, form=LocationForm, extra=1)
AddressFormSet = inlineformset_factory(Agent, Address, form=AddressForm, extra=1)
