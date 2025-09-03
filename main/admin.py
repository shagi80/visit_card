from django.contrib import admin
from .models import Project, ProjectImage, ProjectCategory
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe


class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'hint', 'order')
    readonly_fields = ('image_preview', )
    fieldsets = [
        (_('Cвойства'), {
            'fields': ('title',
                       'slug',
                       'image',
                       'image_preview',
                       'hint',
                       'short_description',
                       'order',
                       'skills',
                       'resume'
                       ),
        })
    ]

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" '
                f'style="max-height: 48px;" />'
            )
        return "Нет изображения"

    image_preview.short_description = ''


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_published', 'order')
    list_filter = ('category', 'is_published')
    readonly_fields = ('image_preview', )
    search_fields = ('title', )
    fieldsets = [
        (_('Описание'), {
            'fields': ('title',
                       'category',
                       'image',
                       'image_preview',
                       'description'
                       ),
            'description': _("Описание проекта")
        }),
        (_('Сервис'), {
            'fields': ('order', 'is_published'),
            'classes': ('wide'),
            'description': _("Служебные поля")
        })
    ]

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" '
                f'style="max-height: 100px;" />'
            )
        return "Нет изображения"

    image_preview.short_description = ''


class ProjectImageAdmin(admin.ModelAdmin):
    fields = ('title', 'project', 'image', 'image_preview', 'description')
    list_display = ('project', 'title', )
    list_display_links = ('title', )
    list_select_related = ('project', )
    readonly_fields = ('image_preview', )
    search_fields = ('title', 'project__title')
    list_filter = ('project__category', )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" '
                f'style="max-height: 100px;" />'
            )
        return "Нет изображения"

    image_preview.short_description = ''


admin.site.register(ProjectCategory, ProjectCategoryAdmin)

admin.site.register(Project, ProjectAdmin)

admin.site.register(ProjectImage, ProjectImageAdmin)

admin.site.site_header = 'Шагинян СВ. Визитка.'
