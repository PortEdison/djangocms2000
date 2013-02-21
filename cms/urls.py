import os

from django.conf.urls import *

import settings


urlpatterns = patterns('cms.views',
	(r'^actions/savepage/$', 'savepage'),
	(r'^actions/savepage/(\d+)/$', 'savepage'),
	(r'^actions/saveblock/(\d+)$', 'saveblock'),
	(r'^actions/saveimage/(\d+)$', 'saveimage'),
	
	(r'^login/$', 'login'),
	(r'^logout/$', 'logout'),
	(r'^block_admin_init.js$', 'block_admin_init'),
    (r'^linklist.js$', 'linklist'),
)
