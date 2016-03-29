from django.conf.urls import url
from test_balance.api.test_balance import GetDataTestBalance, PostDataTestBalance

urlpatterns = [    
    url(r'^get/$', GetDataTestBalance.as_view(), name='test-balance-get'),
    url(r'^post/$', PostDataTestBalance.as_view(), name='test-balance-post'),
]
