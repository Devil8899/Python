import views
def routers():
    urlpatterns = (
        ('/yuan',views.f1),
        ('/alex',views.f2),
        ("/cur_time",views.f3)
    )
    return urlpatterns