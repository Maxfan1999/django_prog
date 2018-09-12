from django.conf.urls import url, include
import views


urlpatterns = [
    url(r'^article/(?P<id>\d+)',views.article),
    url(r'^reg/$',views.reg),
    url(r'^login/$',views.user_login),
    url(r'^logout/$',views.user_logout),
    url(r'^add_article/$',views.add_article)
]