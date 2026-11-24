from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.db.models import Count,Sum,Avg,Max,Min
from .models import student
from .models import book
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import login_required


# Create your views here.
#---------------------------------------------------------------------------------------
#assessment :- 1
def myapp(request):
     return HttpResponse("BLUE") 

def student_detail(request,id):
     return HttpResponse(f"student id is {id}")

#---------------------------------------------------------------------------------------
#assessment :- 2
def student_report(request):
     st=student.objects.filter(age__gte=18) 
     ev =student.objects.filter(Q(age__gte=18) | Q(age__lt=26))
     ak =student.objects.filter(Q(age__gte=18) & Q(age__lt=26))
     return render(request,'student.html',{'students':st,'a':ev,'b':ak})  

def student_calculation(request):
     totals=student.objects.aggregate(Count('name'))
     sums=student.objects.aggregate(Sum('age'))
     avgs=student.objects.aggregate(Avg('age'))
     maxs=student.objects.aggregate(Max('age'))
     mins=student.objects.aggregate(Min('age'))
     return render(request,'calculation.html',{'cou':totals,'su':sums,'av':avgs,'mx':maxs,'mn':mins})

#---------------------------------------------------------------------------------------
# assessment :- 3
def book_detail(request):
     bok=book.objects.all()
     return render(request,'book.html',{'books':bok})

class book_list_view(ListView):
     model=book
     template_name="bo_ok.html"
     context_object_name="books"

class add_book (CreateView):     
     model=book
     fields=['name','title','price']
     template_name='add_book.html'
     success_url=reverse_lazy('book_list')

#---------------------------------------------------------------------------------------
#assessment :- 4
def home(request):
     return render(request,'home.html',{'name':'nelson'})   

def about(request):
     return render(request,'about.html')

def contact(request):
     return render(request,'contact.html')

def item_list (request):
     items=[        
            {"name": "Laptop", "price": 50000, "available": True},
            {"name": "Mobile", "price": 20000, "available": False},
            {"name": "Keyboard", "price": 1500, "available": True},
     ]
     return render(request,'items.html',{'items':items})

#---------------------------------------------------------------------------------------
#assessment :- 5

@login_required
def dashboard(request):
     return render(request,'dashboard.html')