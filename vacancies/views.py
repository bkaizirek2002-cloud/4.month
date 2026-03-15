from django.shortcuts import render, redirect
from .forms import ITSpecialistForm

def register_view(request):
    if request.method == 'POST':
        form = ITSpecialistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')
        else:
            form = ITSpecialistForm()
             
    return render(request, 'vacancies/register.html', {'form: form'})
