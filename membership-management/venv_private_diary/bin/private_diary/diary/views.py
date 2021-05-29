from .forms import InquiryForm
from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy

import logging


logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        logger.info('Inquiry sent by{}'.format(form.cleaned_date['name']))
        return super().form_valid(form)
