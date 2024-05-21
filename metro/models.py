from django.db import models

#On créer la base de données avec les infos indiquées.

class Train(models.Model):
    id = models.AutoField(primary_key = True)
    datetime = models.CharField(max_length = 5)
    destination = models.CharField(max_length = 100)
    plan = models.CharField(max_length = 100)
#On donne les caractéristiques de chaque infos insérées dans la BDD

    def __str__(self):
        return f"{self.destination} ({self.datetime})"
    #On nomme nos infos dans la base de donées dans l'url Admin

