1. Quelle est la différence entre une requête GET et une requête POST dans le contexte d’un formulaire ?

GET : envoie les données du formulaire dans l’URL (ex : /search?name=Alex).
Elle sert surtout à afficher une page, lire des informations, ou rechercher quelque chose.
Les données ne sont pas sensibles.

POST : envoie les données dans le corps de la requête (invisibles dans l’URL).
Elle sert à modifier, ajouter, supprimer ou envoyer des informations importantes, comme un mot de passe ou un formulaire d’ajout.
Les données sont plus sécurisées.

2. À quoi sert redirect(url_for(...)) dans une application Flask ?

redirect(url_for(...)) sert à rediriger l’utilisateur vers une autre page après une action.
Par exemple, après avoir ajouté ou supprimé une tâche, on redirige vers la page d’accueil pour :

éviter de re-soumettre le formulaire si l’utilisateur recharge la page

afficher correctement les nouvelles données

garder la logique propre dans l’application

C’est la méthode standard pour terminer un formulaire POST.

3. Expliquez le rôle des blocs et de l’héritage de templates dans Jinja.

L’héritage de templates permet de créer un template parent (ex : base.html) contenant tout ce qui est commun : navigation, styles, structure.

Les pages enfants (ex : home.html, edit.html) remplissent seulement des blocs comme :

{% block content %}
    ... contenu spécifique ...
{% endblock %}


Cela permet de :

réutiliser le même design sur toutes les pages

éviter de copier/coller du HTML

rendre le code plus clair, organisé et maintenable

4. Donnez un exemple de situation où JavaScript côté client est plus adapté que le traitement côté serveur en Python.

JavaScript est plus adapté lorsqu’on veut faire des actions instantanées sur la page, sans recharger le serveur.

Exemples :

afficher/masquer un message

valider un formulaire en temps réel

mettre à jour un compteur

changer la couleur ou le style d’un élément

afficher une alerte

appliquer un filtre sans recharger la page

➡️ JavaScript est donc idéal pour les interactions rapides avec l’utilisateur, tandis que Python gère les traitements plus lourds côté serveur.