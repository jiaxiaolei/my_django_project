# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin


from app_001.models import User
from app_001.models import  UserProfile
#from app_001.models import Total 

admin.site.register(User)

class TotalAdmin(admin.ModelAdmin):  

    #list_display = ('get_user_article')  
    list_display = ('name','get_user_article')  
  
    def get_user_article(self,user_id):  
        ret = User.objects.all()  
        sum = 0
        for item in ret:
            sum = sum + item.amount
        return sum  
  
    get_user_article.short_description = u'sum'
  
admin.site.register(UserProfile, TotalAdmin)  
#admin.site.register(Total, TotalAdmin)  
