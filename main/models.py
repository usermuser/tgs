# -*- coding: utf-8 -*-
from django.core import validators
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.

@python_2_unicode_compatible
class Phone(models.Model):
	phone_number = models.CharField(max_length=16,validators=[validators.RegexValidator(regex=r'^(8|\+7)(\(|\ )\d{3}(\)|\ )\d{3}(\-|\ )\d{2}(\-|\ )\d{2}$',message=u'Приемлемый формат ввода - 8(888)888 88 88, 8 888 888 88 88, +7 888 888-88-88'),])
	class Meta:
		ordering = ('phone_number',)
		verbose_name = "Номер телефона"
		verbose_name_plural = "Номер телефона"
	
	def __str__(self):
		return self.phone_number
