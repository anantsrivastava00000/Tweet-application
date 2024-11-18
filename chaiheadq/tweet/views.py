from django.shortcuts import render, HttpResponse
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request, 'tweet/index.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet/tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form=TweetForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm()
    return render(request, 'tweet/tweet_form.html', {'form':form})

@login_required
def tweet_edit(request, tweet_pk):
    id=tweet_pk
    tweet=get_object_or_404(Tweet, id=id, user=request.user)
    if request.method == 'POST':
        form=TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm(instance=tweet)
    return render(request, 'tweet/tweet_form.html', {'form': form })

@login_required
def tweet_delete(request, tweet_pk):
    id=tweet_pk
    tweet = get_object_or_404(Tweet, id=id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    # return render(request, 'tweet/tweet_confirm_delete.html', {'tweet': tweet})
    return render(request, 'tweet/tweet_confirm_delete.html')
    

def search(request):
    print(request.GET,'[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]')
    text = request.GET.get('query')
    tweets=Tweet.objects.filter(text__icontains=text)
     

    return render(request, 'tweet/search.html', {'tweets':tweets})
    # return HttpResponse('This is search')
 

def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.set_password(form.cleaned_data['password1'])
           user.save()
           login(request, user)
           return redirect('tweet_list')
    
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})