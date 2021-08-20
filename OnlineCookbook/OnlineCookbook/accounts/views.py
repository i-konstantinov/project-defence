from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from OnlineCookbook.accounts.forms import RegisterForm, ProfileForm
from OnlineCookbook.accounts.models import Profile
from OnlineCookbook.recipes.models import Recipe


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


class UserLoginView(LoginView):
    template_name = 'accounts/log-in.html'

    def get_success_url(self):
        return reverse_lazy('index')


class UserLogoutView(LogoutView):
    template_name = 'index.html'


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/view-profile.html'

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user_id=self.kwargs.get('pk'))

        profile_owner = self.request.user.id == profile.user_id

        recipes_added_by_user = Recipe.objects.filter(user_id=profile.user_id)

        recipes_liked_by_user = Recipe.objects.filter(like__user=profile.user_id)

        context = super().get_context_data(**kwargs)

        context['profile'] = profile
        context['profile_owner'] = profile_owner
        context['recipes_added_by_user'] = recipes_added_by_user
        context['recipes_liked_by_user'] = recipes_liked_by_user
        return context


class ProfileEditView(UpdateView):
    model = Profile

    form_class = ProfileForm
    template_name = 'accounts/edit-profile.html'

    def get_success_url(self):
        return reverse_lazy('view profile', kwargs={'pk': self.kwargs['pk']})

