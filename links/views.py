from django.shortcuts import render

def home(request):

    
    context = {
        'home':'active',
    }
    
    return render(request, 'links/index.html', context )
