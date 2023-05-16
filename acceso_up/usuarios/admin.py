from django.contrib import admin
from usuarios.models import usuario

from django.utils.html import format_html
from django.utils.safestring import mark_safe
import os
from django.conf import settings

admin.site.site_header = "Administracion del control de acceso UP"
admin.site.site_title = "Administracion control de acceso UP"
admin.site.index_title = "Bienvenido Administrador!"


admin.site.register(usuario)