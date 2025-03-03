from django.shortcuts import render,redirect
from App.models import Book1
from datetime import datetime
# Create your views here.



def base(request):
      return render(request,'base.html')

def Homepage(request):
      books=Book1.objects.all()
      allbooks={'books':books}
      return render(request,'homepage.html',allbooks)

def Addbook(request):
      if request.method=='POST':
            title=request.POST['title']
            author=request.POST['author']
            genre=request.POST['genre']
            price=request.POST['price']
            published_date=request.POST['publish_date']
            description=request.POST['description']

            Book1.objects.create(title=title,author=author,genre=genre,price=price,published_date=published_date,description=description)
      return render(request,'addbook.html')




def Edit(request,id):
      a=Book1.objects.get(id=id)
      if request.method=='POST':
            a.title=request.POST['title']
            a.author=request.POST['author']
            a.genre=request.POST['genre']
            a.price=request.POST['price']
            a.published_date=request.POST['publish_date']
            a.description=request.POST['description']
            a.save()
            return redirect('viewdetails',id=a.id)
      
      if a.published_date:
            a.published_date=a.published_date.strftime('%Y-%m-%d')
      b={'a':a}
      return render(request,'edit.html',b)



def Delete(request,id):
      a=Book1.objects.get(id=id)
      a.delete()
      return redirect('homepage')
      

def viewdetails(request,id):
      a=Book1.objects.get(id=id)
      return render(request,'viewdetails.html',{'a':a})
      

def search(request):
      query=request.GET.get('q','')
      Book1.objects.all()
      if query:
            books=Book1.objects.filter(title__icontains=query) | Book1.objects.filter(author__icontains=query) | Book1.objects.filter(genre__icontains=query) | Book1.objects.filter(price__icontains=query) | Book1.objects.filter(published_date__icontains=query) | Book1.objects.filter(description__icontains=query)     
      else:
            books=Book1.objects.all()

      allbooks={'books':books}
      return render(request,'search.html',allbooks)