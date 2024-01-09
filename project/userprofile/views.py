from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.


def userprofile(request):
    if request.method == "POST":
        form = UserprofileForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('profile')
    else:
        userprofile = Userprofile.objects.filter(user=request.user).first()

        if userprofile:
            form = UserprofileForm(instance=userprofile)
        else:
            form = UserprofileForm()

    context = {
        'form': form,
        'userprofile': userprofile

    }
    return render(request, 'profile.html', context)
