"""
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
        path("api/", include("api.urls")),
    path("", include("bank_account.urls")),
    path("admin/", admin.site.urls),
]
