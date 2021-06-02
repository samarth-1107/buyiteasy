from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    allProds=[]
    catProds=Product.objects.values('category','id')
    cats={item['category'] for item in catProds }
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n=len(prod)
        nSlides= n//4+ ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides),nSlides])
    params={'allProds':allProds}         
    return render(request, 'shop/index.html',params)

def searchMatch(query,item):
    #Return True if query==item
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.subcategory.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Your search query didn't match with any of our items."}
    return render(request, 'shop/search.html', params)   

def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    thank=False
    if request.method == 'POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank=True
    return render(request, 'shop/contact.html',{'thank':thank})



def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')



def products(request,myid):
    #Fetch Product Using the ID
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/products.html', {'product':product[0]})

def checkout(request):
    if request.method == 'POST':
        items_json=request.POST.get('items_json','')
        name=request.POST.get('name','')
        the_amount=request.POST.get('the_amount','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','')+" "+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        country=request.POST.get('country','')
        phone=request.POST.get('phone','')
        zip_code=request.POST.get('zip_code','')
        order=Orders(items_json=items_json, name=name, email=email,address=address,city=city,state=state,country=country,zip_code=zip_code, phone=phone,the_amount=the_amount)
        order.save()
        update=OrderUpdate(order_id=order.order_id, update_desc="The order has been placed!!")
        update.save()
        thank=True
        id = order.order_id
        return render(request, 'shop/checkout.html',{'thank':thank, 'id':id})
        #Request Paytm to transfer amnt to your acc. after payment by user.
    return render(request, 'shop/checkout.html')

#Paytm will send POST req. here
@csrf_exempt
def handlerequest(request):
        pass
