from PIL.Image import Image
from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    class AppType(models.TextChoices):
        DJANGO_APP = "DJ", _('Django')
        ANDROID_APP = "AN", _('Android')
        PYTHON_APP = "PY", _('Python')

    class EventDoc(models.TextChoices):
        IS_DOC = "Y", _('Yes')
        IS_NOT_DOC = "N", _('No')

    class ResLinks(models.TextChoices):
        IS_RES = "Y", _('Yes')
        IS_NOT_RES = "N", _('No')

    event_title = models.CharField(max_length=50
                                   )

    event_date = models.DateField()

    event_image_icon = models.ImageField(upload_to='event_icons/', default='prod_default_image.png')

    event_type = models.CharField(max_length=30,
                                  choices=AppType.choices
                                  )

    event_doc_link = models.CharField(max_length=2,
                                      choices=EventDoc.choices
                                      )

    post_res_link = models.CharField(max_length=2,
                                     choices=ResLinks.choices
                                     )

    event_doc_file = models.CharField(max_length=150,
                                         default="No"
                                         )

    production_icon = models.ImageField(upload_to='event_icons/', default='prod_default_image.png')

    event_github_link = models.CharField(max_length=150,
                                         default="No"
                                         )

    event_production_link = models.CharField(max_length=150,
                                             default="No"
                                             )

    event_title_date_color = models.CharField(max_length=6,
                                              default="ff927b"
                                              )

    event_description = models.TextField(max_length=600,
                                         default="")

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open()
    #     if img.height > 300 or img.width>300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.)

    def __str__(self):
        return self.event_title


class Tech(models.Model):
    tech_name = models.CharField(max_length=50,
                                 default="")

    tech_link = models.CharField(max_length=150,
                                 default="")

    event = models.ForeignKey(
        'event.Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.event.event_title + " " + "tech" + " " + self.tech_name


class PostScreen(models.Model):
    event_screenshot = models.ImageField(upload_to='event_icons/', default='prod_default_image.png')
    event = models.ForeignKey(
        'event.Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.event.event_title + " " + "screen"


class PostRes(models.Model):
    res_name = models.CharField(max_length=50,
                                default="")

    res_link = models.CharField(max_length=150,
                                default="")
    event = models.ForeignKey(
        'event.Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.event.event_title + " " + "resource" + " " + self.res_name
