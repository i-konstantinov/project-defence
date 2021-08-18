from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from OnlineCookbook.accounts.forms import LoginForm, RegisterForm, ProfileForm
from OnlineCookbook.accounts.models import Profile
from OnlineCookbook.common.models import Like
from OnlineCookbook.recipes.models import Recipe


def list_profiles(request):
    profiles = Profile.objects.all()

    context = {
        'profiles': profiles,
    }
    return render(request, 'accounts/list-profiles.html', context)


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/log-in.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)


@login_required()
def log_out(request):
    logout(request)
    return redirect('index')


def view_profile(request, pk):
    profile = Profile.objects.get(pk=pk)

    profile_owner = request.user == profile.user

    recipes_added_by_user = Recipe.objects.filter(user_id=profile.user.id)

    recipes_liked_by_user = [obj.recipe for obj in Like.objects.filter(user_id=profile.user.id)]

    context = {
        'profile': profile,
        'profile_owner': profile_owner,
        'recipes_added_by_user': recipes_added_by_user,
        'recipes_liked_by_user': recipes_liked_by_user,
    }
    return render(request, 'accounts/view-profile.html', context)


@login_required
def edit_profile(request, pk):
    profile = Profile.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()
            return redirect('view profile', pk)
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,

    }
    return render(request, 'accounts/edit-profile.html', context)
