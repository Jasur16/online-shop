from django.db import models
from django.utils.translation import gettext_lazy as _


class CaruselModel(models.Model):
    carusel_image = models.ImageField(upload_to='carusel/', verbose_name=_('carusel_image'))
    carusel_text = models.CharField(max_length=100, verbose_name=_('carusel_text'))
    carusel_title = models.CharField(max_length=100, verbose_name=_('carusel_title'))
    carusel_body = models.TextField(verbose_name=_('carusel_body'))

    def __str__(self):
        return self.carusel_title

    class Meta:
        verbose_name = 'carusel'
        verbose_name_plural = 'carusels'
        

class ContactModel(models.Model):
    name = models.CharField(max_length=32, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'