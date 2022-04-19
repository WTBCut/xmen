from django.shortcuts import render, redirect

from .forms import SuperheroForm
from .models import Superhero
from .forms import JeniskelaminForm
from .models import Jeniskelamin
from .models import Skillhero
from .forms import SkillheroForm
from .models import Role
from .forms import RoleForm

# HERO
def index(request): 
  superheroes = Superhero.objects.all()
  

  context = {
    'hero_title':'X-MEN',
    'hero_desc':'Ini adalah X-MEN, ini adalah tentang para pahlawan pembela bumi.',
    'heroes':superheroes,
  } 

  return render(request,'hero/index.html', context)

def create(request): 
  Superhero_Form = SuperheroForm(request.POST or None)
  if request.method == "POST":
    if Superhero_Form.is_valid():
      Superhero.objects.create(
        nama = request.POST.get('nama'),
        jenis_kelamin = request.POST.get("jnsk")
      )
    return redirect('index')
  context = {
    'hero_title':'Create hero',
    'jenis':Jeniskelamin.objects.all(),
    'superhero_form':Superhero_Form
  }
  return render(request,'hero/create.html', context)

def delete(request, id):
    Superhero.objects.get(id=id).delete()
    return redirect('/')

#END HERO

# DETAIL HERO
def detail(request, id):
    skillheroes = Skillhero.objects.filter(id_hero=id)
    context = {
      'hero_title':'X-MEN',
      'hero_desc':'Ini adalah X-MEN, ini adalah tentang para pahlawan pembela bumi.',
      'heroes':skillheroes,
      'detaildata':Superhero.objects.get(id=id)
    }
    
    return render(request, "hero/detail.html", context)
#END DETAIL HERO

# SKILL
def daftarskill(request): 
  skillheroes = Skillhero.objects.all()

  context = {
    'hero_title':'X-MEN',
    'hero_desc':'Ini adalah X-MEN, ini adalah tentang para pahlawan pembela bumi.',
    'skill':skillheroes
  } 

  return render(request,'skill/daftarskill.html', context)

def createskill(request): 
  Skillheroes_form = SkillheroForm(request.POST or None)
  if request.method == "POST":
    if Skillheroes_form.is_valid():
      Skillhero.objects.create(
        skill = request.POST.get('skill'),
      )
    return redirect('daftarskill')
  context = {
    'hero_title':'X-MEN',
    'hero_desc':'Ini adalah X-MEN, ini adalah tentang para pahlawan pembela bumi.',
    'skillheroes_form':Skillheroes_form
  }
  return render(request,'skill/createskill.html', context)

def detailskill(request, id):
    Roles = Role.objects.filter(id_skills=id)
    Superheroes = Superhero.objects.all()
    context = {
      'hero_title':'X-MEN',
      'hero_desc':'Ini adalah X-MEN, ini adalah tentang para pahlawan pembela bumi.',
      'heroes':Roles,
      'detaildata':Skillhero.objects.get(id=id)
    }
    
    return render(request, "skill/detailskill.html", context)
# END SKILL


def tambahhero(request, id):
    superheroes = Superhero.objects.all()
    roles_form = RoleForm(request.POST or None)
    if request.method == "POST":
      if roles_form.is_valid():
        Role.objects.create(
          id_hero = request.POST.get('idhero'),
          id_skills = request.POST.get('id_skill')
        )
      return redirect('daftarskill')
    context = {
      'hero_title':'X-MEN',
      'hero_desc':'Ini adalah X-MEN, ini adalah tentang para pahlawan pembela bumi.',
      'rolehero':roles_form,
      'dataskill':Skillhero.objects.get(id=id),
      'datahero':superheroes,
    }
    return render(request,'skill/tambahhero.html', context)