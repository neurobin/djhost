# -*- coding: utf-8 -*-

"""djhost middleware

djhost middleware to route different hosts to different urlconfs

-------------------------------------------------------------------
Copyright: Md. Jahidul Hamid <jahidulhamid@yahoo.com>

License: [BSD](http://www.opensource.org/licenses/bsd-license.php)
-------------------------------------------------------------------
"""




from django.conf import settings


class MultipleDomainMiddleware(object):
    def process_request(self, request):
        url_config = getattr(settings, 'MULTIURL_CONFIG', None)
        if not url_config:
            return

        host = request.get_host()
        if host in url_config:
            request.urlconf = url_config[host]