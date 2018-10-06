from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
	path('', views.creator, name='creator'),
	path('topic',views.topics,name='top'),
	path('res',views.resource,name='res'),
	path('addR',views.addRes,name='addR'),
	path('addc',views.addcourse,name='addc'),
	path('reord',views.reorder,name='reord')
]
