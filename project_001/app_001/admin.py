# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from django.conf import settings


from app_001.models import User
from app_001.models import  UserProfile
#from app_001.models import Total 

admin.site.register(User)

class TotalAdmin(admin.ModelAdmin):  

    #list_display = ('get_user_article')  
    list_display = ('name','get_user_article', 'test', 'test2')  
  
    def get_user_article(self,user_id):  
        ret = User.objects.all()  
        sum = 0
        for item in ret:
            sum = sum + item.amount
        return sum  
  
    get_user_article.short_description = u'sum'
  
    def test(self, user_id):  
        #return  '2.5%'  
        return settings.TAX_RATE_STR

    def test2(self, user_id):  
        ret = User.objects.all()  
        sum = 0
        for item in ret:
            sum = sum + item.amount
        return sum * settings.TAX_RATE
        #return sum * 0.025
  
    get_user_article.short_description = u'sum'
    test.short_description = u'tax rate'
    test2.short_description = u'tax'
 
  
admin.site.register(UserProfile, TotalAdmin)  
#admin.site.register(Total, TotalAdmin)  
