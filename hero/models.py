from django.db import models
# Create your models here.

class Superhero(models.Model):
  id = models.AutoField(primary_key=True)
  nama = models.CharField(max_length=100)
  jenis_kelamin = models.CharField(max_length=100)
  def __str__(self):
    return self.nama

class Jeniskelamin(models.Model):
  id = models.AutoField(primary_key=True)
  jenis = models.CharField(max_length=100)
  def __str__(self):
    return self.jenis

class Skillhero(models.Model):
  id = models.AutoField(primary_key=True)
  skill = models.CharField(max_length=100)
  def __str__(self):
    return self.skill

class Role(models.Model):
  id_hero = models.IntegerField(null=True)
  id_skills = models.IntegerField(null=True)
  def __str__(self):
    return self.id_hero