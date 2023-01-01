from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
import requests
from blog.models import *
from django.core.paginator import Paginator

def sinkron_wilayah(request):
    
    URL = "https://api.goapi.id/v1/regional/provinsi?api_key=NCi8gCIlihiweY0d99LQAfGwA2Hr4V"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    for d in data['data']:
        cek_prov = ProvAPI.objects.filter(id_prov=d['id'])
        if cek_prov.exists():
            pro = cek_prov.first()
            pro.id_prov = d['id']
            pro.prov = d['name']
            pro.save()
        else:
            ProvAPI.objects.create(
                id_prov = d['id'],
                prov = d['name']        

            )
    ambil_reg = ProvAPI.objects.all()
    
   
    for j in ambil_reg:
        url_kota = "https://api.goapi.id/v1/regional/kota?provinsi_id={}&api_key=NCi8gCIlihiweY0d99LQAfGwA2Hr4V".format(j.id_prov)
    
        r = requests.get(url = url_kota) 
        
        data = r.json()
        
        for i in data['data']:  
            cek_kab = KotaAPI.objects.filter(id_kota=i['id'])
            if cek_kab.exists():     
                kot = cek_kab.first()         
                kot.id_kota = i['id']
                kot.kota = i['name']
                kot.save()
            else:
                KotaAPI.objects.create(
                id_kota = i['id'],
                kota = i['name']        

            )
                       
    return HttpResponse("<h1>berhasil sinkron API Wilayah</h1>")

def home(request):
    
    template_name = "front/home.html"
    
    URL = "https://api.quotable.io/random"
    
    r = requests.get(url = URL)
    
    data = r.json()
     
    prov = ProvAPI.objects.all()
    
    context ={
        "data" : prov,
        "author" : data['author'],
        "content" : data['content'],
        "tags" : data['tags'],

    }
    
    return render(request, template_name, context)

def aboutus(request):
    
    template_name = "front/aboutus.html"
   
    prov = ProvAPI.objects.all()
    
    context= {
        "data" : prov
    }
    
    return render(request, template_name, context)

def presiden(request):
    
    template_name = "front/presiden.html"
    
    prov = ProvAPI.objects.all()
    
    context= {
        "data" : prov
    }
    
    return render(request, template_name, context)

def blog(request):
    
    template_name = "front/blog.html"
    
  
    
    art = Artikels.objects.all()
    prov = ProvAPI.objects.all()
    
    p = Paginator(Artikels.objects.all(), 3)
    page = request.GET.get('page')
    artis =p.get_page(page)
    nums = "a" * artis.paginator.num_pages
    
    context ={
       
        "data" : prov,
        "art" : art,
        "artis" : artis,
        "nums" : nums
    }
    
    return render(request, template_name, context)

def detailBlog(request, id):
    
    template_name = "front/detail.html"
    
    take = Artikels.objects.get(id=id)
    
    prov = ProvAPI.objects.all()
    
    context = {
        "data" : prov,
        "take" : take,

    }
    
    return render(request, template_name, context)

def provinsi(request):
    
    template_name = "front/provinsi.html"
    
    get_id = request.POST.get('provinsi')
    
    prov = ProvAPI.objects.all()
    
    kota = KotaAPI.objects.filter(id_kota__startswith=get_id)
    
    context ={
       
        "data" : prov,
        "data2" : kota
    }
    
    return render(request, template_name, context)

def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    template_name = "front/home.html"
    
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            print("kamu gagal")
            
    return render(request, template_name)


    