from django.urls import path
from typing import List, Any

# from connector_street_api.users.views import (
#     user_detail_view,
#     user_redirect_view,
#     user_update_view,
# )

app_name = "users"
urlpatterns: List[Any] = [
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
