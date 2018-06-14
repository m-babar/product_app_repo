import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from .models import Product, PlaceOrder


def index(request):
    """
    welcome page of the application.
    """
    return render(request, 'product/index.html')


def get_product_records(request):
    """
    It's ajax request. it will return all project records with json format.
    """
    products = Product.objects.all()

    products_info = []

    # prepage the json response.
    for product in products:
        products_info.append({
            'id': product.id, 
            'symbol': product.symbol, 
            'description': product.description, 
            'unit': product.unit,
        })

    res = {'products_info': products_info, 'status': 201,'message': 'all products record'}
    return HttpResponse(json.dumps(res), content_type='application/json')


@login_required(login_url='/raise/exception')
@csrf_exempt
def update_product_quantity(request):
    """
    It's ajax request, accepted post method.
    it's update product quntity for place order.
    """
    if request.method == 'POST':

        product_id = request.POST.get('id')
        quantity = request.POST.get('quantity')

        try:
            product = Product.objects.get(id=product_id)    
        except Product.DoesNotExist as e:
            product = None

        if product:
            # create a product place order.
            place_order = PlaceOrder.objects.get_or_create(
                                product_order_by=request.user,
                                product=product,
                                quantity=quantity
                            )
            data = {'status': 201,'message': 'Your order has been placed.'}
            return HttpResponse(json.dumps(data), content_type='application/json')

        data = {'status': 400,'message': 'Product related Id not found.'}
        return HttpResponse(json.dumps(data), content_type='application/json')


@login_required
def place_order(request):
    """
    It's place order index page. it's show all product place order of the user.
    """
    return render(request, 'product/place_order.html')


@login_required
def get_place_order(request):
    """
    It's ajax request to return all the user related product place order.
    """
    placed_orders = PlaceOrder.objects.filter(product_order_by=request.user)

    placed_order_records = []
    # prepare json response of the product.
    for order in placed_orders:
        placed_order_records.append({
            'id': order.id, 
            'symbol': order.product.symbol, 
            'description': order.product.description, 
            'unit': order.product.unit,
            'created_date' : order.created_date.strftime('%Y-%m-%d'),
            'quantity' : order.quantity
        })

    data = {'orders': placed_order_records, 'status': 200, 'message': 'Placed order records.'}
    return HttpResponse(json.dumps(data), content_type='application/json')


def get_search_product(request):
    """
    This view return all the query related search response from the database.
    """
    query = request.GET.get('q')

    products = Product.objects.filter(Q(symbol__icontains=query) | Q(description__icontains=query))

    products_info = []
    print("######################", products)
    for product in products:
        products_info.append({
            'id': product.id, 
            'symbol': product.symbol, 
            'description': product.description, 
            'unit': product.unit,
        })

    res = {'products_info': products_info, 'status': 201, 'message': 'search products record'}
    return HttpResponse(json.dumps(res), content_type='application/json')

