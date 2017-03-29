from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .forms import TwitterForm
from django.http import HttpResponseRedirect,HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
def index(request):
    return render(request, 'twitter/index.html')


@login_required
def myadmin(request):
    return render(request, 'twitter/myadmin.html')


@login_required
def redilect(request):
    return render(request, 'twitter/redilect.html')


# def timeline(request):
#     tweets = Tweet.objects.all()
#     return render(request,'twitter/timeline.html',{'tweets':tweets})


def timeline(request):
    if request.method == 'POST':

        # create a form instance and populate it with data" from the request:
        form = TwitterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            t = Tweet(user_id=request.user.id,text=form.cleaned_data['text'], tweet_date=timezone.now())
            t.save()
            return HttpResponseRedirect('/timeline')
    # elif request.method =='DELETE':
    #     d = Tweet.objects.get(id=request.DELETE['delete'])
    #     d.delete()
    #     return HttpResponseRedirect('/timeline')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TwitterForm()
    tweets = Tweet.objects.all()
    return render(request,'twitter/timeline.html',{'tweets':tweets,'form': form})

def delete(request):
    if request.method =="POST":
        tweet_id = request.POST["delete"]
        d = Tweet.objects.get(id=tweet_id)
        d.delete()
        return HttpResponseRedirect('/timeline')
