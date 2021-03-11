from django.urls import path


from .views.languages import RetrieveLanguages

app_name = "api"

urlpatterns = [
    path("languages", RetrieveLanguages.as_view(), name="all_languages"),
    path(
        "languages/<uuid:uuid>",
        RetrieveLanguages.as_view(),
        name="all_languages"
    ),
]
