from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import Recherche
from .models import Train
#On importe les dossiers


def info(request, id) :
#On créer une fonction info qui va récuperer l'id de chaque trains.
    train = Train.objects.get(pk=id)    
    #On récuprère l'id du train
    return render(request, "metro/info.html", {"train": train})
    #Return nous renvoie le train lié à son id 

def index(request):
    trains = Train.objects.all()
    #Cette fonction récupère tous les objets de modèle Train dans la base de données
    # et les stocke dans une variable appelée "trains".
    if request.method == "POST":
        form = Recherche(request.POST)
    #Cette instruction vérifie si la méthode de la requête HTTP est POST 
    #et crée un formulaire de recherche en utilisant les données POST reçues.
        if form.is_valid():
            query = request.POST.get('query')
            #Cette condition vérifie si les données entrées dans le formulaire sont valides,
            #puis récupère le contenu du champ de formulaire nommé 'query' à partir de la requête POST.
            try:
                try:
                    train = Train.objects.get(pk=int(query))
                    print(train)
                    #ON récupère l'id du train puis on l'affiche
                    return HttpResponseRedirect(f"/metro/train-info-{train.pk}")
                #Ca nous renvoie sur la page du train destiné
                except ValueError:
                    train = Train.objects.get(destination=query)
                    return HttpResponseRedirect(f"/metro/train-info-{train.pk}")
            except Train.DoesNotExist:
                #Si la requete ne mène à rien 
                return render(request, "metro/index.html", {"form": form, "trains": trains, "error": f"Votre destination ({query}) n'existe pas. Vérifiez que vous avez bien écrit."})
            #On affiche un message d'erreur 
    else:
        form = Recherche()

    return render(request, "metro/index.html", {"form": form, "trains": trains})
    #Si la recherche est conforme, on renvoie le user sur la page du train indiqué
