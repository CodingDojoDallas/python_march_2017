from django.conf.urls import url
from . import views


# Models -- views -- TEMPLATES


# def method_to_run(request):
#     print "Whatever route that was hit by an HTTP request (by the way) decided to invoke me!"
#     print "By the way, here's the request object that Django automatically passes us:", request
#     print "By the by, we still aren't delivering anything to the browser, so you should see 'ValueError at /'"
#
# urlpatterns = [
#     url(r'^$', method_to_run)
# ]

# same same in Flask:
# @app.route('/')
# def method_to_run():


urlpatterns = [
    url(r'^', views.index)  # specifically: r'^$' and r'^generate/$' should run route for index; no other routes in app
]
