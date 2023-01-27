# this is required 
    # #request.body
    # # request -> HttpRequest -> Django
    # print(request.GET)#url query params
    # body =request.body #byte string of JSON data
    # data = {}
    # try:
    #     data = json.loads(body) # string of JSOn data -> Python dictionary
    # except:
    #     pass    
    # print(data)
    # data['params'] =dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    #  return JsonResponse(data)
    # return JsonResponse({"message": "Hi there!, this is your Django API Response!"})
import json
# from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    # DRF Api view
    model_data = Product.objects.all().order_by("?").first()
    data ={}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title", "price"])
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        #serialization
        #model instance (model_data)
        #turn python dict
        #return JSON to my client
    return Response(data)
