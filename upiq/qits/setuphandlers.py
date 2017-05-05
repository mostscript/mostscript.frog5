from plone import api
from zope.component.hooks import getSite, setSite


# allowed styles for safe_html:
ALLOWED_STYLES = [
    u'text-align',
    u'list-style-type',
    u'float',
    u'padding-left',
    u'text-decoration',
    u'color',
    u'background-color',
    u'margin-left',
    u'margin-right',
    u'display'
    ]


def _siteBootstrap(site):
    if getSite() is not site:
        setSite(site)


def adjust_nav_displayed_types(context):
    _get = api.portal.get_registry_record
    _set = api.portal.set_registry_record
    site = context.getSite()
    _siteBootstrap(site)
    displayed_types = list(_get('plone.displayed_types'))
    types_to_remove = ['File', 'Image']
    for name in types_to_remove:
        displayed_types.remove(name)
    _set('plone.displayed_types', tuple(displayed_types))


def whitelist_safe_styles(context):
    site = context.getSite()
    tool = site.portal_transforms
    plugin = tool.get('safe_html')
    plugin._config['style_whitelist'] = ALLOWED_STYLES
    plugin._p_changed = True

