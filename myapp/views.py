from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import Category,Student
from myapp.forms import StudentAddForm

# Create your views here.



class StudentListView(View):
    def get(self, request, *args, **kwargs):
        
        qs=Student.objects.all()
        cator=Category.objects.all()
        cat=request.GET.get("category")
        print(cat)
        if cat:
            qs=qs.filter(category_obj__category_name=cat)
        
        return render(request,"student_list.html",{"data":qs,"cat":cator})
    
class StudentCreateView(View):
    def get(self, request, *args,**kwargs):
        
        form = StudentAddForm()
        return render(request,"student_create.html",{"form":form})
        
        
    def post(self, request, *args, **kwargs):
        
        form = StudentAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student-list")
        return render(request,"student_create.html",{"form":form})
    
    
class StudentDetailView(View):
    
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=Student.objects.get(id=id)
        return render(request,"student_detail.html",{"form":qs})

  
class StudentUpdateView(View):
    def get(self, request, *args,**kwargs):
        id=kwargs.get("pk")
        qs=Student.objects.get(id=id)
        form=StudentAddForm(instance=qs)
        return render(request,"student_update.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Student.objects.get(id=id)
        form=StudentAddForm(request.POST, instance=qs)
        if form.is_valid():
            form.save()
            return redirect("student-list")
        return render(request,"student_update.html",{"form":form})

class StudentDeleteView(View):
    def get(self, request, *args,**kwargs):
        id=kwargs.get("pk")
        qs=Student.objects.get(id=id).delete()
        return redirect("student-list")       


        
        
