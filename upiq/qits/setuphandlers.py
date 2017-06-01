from persistent.mapping import PersistentMapping
from plone import api
from zope.annotation.interfaces import IAnnotations
from zope.component.hooks import getSite
from zope.component.hooks import setSite


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
    changed = False
    _get = api.portal.get_registry_record
    _set = api.portal.set_registry_record
    site = context.getSite()
    _siteBootstrap(site)
    displayed_types = list(_get('plone.displayed_types'))
    types_to_remove = ['File', 'Image']
    for name in types_to_remove:
        if name in displayed_types:
            displayed_types.remove(name)
            changed = True
    if changed:
        _set('plone.displayed_types', tuple(displayed_types))


def whitelist_safe_styles(context):
    site = context.getSite()
    tool = site.portal_transforms
    plugin = tool.get('safe_html')
    plugin._config['style_whitelist'] = ALLOWED_STYLES
    plugin._p_changed = True


def documentviewer_config(context):
    site = context.getSite()
    anno = IAnnotations(site)
    config = anno.get('collective.documentviewer')
    if config is None:
        config = PersistentMapping()
        anno['collective.documentviewer'] = config
    config['auto_layout_file_types'] = ['ppt', 'word', 'rft', 'excel', 'pdf']

