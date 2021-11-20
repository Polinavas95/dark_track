
from django.views.generic.edit import FormView

from .forms import TractorTrackForm


class TractorTrackView(FormView):
    form_class = TractorTrackForm
    template_name = 'index.html'
#    success_url = 'index.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
