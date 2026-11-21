# IAM BIG MAN — V20 | Guide de vérification

## Modifications
- 20 templates: configuration embarquée dans index.html pour fonctionner même via file:// dans Acode.
- config.json reste la source éditable utilisée sur un serveur HTTP/HTTPS; après modification de config.json, il faut aussi actualiser la copie embarquée pour que file:// affiche les changements.
- Formulaire principal: avertissement visible et liens de secours vers e-mail / WhatsApp. La destination Formspree reste inchangée et n’est pas vérifiée.

## Vérifications manuelles nécessaires
1. Ouvrir `index.html` dans Acode, puis `templates/restaurant/index.html` via Acode ou Chrome.
2. Vérifier menu, recherche, filtres, photos, contact et retour en haut.
3. Envoyer un message test depuis le formulaire principal et confirmer réception dans la boîte e-mail; en cas d’échec, utiliser les liens directs.
4. Tester chaque démo et template sur Android, puis en navigation desktop.
5. Avant livraison client: remplacer toutes les données fictives, vérifier mentions légales, formulaires et droits d’image.

Aucune réservation, paiement, ni livraison client automatisés ne sont activés.
