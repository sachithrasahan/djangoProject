from django.shortcuts import render
from django.http import HttpResponse
from TestProfileApp.models import UserProfile
# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'user_profile.html')

def addUser(request):
    firstName = request.POST.get('FirstName')
    lastName = request.POST.get('LastName')
    if firstName and lastName:
        user = UserProfile()
        user.FirstName = firstName
        user.LastName = lastName
        user.save()
        return render(request, 'user_profile.html')

    return render(request, 'user_profile.html')

def getUserList(request):
    return render(request, 'user_list.html', {'userList' : UserProfile.objects.all()})

