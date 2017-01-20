from django.conf.urls import url
from django.shortcuts import redirect

from members.views import json

urlpatterns = [
    url(r'^json/user_search/$', json.user_search, name='json_user_search'),
    url(r'^json/user_tags/$', json.user_tags, name='json_user_tags'),
    url(r'^json/org_tags/$', json.org_tags, name='json_org_tags'),
    url(r'^json/org_search/$', json.org_search, name='json_org_search'),
]

# Copyright 2017 Office Nomads LLC (http://www.officenomads.com/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
