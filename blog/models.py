from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse 



class Post(models.Model): #criando a tabela Post para armazenar os posts / NOT NULL é padrão / Id é padrão id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-create",)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):# Cria url pelo nome do slug
        return reverse("blog:detail", kwargs={"slug": self.slug})

