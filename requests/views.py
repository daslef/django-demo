from django.shortcuts import render
from . import models, forms

def requests_list(request):
    if request.user.groups.filter(name='Moderators'):
        requests = models.Request.objects.all()
    else:
        requests = models.Request.objects.filter(contact__id=request.user.contact.id).all()
    return render(
        request, 
        'requests_list.html', 
        { "requests": requests }
    )

def create_request(request):
    if request.method == "POST":
        form = forms.RequestForm(request.POST)
        if form.is_valid:
            form.save(commit=False)
            # form.contact_id = models.Contact.objects.get(user__id=request.user.id)
            form.contact_id = 1
            form.save()
    else:
        form = forms.RequestForm()
    return render(request, 'new_request.html', { "form": form })