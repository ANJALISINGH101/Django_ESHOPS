from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.category import Category
from django.views import View

print(make_password('1234'))
print(check_password('1235', 'pbkdf2_sha256$720000$u0BOGgUFYSBoDzdeAswEEQ$r4d1gF8wBPkNU7qhdJMaulsSjKciOCSOSqm68koNNgk='))

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove=request.POST.get('remove')

        print(product)
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product] = 1
        request.session['cart']=cart
        print('cart:',request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products = None

        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID);
        else:
            products = Product.get_all_products();
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('you are :', request.session.get('email'))

        # return render(request,'orders/orders.html')
        return render(request, 'index.html', data)
