from django.contrib import admin
from .models import ExtendedUser, House, Campaing, Poll, PoolForm, CampaignData

# Register your models here.
admin.site.register(ExtendedUser)
admin.site.register(House)
admin.site.register(Campaing)
admin.site.register(Poll)
admin.site.register(PoolForm)
admin.site.register(CampaignData)
