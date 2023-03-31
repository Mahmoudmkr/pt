from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from . import forms
from . import models


class CustomerListView(ListView):
    model=models.Customer
    template_name = 'project/list.html'

class CustomerCreateView(CreateView):
    model=models.Customer
    form_class = forms.CustomerCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('customer_list')

class CustomerUpdateView(UpdateView):
    model=models.Customer
    form_class = forms.CustomerUpdateForm
    template_name = 'project/update.html'
    success_url = reverse_lazy('customer_list')


class CustomerDeleteView(DeleteView):
    model=models.Customer
    template_name = 'project/delete.html'
    success_url = reverse_lazy('customer_list')

class TaskCreateView(CreateView):
    model=models.Task
    template_name = 'project/task.html'
    fields=['description','customer']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('customer_update',args=[self.object.customer.id])

class TaskUpdateView(UpdateView):
    model=models.Task
    template_name = 'project/task.html'
    fields=['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('customer_update',args=[self.object.customer.id])

class TaskDeleteView(DeleteView):
    model=models.Task

    def get_success_url(self):
        return reverse('customer_update',args=[self.object.customer.id])