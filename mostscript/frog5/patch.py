# monkey patches
import json

try:
    # Plone 5.1+
    from Products.CMFPlone.patterns.settings import PatternSettingsAdapter
except:
    # Plone 5.0.x
    PatternSettingsAdapter = None
    from Products.CMFPlone.patterns import PloneSettingsAdapter

    
def patch_tinymce_settings():
    cls = PatternSettingsAdapter or PloneSettingsAdapter
    _orig = cls.tinymce

    def wrapper(self):
        result = _orig(self)
        config = json.loads(result['data-pat-tinymce'])
        config['relatedItems']['mode'] = 'browse'
        return {'data-pat-tinymce': json.dumps(config)}
    setattr(cls, 'tinymce', wrapper)


def patch_access_logging():
    """
    Monkey patch access logging with a wrapper that returns
    before emitting any messages for OPTIONS requests from haproxy
    health checks.
    """
    from ZServer.AccessLogger import AccessLogger
    _orig = AccessLogger.log

    def newlog(self, message):
        if 'OPTIONS / HTTP/1.0' in message:
            return  # do not emit log message for haproxy health check
        _orig(self, message)

    setattr(AccessLogger, 'log', newlog)

