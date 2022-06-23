from django.shortcuts import render
from camp.forms import CampManageForm, CampCreateForm, CampRedactForm, CampEditForm, HouseEditForm, FormPoll, FormPollForm
from usermanag.models import Campaing, CampaignData, House, Poll, PoolForm

# Create your views here.
def mycamp(request):

    if request.method == "GET":
        camp_dat_id = CampaignData.objects.filter(user_camp_id = request.user.id)
        uniq_id = []
        for n in camp_dat_id:
            if n.camp_num_id not in uniq_id:
                uniq_id.append(n.camp_num_id)
        uniq_id.sort()
        camp_dat = Campaing.objects.filter(id_campaign__in=uniq_id)

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
    camp_data = Campaing.objects.all()
    return render(request, "camps.html", {"data" : camp_data})

        

def showcamp(request, id_campaign):
    camp_data = Campaing.objects.filter(id_campaign = id_campaign)
    all_data = CampaignData.objects.filter(camp_num_id = id_campaign)
    return render(request, "showcamp.html", {"data" : camp_data, "all_data" : all_data})


def editcamp(request, id_campaign):
    #camp_data = CampaignData.objects.get(camp_num_id = id_campaign)
    #camp = Campaing.objects.get(id_campaign = camp_data.camp_num_id)
    camp_data = Campaing.objects.get(id_campaign=id_campaign)
    data = CampaignData.objects.filter(camp_num_id = id_campaign)
    if request.method == "POST":
        form_camp = CampEditForm(request.POST, instance=camp_data)
        if form_camp.is_valid():
            form_camp.save()
        else:
            print(form_camp.errors)
            print('EROOOOORRRRR')
        
    
    form_camp = CampEditForm()
    form_camp.fields['campaign_name'].initial = camp_data.campaign_name
    form_camp.fields['campaign_description'].initial = camp_data.campaign_description

    return render(request, "editcamp.html", {"data" : data, "form_camp" : form_camp, "camp_data" : camp_data})


def homeedit(request, id_campaign):
    form = CampRedactForm()
    camp = Campaing.objects.get(id_campaign=id_campaign)

    if request.method == "POST":
        form = CampRedactForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_camp = request.user
            obj.camp_num = camp
            obj.save()
            print (form)
        else:
            print(form.errors)
            print('EROOOOORRRRR')

    return render(request, "homeedit.html", {"form" : form})

def polledit(request, id_campaign):
    form = FormPoll()
    poll = Poll.objects.all()
    if request.method == "POST":
        form = FormPoll(request.POST)
        if form.is_valid():
            form.save()

        else:
            print(form.errors)
            print('EROOOOORRRRR')
    poll = Poll.objects.all()
    return render(request,"polledit.html", {"form": form, "poll": poll})

def formpoll (request, id_campaign):
    form = FormPollForm()
    poll_form = PoolForm.objects.all()

    if request.method == "POST":
        form = FormPollForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            print('EROOOOORRRRR')

    poll_form = PoolForm.objects.all()
    return render(request, "formpoll.html", {"form": form, "poll_form": poll_form})

def showpoll(request, id_poll):
    poll_data = Poll.objects.get(id_poll=id_poll)
    return render(request, "showpoll.html", {"poll_data" : poll_data} )

def showpollform(request, id_form):
    poll_form_data = PoolForm.objects.get(id_form=id_form)
    return render(request, "showpollform.html", {"poll_form_data" : poll_form_data})
