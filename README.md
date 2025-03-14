# Meta Backend Capstone

Ce projet est le projet final du cours **Meta Back-End Development**.

## 📌 Structure de l'API

### 🏠 Base URL
```
/api/
```

### 📋 Menu Items
- Liste des éléments du menu :
  ```
   /api/menu/
  ```
- Détails, modification ou suppression d'un élément du menu :
  ```
   /api/menu/{menuItemId}
   /api/menu/{menuItemId}
   /api/menu/{menuItemId}
  ```

### 📅 Réservations de Tables
- Liste des réservations de tables :
  ```
   /api/booking/tables/
  ```
- Détails, modification ou suppression d'une réservation :
  ```
   /api/booking/tables/{bookingId}
   /api/booking/tables/{bookingId}
   /api/booking/tables/{bookingId}
  ```

## 🔑 Authentification
L'API utilise **[Django REST Framework Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)** pour la gestion des utilisateurs.

- Création d'un utilisateur :
  ```
  POST /auth/users/
  ```

## 🚀 Technologies utilisées
- **Django** & **Django REST Framework**
- **MySQL** (Base de données)
- **JWT (JSON Web Token)** pour l'authentification
- **Joser** pour la gestion des utilisateurs

## 📌 Instructions d'installation
1. Cloner le projet :
   ```sh
   git clone https://github.com/ton-utilisateur/ton-repo.git
   cd ton-repo
   ```
2. Effectuer les migrations :
   ```sh
   python manage.py migrate
   ```
3. Démarrer le serveur :
   ```sh
   python manage.py runserver
   ```

## 📫 Contact
Si vous avez des questions, n'hésitez pas à me contacter ! 😊

