

import abc
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product_view,Signup,vprofile,oContact
from django.db.models import Q
# Create your views here.

def proview(request,abc):
    # a=product.objects.all()
    if 'xyz' in request.session.keys():
        pv=Product_view.objects.get(id=abc)
        return render(request,'proview.html',{'pv':pv})
    else:
        return redirect('loginview')
def prodelete(request,abc):
    # a=product.objects.all()
    if 'xyz' in request.session.keys():
        pall=Product_view.objects.get(id=abc)
        pall.delete()
        return redirect('contact')
    else:
        return redirect('loginview')
# def productall(request):
#     b=Product_view.objects.all()
#     return render(request,'productall.html',{'pall':b})
def contact(request):
    if 'xyz' in request.session.keys():
        up=Signup.objects.get(id=int(request.session['xyz']))
        print(up)
        pd=Product_view.objects.filter(up=up)
        print(pd)
        return render(request,'contact.html',{'pVIEW':pd,'USER':up})
    else:
        return redirect('loginview')
def Signupform(request):
    if request.method=='POST':
        model=Signup()
        model.name=request.POST['name']
        model.email=request.POST['email']
        model.mobile_no=request.POST['number']
        model.password=request.POST['password']
        model.image=request.FILES.get('image')
        model.address=request.POST['address']
        model.bussiness_type=request.POST['bussiness_type']
        model.save()
        return redirect('loginview')
    return render(request,'Signup.html')
def vanderprofile(request):
    if request.method=='POST':
        model=vprofile()
        model.name=request.POST['name']
        model.bussiness_type=request.POST['bname']
        model.m_no=request.POST['m_no']
        model.address=request.POST['address']
        model.image=request.FILES.get('image')
        model.email=request.POST['email']
        model.save()
    return render(request,'vprofile.html')
def add_product(request):
    if 'xyz' in request.session.keys():
        up=Signup.objects.get(id=  int(request.session['xyz']))
        if request.POST:
            name=request.POST['productname']
            image=request.FILES.get('image')
            dec=request.POST['dec']
            price=request.POST['price']
            rating=request.POST['rating']
            
            var=Product_view()
            var.up=up
            var.name=name
            var.image=image
            var.dec=dec
            var.price=price
            var.rating=rating
            var.save()
            return redirect('contact')
        return render(request,'add_product.html',{'USER':up})    
    else:
        return redirect('loginview')

def home(request):
    # if 'xyz' in request.session.keys():
    #     l=home.objects.all()
    # if 'xyz' in request.session.keys():
    #     up=Signup.objects.get(id = int(request.session['xyz']))
        q=request.GET.get('search')
        if q:
            pr=Product_view.objects.filter(Q(name__icontains= q) | Q(dec__icontains= q) | Q(price__icontains= q))
            data={'s':pr}
        else:
            data={}
        if 'xyz' in request.session.keys():
            return render(request,'home.html',data)
        else:
            return redirect('loginview')
    # else:
        # return redirect('loginview')
def loginview(request):
    if request.method=='POST':
        try:
            m=Signup.objects.get(name=request.POST['name'])
            if m.email==request.POST['email']: 
                request.session['xyz']=m.id
                # request.session['xyz']=m.id 
                return redirect('home')
            else:
                return HttpResponse("wrong email")
        except:
            return HttpResponse("wrong username")
    return render(request,'index.html')
def Searchview(request):
    q=request.GET.get('search')
    if q:
        pr=Product_view.objects.filter(Q(name__icontains= q) | Q(dec__icontains= q) | Q(price__icontains= q))
        data={'s':pr}
    else:
        data={}
    return render(request,'search.html',data)
def logout (request):
    if 'xyz' in request.session.keys():
        del request.session['xyz']
        return redirect('loginview')
    else:
        return redirect('loginview')
def vprofileview(request):
    # vp=vprofile.objects.all()
    # return render(request,'vcp.html',{'vp':vp})
    if 'xyz' in request.session.keys():
        up=Signup.objects.get(id = int(request.session['xyz']))

        if request.POST:
            im=request.FILES.get('image')
            vnm=request.POST['name']
            bn=request.POST['bussiness_type']
            em=request.POST['email']
            mn=request.POST['mobile_no']
            add=request.POST['address']
             

            up.name=vnm
            up.bussiness_type=bn
            up.email=em
            up.mobile_no=mn
            up.address=add
            print(im)
            if im != None:
                up.prifile =im 
            up.save()
        return render(request,'vcp.html',{'USER':up})
    else:
        return redirect('loginview')

def service(request):
    return render(request,'service.html')
def owContact(request):
    if'xyz' in request.session.keys():
        up=Signup.objects.get(id=int(request.session['xyz']))
        if request.POST:
            var=oContact()
            var.up=up
            var.name=request.POST['name']
            var.number=request.POST['number']
            var.bussiness_type=request.POST['bussiness']
            var.problem=request.POST['problem']
            var.save()
            return redirect('home')
    return render(request,'owenerContact.html',{'USER':up})
   
       