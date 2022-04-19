from django import forms
from .models import Superhero
from .models import Jeniskelamin
from .models import Skillhero
from .models import Role

class SuperheroForm(forms.Form):
  class Meta:
    model = Superhero
    fields = "__all__"

class JeniskelaminForm(forms.Form):
  class Meta:
    model = Jeniskelamin
    fields = "__all__"

class SkillheroForm(forms.Form):
  class Meta:
    model = Skillhero
    fields = "__all__"

class RoleForm(forms.Form):
  class Meta:
    model = Role
    fields = "__all__"