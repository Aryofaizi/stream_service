"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib.sitemaps.views import sitemap
from content.v2.sitemaps import ContentSitemap
from content.v2.views import search_content

#sitemaps configuration
sitemaps = {
    "content": ContentSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path("", include("content.urls")),
    path("carts/", include("cart.urls")),
    path("orders/", include("order.urls")),
    path("subscriptionplans/", include("subscription.urls")),
    path("payment/", include("payment.urls")),
    path("core/", include("core.urls")),
    path("sitemap.xml", sitemap, {"sitemaps":sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("search/", view=search_content, name="search_content"),
] + debug_toolbar_urls()
