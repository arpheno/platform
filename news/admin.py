from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from models import Entry

admin.site.register(Entry)
