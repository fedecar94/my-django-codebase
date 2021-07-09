"""config URL Configuration"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.authtoken.views import obtain_auth_token

from apps.testing.urls import router as testing_router


schema_view = get_schema_view(
    openapi.Info(
        title="Example API",
        default_version="v1",
        description="Test description",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path(
        "api/",
        include(
            [
                path("testing/", include(testing_router.urls)),
                path(
                    "token/",
                    include(
                        [
                            path("default/", obtain_auth_token, name="token_obtain_default"),
                            path("jwt/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
                            path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
                            path("verify/", TokenVerifyView.as_view(), name="token_verify"),
                        ]
                    ),
                ),
                path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
            ]
        ),
    ),
    path("admin/", admin.site.urls),
]
