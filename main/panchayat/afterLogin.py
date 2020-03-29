from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Profile, Post, Comment, Follower, Following
from .forms import profileForm, postForm

@login_required
def home(request):
    currentUser = Profile.objects.get(user=request.user)
    return render(request, 'home.html', {"userdata": currentUser})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def showFollowers(request):
    current_user = Profile.objects.get(user=request.user)
    followers = Follower.objects.filter(user=current_user)
    return render(request, 'followers.html', {"current_user": current_user, "users": followers})      

@login_required
def showFollowing(request):
    current_user = Profile.objects.get(user=request.user)
    followings = Following.objects.filter(user=current_user)
    return render(request, 'following.html', {"current_user": current_user, "users": followings})

@login_required
def showAllUsers(request):
    current_user = Profile.objects.get(user=request.user)
    users = Profile.objects.all()
    return render(request, 'allUsers.html', {"current_user": current_user, "users": users})

@login_required
def followPerson(request):
    current_user = Profile.objects.get(user=request.user)
    new_follow = Profile.objects.get(user=request.POST['person_id'])
    
    followings = Following.objects.filter(user=current_user)

    for following in followings:
        if (new_follow.user.id == following.following.user.id):
            redirect_to = '/profile?person_id=' + str(new_follow.user.id)
            return redirect(redirect_to)

    following = Following(user=current_user, following=new_follow)
    following.save()

    follower = Follower(user=new_follow, follower=current_user)
    follower.save()

    redirect_to = '/profile?person_id=' + str(new_follow.user.id)
    return redirect(redirect_to)

@login_required
def unfollowPerson(request):
    current_user = Profile.objects.get(user=request.user)
    unfollow = Profile.objects.get(user=request.POST['person_id'])

    following = Following.objects.filter(user=current_user).filter(following=unfollow)
    following.delete()

    follower = Follower.objects.filter(user=unfollow).filter(follower=current_user)
    follower.delete()

    redirect_to = '/profile?person_id=' + str(unfollow.user.id)
    return redirect(redirect_to)

@login_required
def profile(request):
    current_user = Profile.objects.get(user=request.user)
    
    viewing_profile = User.objects.get(pk=request.GET['person_id'])
    viewing_profile = Profile.objects.get(user=viewing_profile)

    posts=Post.objects.filter(user=viewing_profile)
    followings = Following.objects.filter(user=current_user)

    isFollowed = False

    for following in followings:
        if viewing_profile == following.following:
            isFollowed = True

    return render(request, 'profile.html', {"isFollowed": isFollowed, "posts": posts, "viewing_profile": viewing_profile, "current_user": current_user})
    
@login_required
def newPost(request):
    current_user = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(user=current_user, text=request.POST['text'], image=request.FILES['image'])
            post.save()
            return redirect('/feed')

    form = postForm()
    return render(request, 'createPost.html', {"current_user":current_user, "form":form})

@login_required
def feed(request):
    current_user = Profile.objects.get(user=request.user)
    followings = Following.objects.filter(user=current_user)
    posts=Post.objects.none()

    for following in followings:
        posts = posts | Post.objects.filter(user=following.following)

    # post_ids=[]

    # for post in posts:
    #    post_ids.append(post.id)
    
    # post_ids.sort(reverse=True)
    # post_ids.sort()
    # posts=Post.objects.none()

    # for post_id in post_ids:
    #    posts = posts | Post.objects.filter(id=post_id)

    return render(request, 'feed.html', {"current_user": current_user, "posts": posts})

@login_required
def editProfile(request):
    form = profileForm()
    return render(request, 'editProfile.html', {"form":form})