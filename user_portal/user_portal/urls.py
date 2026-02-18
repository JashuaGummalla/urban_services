# from django.contrib import admin
# from django.urls import path
# from accounts.views import (
# #     register, login_view, dashboard, purchase_product,
# #     product_edit, product_delete,email_sender, 
# #     send_otp_view, verify_otp_view
#       RegisterView
# )

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     # path('register/', register, name='register'),
# #     # path('login/', login_view, name='login'),
# #     # path('dashboard/', dashboard, name='dashboard'),
# #     # path('purchase/<int:product_id>/', purchase_product, name='purchase_product'),
# #     # path('product/edit/<int:pk>/', product_edit, name='product_edit'),      
# #     # path('product/delete/<int:pk>/', product_delete, name='product_delete'),
# #     # path('email/',email_sender,name='email'),
# #     # path('send_otp/',send_otp_view,name='send_otp'),
# #     # path('verify_otp',verify_otp_view,name='verify_otp'),
# #     urlpatterns = [
# #     path('register/', RegisterView.as_view(), name='register'),
# # ]
# # ]
# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='register'),
# ]
from django.urls import path
from accounts.views import RegisterView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('register/', RegisterView.as_view(), name='register'),
]
