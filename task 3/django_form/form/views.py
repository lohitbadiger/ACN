from django.shortcuts import render,redirect

# Create your views here.

# importing the data from the models


from .models import InfoStore

# importing the form by its class name 

from .forms import AllInfoForm

# index function is the first page 
def index(request):
    all_info=InfoStore.objects.all().order_by('-name')
    
    context={
       'all_info':all_info 
    }
    return render(request,'all_info.html',context)

# creating the new form 

def create_form(request):
    # check if form has all the valid input before creating the form.
    # if valid redirect to Index function
    # else stay in the  add_form.html
    
    form=AllInfoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(index)
    return render(request, 'add_form.html',{'form':form})


# check if form has all the valid input before updaing the form.
    # if valid redirect to Index function
    # else stay in the  add_form.html
    # instance => we are updating the 1 particular form so get it by its id.

def update_info(request, id):
    all_info=InfoStore.objects.get(id=id)
    form=AllInfoForm(request.POST or None, instance=all_info)
    if form.is_valid():
        form.save()
        return redirect(index)

    return render(request,'add_form.html', {'form':form, 'all_info':all_info})


# delete function same as crate function but here we have    delete_info.delete()
# to delete
def delete_info(request,id):
    delete_info=InfoStore.objects.get(id=id)
    
    if request.method=='POST':
        delete_info.delete()
        return redirect(index)
    
    return render(request, 'info-delete.html', {'delete_info':delete_info})