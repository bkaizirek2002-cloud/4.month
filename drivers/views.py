from django.shortcuts import render, get_object_or_404, redirect
from .models import DriverModel
from .forms import DriverForm

def driver_list(req):
    drivers = DriverModel.objects.all()
    return render(req, 'driver_list.html', {'drivers': drivers})

def driver_create(req):
    if req.method == 'POST':
        form = DriverForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('driver_list')

    else:
        form = DriverForm()

    return render(req, 'driver_list.html', {'form': form})


def driver_update(request, pk):
    driver = get_object_or_404(DriverModel, pk=pk)
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm(instance=driver) 
    return render(request, 'driver_form.html', {'form': form})

def driver_delete(request, pk):
    driver = get_object_or_404(DriverModel, pk=pk)
    driver.delete()
    return redirect('driver_list')
          

