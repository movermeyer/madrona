from django.conf.urls import *
from views import get_json, demo

urlpatterns = patterns('madrona.layer_manager.views',
    (r'^layers.json$', get_json),
    (r'^demo', demo)
)
