from django import template

register = template.Library()


@register.simple_tag
def filter_query(queryset, **filters):
    if not filters:
        raise template.TemplateSyntaxError('`filter_query` tag requires filters.')
    return queryset.filter(**filters).all()

