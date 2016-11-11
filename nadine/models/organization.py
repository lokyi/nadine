from __future__ import unicode_literals

import logging

from django.db import models
from django.core import urlresolvers
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class Organization(models.Model):
    created_ts = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="+")
    name = models.CharField(max_length=128)
    lead = models.ForeignKey(User, null=True, blank=True)

    def is_member(self, user, on_date=None):
        if not on_date:
            on_date = timezone.now().date()
        for m in OrganizationMember.objects.filter(organization=self, user=user):
            if m.is_active(on_date):
                return True
        return False

    def add_member(self, user, start_date=None):
        if not start_date:
            start_date = timezone.now().date()
        if self.is_member(user, start_date):
            raise Exception("User already a member")
        return OrganizationMember.objcts.create(organization=self, user=user, start_date=start_date)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'nadine'
        ordering = ['name']


class OrganizationMember(models.Model):
    """ A record of a user being part of an organization """
    organization = models.ForeignKey(Organization)
    user = models.ForeignKey(User)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def is_active(self, on_date=None):
        if not on_date:
            on_date = timezone.now().date()
        if self.start_date > on_date:
            return False
        return self.end_date == None or self.end_date >= on_date


class OrganizationNote(models.Model):
    created_ts = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="+")
    organization = models.ForeignKey(Organization)
    note = models.TextField()

    def __str__(self):
        if len(self.note) > 16:
            return "%s: %s" % (self.organization, self.note[16:])
        else:
            return "%s: %s" % (self.organization, self.note)

    class Meta:
        app_label = 'nadine'



# class OrganizationMembership(models.Model):
#     created_ts = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User, related_name="+")
#     organization = models.ForeignKey(Organization, related_name="membership")
#     allowances = models.ManyToManyField(ResourceAllowance)


# Copyright 2016 Office Nomads LLC (http://www.officenomads.com/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
