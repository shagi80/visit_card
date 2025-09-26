import bleach
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import MinLengthValidator
from django.urls import reverse


class ProjectCategory(models.Model):
    # Project categories

    # Class value for skugs list (will be use in views)
    _category_slugs = []

    title = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name=_('Наименование категории'),
        help_text=_('Максимум 50 символов')
    )

    # SLUG for requests
    slug = models.SlugField(
        max_length=30,
        unique=True,
        validators=[MinLengthValidator(2, _('Минимум 2 символа'))],
        blank=False,
        null=False,
        verbose_name=_('SLUG для запросов')
    )

    image = models.ImageField(
        upload_to='categories/',
        verbose_name=_('Иконка'),
        null=True,
        help_text=_('Рекомендуемый размер: 48x48px')
    )

    hint = models.CharField(
        max_length=150,
        blank=False,
        null=True,
        verbose_name=_('Подсказка для кнопки'),
        help_text=_('До 150 символов')
    )

    short_description = models.TextField(
        max_length=300,
        validators=[MinLengthValidator(10, _('Минимум 50 символов'))],
        blank=False,
        null=True,
        verbose_name=_('Краткое описание'),
        help_text=_('10 - 300 символов')
    )

    skills = CKEditor5Field(
        blank=True,
        verbose_name=_('Описание навыков'),
        help_text=_('Форматированный текст с HTML')
    )

    resume = models.FileField(
        upload_to='resume',
        null=True,
        blank=True,
        verbose_name=_('Резюме'),
        help_text=_('Файл резюме')
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Порядок сортировки')
    )

    class Meta:
        verbose_name = _('Категория деятельности')
        verbose_name_plural = _('Категории деятельности')
        ordering = ['order', 'title']

    def get_absolute_url(self):
        return reverse('projects-category', kwargs={'category': self.slug})

    def __str__(self):
        return self.title

    @classmethod
    def get_category_slugs(cls):
        if not cls._category_slugs:
            ProjectCategory._category_slugs = ProjectCategory.objects.all()\
              .values_list('slug', flat=True)
        return cls._category_slugs


class Project(models.Model):
    # Projects

    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name=_('Название проекта'),
        help_text=_('Максимум 100 символов')
    )

    image = models.ImageField(
        upload_to='projects/',
        verbose_name=_('Главное изображение'),
        help_text=_('Рекомендуемый размер: 1200x800px')
    )

    category = models.ForeignKey(
        ProjectCategory,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Катгория проекта')
    )

    description = CKEditor5Field(
        verbose_name=_('Полное описание'),
        help_text=_('Форматированный текст с HTML')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Запись создана')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Запись обновлена')
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Порядок сортировки')
    )

    is_published = models.BooleanField(
        default=True,
        verbose_name=_('Проект опубликован')
    )

    class Meta:
        verbose_name = _('Проект')
        verbose_name_plural = _('Проекты')
        ordering = ['order', '-created_at']

    def get_absolute_url(self):
        return reverse('projects-category',
                       kwargs={'category': self.category.slug})

    def __str__(self):
        if self.category:
            category_title = self.category.title
        else:
            category_title = 'Нет категории'
        return _("{category}. {title}").format(
            category=_(category_title),
            title=_(self.title)
            )

    @property
    def add_images(self):
        return self.projectimage_set.all()

    # Clear HTML before save
    def save(self, *args, **kwargs):
        self.description = bleach.clean(
            self.description,
            tags=['p', 'a', 'ul', 'li', 'strong', 'em', 'b', 'span', 'div',
                  'h1', 'h2', 'h3', 'blockquote'],
            attributes={'a': ['href', 'title']})
        super().save(*args, **kwargs)


class ProjectImage(models.Model):
    # Additional images for progects

    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name=_('Название изображения'),
        help_text=_('Максимум 100 символов')
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name=_('Проект')
    )

    image = models.ImageField(
        upload_to='projects/',
        blank=False,
        null=False,
        verbose_name=_('Изображение'),
        help_text=_('Рекомендуемый размер: 1200x800px')
    )

    description = models.TextField(
      max_length=300,
      blank=True,
      verbose_name=_('Описание изображения'),
      help_text=_('Максимум 300 символов')
    )

    class Meta:
        verbose_name = _('Дополнитнльное изображение')
        verbose_name_plural = _('Дополнитнльные изображения')
        ordering = ['project', ]

    def __str__(self):
        return _("{project}. {title}").format(
            project=self.project.title,
            title=self.title)
