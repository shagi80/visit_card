from datetime import date
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.views import View
from django.template import loader

from .models import Project, ProjectCategory, ProjectImage


# Calculate age from birthday
def GetMyAge():
    birthday = date(1980, 6, 19)
    today = date.today()
    return today.year - birthday.year - ((today.month, today.day) <
                                         (birthday.month, birthday.day))


class IndexPage(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["age"] = GetMyAge()
        context["navbar_transparent"] = True
        context['categories'] = ProjectCategory.objects.all()[1:]
        return context


class ProjectListView(ListView):
    model = Project
    template_name = 'main/projects.html'
    context_object_name = 'projects'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('category')
        if (slug in ProjectCategory.get_category_slugs()) and (slug != 'all'):
            queryset = queryset.filter(category__slug=slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('category')
        if not slug:
            slug = 'all'
        сategories = ProjectCategory.objects.all()
        current_category = None
        if (slug in ProjectCategory.get_category_slugs()):
            current_category = сategories.filter(slug=slug).first()
        context['categories'] = сategories
        context['current_category'] = current_category
        context["navbar_transparent"] = False
        return context


def project_images_list(request, project_pk):
    context = {}

    if project_pk:
        images = ProjectImage.objects.filter(
            project__pk=project_pk
        ).prefetch_related("project").values('image', 'description')

        if images.exists():
            context['first_images'] = images.first()
            context['images'] = images[1:]
            return render(request, 'main/project_images.html', context)

    raise Http404("Project not found or no images available")


class RobotsTxtView(View):
    def get(self, request):
        template = loader.get_template('main/robots.txt')
        context = {
            'sitemap_url': "https://" + request.get_host() + "/sitemap.xml"
        }
        return HttpResponse(template.render(context, request),
                            content_type='text/plain')
