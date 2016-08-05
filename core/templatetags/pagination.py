# coding=utf-8

from django import template


register = template.Library()


@register.simple_tag
def simplemooc():
    return 'Simple MOOC'


@register.inclusion_tag('pagination.html')
def pagination(request, paginator, page_obj):
    context = {
        'request': request,
        'paginator': paginator,
        'page_obj': page_obj,
    }
    getvars = request.GET.copy()
    if 'page' in getvars:
        del getvars['page']
    if len(getvars) > 0:
        context['getvars'] = '&%s' % getvars.urlencode()
    return context
