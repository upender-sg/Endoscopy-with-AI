# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from uuid import uuid4

from django.core import validators
from django.db import models

#from utils import validators as cust_validators


class UUIDModel(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


