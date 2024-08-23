from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, View, ListView
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm, UserUpdateForm, UserPasswordChangeForm
from transactions.views import send_transaction_email
from history.models import BorrowHistory
from transactions.constants import BORROW_BOOK
from django.utils.dateparse import parse_date
from django.db.models import Q

# Create your views here.

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('profile'))
        return super().dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
    
class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('profile'))
        return super().dispatch(request, *args, **kwargs)
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('home')

class UserAccountUpdateView(View):
    template_name = 'accounts/update_profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Account Updated successfully !!')
            return redirect('profile')
        return render(request, self.template_name, {'form': form})
    
class UserPassChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Password changed successfully')
        send_transaction_email(
                user = self.request.user,
                subject = "Change Password",
                template = "accounts/change_password_email.html",
            )
        return super().form_valid(form)

class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'accounts/profile.html'
    model = BorrowHistory
    context_object_name = 'borrow_list'
    is_filter = False

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
        
        if start_date_str and end_date_str:
            start_date = parse_date(start_date_str)
            end_date = parse_date(end_date_str)
            
            queryset = queryset.filter(
                Q(transaction__timestamp__date__gte=start_date) &
                Q(transaction__timestamp__date__lte=end_date) &
                Q(transaction__transaction_type=BORROW_BOOK)
            )
            self.is_filter = True
        else:
            self.is_filter = False
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account,
            'is_filter': self.is_filter,
        })
        return context