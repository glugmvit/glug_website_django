from django.urls import path
from events import views

app_name = 'events'

urlpatterns = [
	path('',views.index,name='index'),
	path('ai-gaming', views.ai_gaming, name="ai_gaming"),
	
]
