from django.db import models

class Directior(models.Model):
    name = models.CharField(max_length=40)
    birn_year = models.IntegerField()

    def __str__(self):
        return self.name


class Janr(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Films(models.Model):
    name = models.CharField(max_length=40)
    year_relise = models.IntegerField()
    country = models.CharField(max_length=30)
    director = models.ForeignKey(Directior, on_delete=models.CASCADE)
    janr = models.ForeignKey(Janr, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=40)
    relise_date = models.DateField()
    films = models.ManyToManyField(Films, blank=False)

    def __str__(self):
        return self.name