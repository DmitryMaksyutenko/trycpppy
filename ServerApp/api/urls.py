from django.urls import path

from .views.languages import (
    LanguagesView, LanguageView
)
from .views.categories import (
    CategoriesView, CategoryView
)
from .views.articles import (
    ArticleView, ArticlesView
)

app_name = "api"

urlpatterns = [
    path("languages", LanguagesView.as_view(), name="languages"),
    path("languages/<uuid:uuid>", LanguageView.as_view(), name="language"),
    path("categories", CategoriesView.as_view(), name="categories"),
    path("categories/<uuid:uuid>", CategoryView.as_view(), name="category"),
    path("articles", ArticlesView.as_view(), name="articles"),
    path("articles/<uuid:uuid>", ArticleView.as_view(), name="article"),
]
