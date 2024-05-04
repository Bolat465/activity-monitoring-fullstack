from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.views import LogoutView 
from django.views.generic import TemplateView
from .forms import LoginForm
from django.shortcuts import redirect

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home_page')  # Перенаправление после успешного входа

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            # Если пользователь не найден, возвращаем ошибку на страницу входа
            return self.form_invalid(form)

    def form_invalid(self, form):
        # Можно добавить кастомное сообщение об ошибке
        form.add_error(None, 'Invalid credentials')
        return super().form_invalid(form)
    

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class UserProfileView(TemplateView):
    template_name = 'profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context