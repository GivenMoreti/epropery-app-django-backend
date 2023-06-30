
from django.forms import ModelForm
from .models import SearchModel

class SearchFormTwo(ModelForm):
  class Meta:
    model = SearchModel
    fields = "__all__"