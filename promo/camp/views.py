from django.shortcuts import render
from camp.forms import CampManageForm, CampCreateForm, CampDataCreateForm, CampRedactForm, CampEditForm, HouseEditForm, FormPoll
from usermanag.models import Campaing, CampaignData, House

# Create your views here.
def mycamp(request):

    if request.method == "GET":
        camp_dat = CampaignData.objects.filter(user_camp_id = request.user.id)
        return render(request, "mycamp.html", {"camp": camp_dat})
    elif request.method == "POST":
        form = CampManageForm(request.POST)
        if form.is_valid():
            camp = form.save()
            return render(request, "mycamp.html")
        else:
            data = form.errors
            return render(request, "error.html", {'data' : data})


def createcamp(request):
    if request.method == "POST":
        form_cam_create = CampCreateForm(request.POST)
        create_camp_data = CampaignData.objects.create()
        if form_cam_create.is_valid():
            form_cam_create = form_cam_create.save()
            create_camp_data.camp_num = form_cam_create
            create_camp_data.user_camp = request.user
            create_camp_data.save()
        else:
            data = form_cam_create.errors
            return render(request, "error.html", {'data' : data})
    form_cam_create = CampCreateForm()
    data_cam = {'form_cam_create': form_cam_create}
    return render(request, "createcamp.html", data_cam)


def camps(request):
    camp_data = CampaignData.objects.all()
    return render(request, "camps.html", {"data" : camp_data})

        

def showcamp(request, id_campaign):
    camp_data = CampaignData.objects.filter(camp_num_id = id_campaign)
    return render(request, "showcamp.html", {"data" : camp_data})


def editcamp(request, id_campaign):
    camp_data = CampaignData.objects.get(camp_num_id = id_campaign)
    camp = Campaing.objects.get(id_campaign = camp_data.camp_num_id)
    if request.method == "POST":
        form_camp = CampEditForm(request.POST, instance=camp)
        if form_camp.is_valid():
            form_camp.save()
        else:
            print(form_camp.errors)
            print('EROOOOORRRRR')
        
    
    form_camp = CampEditForm()
    form_camp.fields['campaign_name'].initial = camp_data.camp_num.campaign_name
    form_camp.fields['campaign_description'].initial = camp_data.camp_num.campaign_description

    return render(request, "editcamp.html", {"data" : camp_data, "form_camp" : form_camp})


def homeedit(request, id_campaign):
    house = House.objects.all()
    if request.method == "POST":
        camp_data = CampaignData.objects.get(camp_num_id=id_campaign)
        form_redact_camp = CampRedactForm()
        form_redact_camp.fields['user_camp'] = request.user
        form_redact_camp.fields['camp_num'] = camp_data.camp_num
        house_data = request.POST
        id_h = House.objects.get(id_house=house_data.get('house'))
        form_redact_camp.fields['house_camp'] = id_h
        poll_form = FormPoll(request.POST)
        if form_redact_camp.is_valid():
            form_redact_camp.save()
        else:
            print(form_redact_camp.errors)
            print('EROOOOORRRRR')
        if request.POST.get('poll') == 'on':
            if poll_form.is_valid():
                poll_form.save()
            else:
                print(poll_form.errors)
                print('EROOOOORRRRR')


    poll_form = FormPoll()
    return render(request, "homeedit.html", {"house" : house, "poll_form" : poll_form})

