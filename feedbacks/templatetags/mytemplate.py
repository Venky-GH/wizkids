from django import template
from creator.models import course, topic, content
from django.db.models import Q

register = template.Library()

@register.filter(name='my_filter')
def my_filter(did, stxt):
    tops = topic.objects.filter(cid=did).order_by('oid')
    return tops.all()

@register.filter(name='filter_content')
def filter_content(td,sometxt):
    cons = content.objects.filter(tid=td)
    return cons.all()