from django.contrib import admin
from .models import Achievments,Testimonial,Form

class AcheivmentAdmin(admin.ModelAdmin):
    fields = ('photos', 'customers','photographs')


class TestimonialAdmin(admin.ModelAdmin):
    fields = ['description']

class formAdmin(admin.ModelAdmin):
    fields = ['Name','Email','Phone_no','Message']    

admin.site.register(Achievments,AcheivmentAdmin)
admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(Form,formAdmin)