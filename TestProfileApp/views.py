from django.shortcuts import render
from django.http import HttpResponse
from TestProfileApp.models import UserProfile
from TestProfileApp.forms import UserProfileForm
# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'user_profile.html')

def addUser(request):
    firstName = request.POST.get('FirstName')
    lastName = request.POST.get('LastName')
    if firstName and lastName:
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'user_profile.html')
        else:
            return HttpResponse("Form is not valid.")
    else:
        return HttpResponse("Fields are empty.")

def getUserList(request):
    return render(request, 'user_list.html', {'userList' : UserProfile.objects.all()})

