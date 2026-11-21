# IAM BIG MAN — V23 · Correctifs fonctionnels vérifiés

## Problème critique corrigé
Dans les 20 fichiers `templates/*/app.js`, le script cherchait `#phone` et `#email` supprimés des pages HTML. Une exception JavaScript interrompait le rendu avant les cartes, la recherche et les gestionnaires de formulaires. Ces accès invalides ont été supprimés. Les coordonnées de démonstration ne sont plus présentées comme liens de contact.

## Contrôles automatiques
- Intégrité du ZIP, présence de 20 démos et 20 templates.
- Analyse syntaxique de tous les scripts JS avec Node.js.
- Présence des éléments DOM nécessaires à chaque script.
- Analyse des JSON et présence des images WebP.

## Tester sur Android (Acode)
1. Décompresser toute l’archive dans un dossier neuf.
2. Ouvrir `index.html`, puis la boutique et le lien « Live demo ».
3. Ouvrir `templates/restaurant/index.html` et `templates/barber/index.html`.
4. Vérifier que les cartes de services apparaissent, puis filtrer un mot dans la recherche.
5. Remplir le formulaire avec un message de 10 caractères minimum ; le bouton e-mail ouvre l’application de messagerie (il n’envoie pas automatiquement).
6. Tester les liens de navigation, puis refaire le test sur les autres templates.

## Limites honnêtes
Les 20 sites sont des démos et bases personnalisables. La réservation, le paiement, l’envoi automatique des formulaires de templates, les coordonnées réelles des futurs clients et les obligations légales restent à configurer au cas par cas. Le formulaire principal du studio a été testé par l’utilisateur via une notification reçue dans Gmail, mais sa disponibilité continue n’est pas garantie. Aucun test visuel exhaustif sur appareils réels n’est revendiqué.
