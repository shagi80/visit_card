from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import ProjectCategory, Project


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['index', ]

    def location(self, item):
        return reverse(item)


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return ProjectCategory.objects.all()

    def lastmod(self, obj):
        last_project = obj.project_set.filter(is_published=True).order_by(
            '-updated_at').first()
        if last_project:
            return last_project.updated_at
        return None


class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Project.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at
