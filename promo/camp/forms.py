from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from usermanag.models import ExtendedUser, Campaing, CampaignData, House
from django.forms import ModelForm 
from django.contrib.auth import get_user_model


from django.forms.models import model_to_dict
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404


class CampManageForm(ModelForm):

    class Meta(UserCreationForm.Meta):
        fields = ["campaign_name", "campaign_description"]
        model = Campaing

class CampCreateForm(ModelForm):
    campaign_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    campaign_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta(UserCreationForm.Meta):
        fields = ["campaign_name", "campaign_description"]
        model = Campaing

class CampDataCreateForm(ModelForm):
    house_camp = forms.ModelChoiceField(queryset = House.objects.all())

    class Meta(UserCreationForm.Meta):
        fields = ["house_camp", "camp_num"]
        model = CampaignData


class CampRedactForm(ModelForm):
    
    class Meta(UserCreationForm.Meta):

        fields = ["user_camp", "house_camp", "camp_num", "poll_camp", "poll_form_camp"]
        model = CampaignData

class CampEditForm(ModelForm):
    campaign_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'card-text'}))
    campaign_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        fields = ["campaign_name", "campaign_description"]
        model = Campaing
