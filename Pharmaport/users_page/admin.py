from django.contrib import admin
from users_page.models import otp,doc,connections_existed,files,connection_api

admin.site.register(otp)
admin.site.register(doc)
admin.site.register(connections_existed)
admin.site.register(files)
admin.site.register(connection_api)