from django.urls import path, include

# router = routers.SimpleRouter()
# router.register(r'create-view', EmployeeView)
# router.register(r'update-delete/<int:pk>', EmployeeUpdate)
# urlpatterns = router.urls
from webapp.views import staffView
from webapp.views.staffView import StaffCreateView

urlpatterns = [
    # path(r'staffCreate/', StaffCreateView.as_view()),
    # path(r'staffUpdate/<int:pk>', staffView.StaffUpdate.as_view()),
    # path('', include(router.urls)),

]
