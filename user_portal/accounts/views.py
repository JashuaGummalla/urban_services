# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from .forms import RegistrationForm, LoginForm, ProductForm
# from .models import User, Product
# from django.core.mail import send_mail

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.password = form.cleaned_data['password']
#             user.save()
#             messages.success(request, "Registration successful. Please log in.")
#             return redirect('login')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = RegistrationForm()
#     return render(request, 'accounts/register.html', {'form': form})

# def login_view(request):
#     error_message = None
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             role = form.cleaned_data['role']
#             try:
#                 user = User.objects.get(name=name, email=email, password=password, role=role)
#                 request.session['user_name'] = user.name
#                 request.session['user_email'] = user.email
#                 request.session['user_role'] = user.role
#                 messages.success(request, f"Welcome {user.name}!")
#                 return redirect('dashboard')
#             except User.DoesNotExist:
#                 messages.error(request, "Invalid credentials or role.")
#     else:
#         form = LoginForm()
#     return render(request, 'accounts/login.html', {'form': form, 'error_message': error_message})

# def dashboard(request):
#     name = request.session.get('user_name')
#     email = request.session.get('user_email')
#     role = request.session.get('user_role')
#     if not name or not email or not role:
#         messages.warning(request, "Please log in first.")
#         return redirect('login')

#     if role == 'admin':
#         return admin_dashboard(request)
#     else:
#         return user_dashboard(request)

# def admin_dashboard(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Product added successfully.")
#             return redirect('dashboard')
#     else:
#         form = ProductForm()
#     products = Product.objects.all()
#     return render(request, 'accounts/admin_dashboard.html', {
#         'form': form,
#         'products': products,
#         'name': request.session['user_name'],
#         'email': request.session['user_email']
#     })

# def user_dashboard(request):
#     products = Product.objects.all()
#     return render(request, 'accounts/user_dashboard.html', {
#         'products': products,
#         'name': request.session['user_name'],
#         'email': request.session['user_email']
#     })

# def purchase_product(request, product_id):
#     if request.method == "POST":
#         print("POST data:", request.POST)  
#         quantity_raw = request.POST.get('quantity', '0')
#         print("Raw quantity value:", quantity_raw)
#         try:
#             quantity = int(quantity_raw)
#         except ValueError:
#             quantity = 0
#         product = get_object_or_404(Product, pk=product_id)
#         if quantity < 1 or quantity > product.quantity:
#             messages.error(request, "Please enter a valid quantity between 1 and available stock.")
#         else:
#             product.quantity -= quantity
#             product.save()
#             messages.success(request, "Purchase successful!")
#         return redirect('dashboard')


# def product_delete(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     product.delete()
#     messages.success(request, "Product deleted successfully!")
#     return redirect('dashboard')

# def product_edit(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == "POST":
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Product updated successfully!")
#             return redirect('dashboard')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'accounts/product_edit.html', {'form': form, 'product': product})


# from django.core.mail import send_mail
# from django.shortcuts import render

# def email_sender(request):
#     success = None
#     error = None
#     to_email = None
#     if request.method == "POST":
#         to_email = request.POST.get('to_email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         try:
#             send_mail(
#                 subject,
#                 message,
#                 None,  # uses DEFAULT_FROM_EMAIL from settings
#                 [to_email],
#                 fail_silently=False,
#             )
#             success = "Email sent successfully!"
#         except Exception as e:
#             error = f"Failed to send email: {str(e)}"

#     return render(request, 'accounts/email.html', {'success': success, 'error': error, 'to_email': to_email})


# from django.core.mail import EmailMessage
# from django.shortcuts import render,redirect
# import random
# def send_otp_view(request):
#     if request.method == "POST":
#         receiver = request.POST.get('receiver')
#         otp = str(random.randint(100000,999999))
#         subject = "your otp verification code"
#         message = f"dear user , \n\n your one time password(OTP) is {otp} \n\n use this code to verify your email.\n\n thank you"
#         email = EmailMessage(
#             subject,
#             message,
#             "gummallajashua@gmail.com",
#             [receiver],
#         )
#         email.send(fail_silently=False)
#         request.session["otp"] = otp
#         request.session["receiver"] = receiver
#         return render(request,"accounts/verify_otp.html",{"receiver": receiver})
#     return render(request,"accounts/send_otp.html")


# def verify_otp_view(request):
#     if request.method == 'POST':
#         otp_entered = request.POST.get("otp_entered")
#         otp_stored = request.session.get("otp")
#         receiver = request.session.get("receiver")

#         if otp_entered == otp_stored:
#             message = "OTP verified Successfully!"
#             # Clear OTP session after successful verification
#             request.session.pop("otp", None)
#             request.session.pop("receiver", None)
#             return render(request, "accounts/otp_result.html", {"message": message, "receiver": receiver})
#         else:
#             message = "Invalid OTP Please Try Again!"
#             # Clear OTP session on failure as well
#             request.session.pop("otp", None)
#             return render(request, "accounts/otp_result.html", {"message": message, "receiver": receiver})

#     # For GET request or others, redirect to send_otp page
#     return redirect("send_otp")


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import RegisterSerializer
from .models import User

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]  # Allow any user to access registration

    # POST method for registering a new user
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Registration successful!",
                "data": serializer.data  # Return saved user data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET method to view all registered users
    def get(self, request):
        users = User.objects.all()
        serializer = RegisterSerializer(users, many=True)  # Serialize list of users
        return Response(serializer.data, status=status.HTTP_200_OK)
