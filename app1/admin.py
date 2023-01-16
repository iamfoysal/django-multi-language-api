from django.contrib import admin
from parler.admin import TranslatableAdmin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from .models import *


class PostAdmin(TranslatableAdmin, SortableAdminMixin):

    list_display = ('title', 'short_description', 'description',
                    'author', 'created_on', 'updated_on')

    fieldsets = (
        (None, {

            'fields': ('title', 'short_description', 'description'),
        }),
    )

    def save_model(self, request, obj, form, change):

        obj.author_id = request.user.id

        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
