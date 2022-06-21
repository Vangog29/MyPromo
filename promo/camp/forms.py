from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from usermanag.models import ExtendedUser, Campaing, CampaignData, House, Poll, PoolForm
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




class CampRedactForm(ModelForm):
    house_camp = forms.ModelChoiceField(
                                        queryset=House.objects,
                                        to_field_name ="address",
                                        widget=forms.Select
                                        )
    user_camp = forms.IntegerField()
    camp_num = forms.IntegerField()

    class Meta(UserCreationForm.Meta):

        fields = ["user_camp", "house_camp", "camp_num", "poll_camp", "poll_form_camp"]
        model = CampaignData


class CampEditForm(ModelForm):
    campaign_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'card-text'}))
    campaign_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        fields = ["campaign_name", "campaign_description"]
        model = Campaing

class HouseEditForm (ModelForm):

    class Meta(UserCreationForm.Meta):
        fields = ["id_house", "address",]
        model = House


class FormPoll (ModelForm):
    door_open = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class' : 'custom-checkbox', 'id' : 'door_open'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'id':'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'id':'time'}))
    reaction = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'reaction'}))
    class Meta(UserCreationForm.Meta):
        fields = '__all__'
        model = Poll

class FormPollForm(ModelForm):
    resp_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'resp_name'}))
    resp_phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'resp_phone_number'}))
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id':'comment'}))

    class Meta(UserCreationForm):
        fields = ["resp_name", "resp_phone_number", "comment", "id_form"]
        model = PoolForm