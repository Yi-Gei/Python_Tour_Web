from django.contrib import admin

from tour.models import Group

from tour.models import HotCity

from tour.models import HotLine

class GroupAdmin(admin.ModelAdmin):
	list_display = ('Gp','GpId','Gp_PubDate','Gp_StartDate','Gp_lp','Gp_Type','Gp_description','Gp_Img');

class HotCityAdmin(admin.ModelAdmin):
	list_display = ('HCity','HCId','HC_PubDate','HC_StartDate','HC_lp','HC_Type','HC_description','HC_Img');

class HotLineAdmin(admin.ModelAdmin):
	list_display = ('HLine','HLId','HL_PubDate','HL_StartDate','HL_lp','HL_Type','HL_description','HL_Img');

admin.site.register(Group,GroupAdmin);
admin.site.register(HotCity,HotCityAdmin);
admin.site.register(HotLine,HotLineAdmin);
# Register your models here.
