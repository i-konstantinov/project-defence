from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, UpdateView
from django.views.generic.base import ContextMixin
from django.views.generic.detail import SingleObjectMixin

from OnlineCookbook.accounts.forms import LoginForm, RegisterForm, ProfileForm
from OnlineCookbook.accounts.models import Profile
from OnlineCookbook.common.models import Like
from OnlineCookbook.recipes.models import Recipe

UserModel = get_user_model()


class ListProfilesView(ListView):
    model = Profile
    template_name = 'accounts/list-profiles.html'
    context_object_name = 'profiles'


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


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


@login_required()
def log_out(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(LoginRequiredMixin, FormView):
    template_name = 'accounts/view-profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('view profile')

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        profile_owner = self.request.user.id == profile.user_id
        recipes_added_by_user = Recipe.objects.filter(user_id=profile.user_id)
        recipes_liked_by_user = [obj.recipe for obj in Like.objects.filter(user_id=profile.user_id)]
        context = super().get_context_data(**kwargs)

        context['profile'] = profile
        context['profile_owner'] = profile_owner
        context['recipes_added_by_user'] = recipes_added_by_user
        context['recipes_liked_by_user'] = recipes_liked_by_user
        return context

#
# @login_required
# def edit_profile(request, pk):
#     profile = Profile.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         form = ProfileForm(
#             request.POST,
#             request.FILES,
#             instance=profile,
#         )
#         if form.is_valid():
#             form.save()
#             return redirect('view profile', pk)
#     else:
#         form = ProfileForm(instance=profile)
#
#     context = {
#         'form': form,
#         'profile': profile,
#
#     }
#     return render(request, 'accounts/edit-profile.html', context)


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/edit-profile.html'
    success_url = reverse_lazy('list profiles')
