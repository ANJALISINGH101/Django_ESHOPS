from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')

    def post(self,request):
        postData = request.POST
        frist_name = postData.get('fristname')
        last_name = postData.get('lastname')
        phone = postData.get('phonenumber')
        email = postData.get('email')
        password = postData.get('password')
        # validations
        value = {
            'frist_name': frist_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None
        customer = Customer(frist_name=frist_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        # save
        if not error_message:
            print(frist_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self,customer):
        error_message = None
        if (not customer.frist_name):
            error_message = "Frist Name Required !!"
        elif len(customer.frist_name) < 4:
            error_message = "Frist Name must be 4 char long or more"
        elif not customer.last_name:
            error_message = "LAST Name Required"

        elif len(customer.last_name) < 4:
            error_message = "last Name must be 4 char long or more"
        elif not customer.phone:
            error_message = "phone number required"
        elif len(customer.phone) < 10:
            error_message = "phonre number must be 10 char"
        elif len(customer.password) < 6:
            error_message = "password must be 6 char"
        elif len(customer.email) < 5:
            error_message = "email must be 5 char"

        elif customer.isExists():
            error_message = 'Email Address Alerady Registered'

        return error_message


