
from django.contrib import admin
from edu.models import Institute, Stream, University, XLAT, Application, Exam


class InstituteAdmin(admin.ModelAdmin):
	list_display = ('inst_id', 'name', 'university','aicte_approv_status','reg_state')
	search_fields = ['inst_id']
	list_filter = ['inst_id']

	def save_model(self, request, obj, form, change): 
		obj.created_by = request.user
		obj.save()

class StreamAdmin(admin.ModelAdmin):
	list_display = ('stream_code', 'name', 'description')
	search_fields = ['name']
	list_filter = ['stream_code']

	def save_model(self, request, obj, form, change): 
		obj.created_by = request.user
		obj.save()

class UniversityAdmin(admin.ModelAdmin):
	list_display = ('univ_id', 'name', 'aicte_approv_status','state','pin')
	search_fields = ['appln_id']
	list_filter = ['univ_id']

	def save_model(self, request, obj, form, change): 
		obj.created_by = request.user
		obj.save()

class XLATAdmin(admin.ModelAdmin):
	list_display = ('field_name', 'field_value','description')
	search_fields = ['field_name']
	list_filter = ['field_name']

	def save_model(self, request, obj, form, change): 
		obj.created_by = request.user
		obj.save()
	
class ApplicationAdmin(admin.ModelAdmin):
	list_display = ('appln_id', 'user', 'institute','stream','created_date')
	search_fields = ['appln_id']
	list_filter = ['appln_id']

	def save_model(self, request, obj, form, change): 
		obj.created_by = request.user
		obj.save()

admin.site.register(Institute, InstituteAdmin)
admin.site.register(Stream, StreamAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(XLAT, XLATAdmin)
admin.site.register(Application, ApplicationAdmin)

