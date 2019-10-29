# -*- coding: utf-8 -*-

"""djhost middleware

djhost middleware to route different hosts to different urlconfs

-------------------------------------------------------------------
Copyright: Md. Jahidul Hamid <jahidulhamid@yahoo.com>

License: [BSD](http://www.opensource.org/licenses/bsd-license.php)
-------------------------------------------------------------------
"""


import re

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class HostsMiddleware(MiddlewareMixin):
    """Rout hosts to corresponding urlconfs.
    
    urlconfs should be defined in DJHOST_CONF_EXACT and DJHOST_CONF_REGEX for exact and regex matching of hosts respectively.
    
    """
    def process_request(self, request):
        host = request.get_host()

        djhost_conf = getattr(settings, 'DJHOST_CONF_EXACT', None)
        if djhost_conf:
            if host in djhost_conf:
                request.urlconf = djhost_conf[host]
        
        djhost_conf = getattr(settings, 'DJHOST_CONF_REGEX', None)
        if djhost_conf:
            for k,v in djhost_conf.items():
                if re.match(k, host):
                    request.urlconf = v
                    break