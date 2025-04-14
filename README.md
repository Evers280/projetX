# projetX

# Configuration de l'API Django pour ce projet

Ce document explique comment configurer et utiliser l'intégration avec une API REST Django dans cette application React.

## Configuration

### Variables d'environnement

Pour configurer la connexion à votre API Django, créez un fichier `.env.local` à la racine du projet avec les variables suivantes:

```
VITE_API_BASE_URL=http://votre-api-django.com/api
```

Si vous travaillez en local, l'URL sera probablement:
```
VITE_API_BASE_URL=http://localhost:8000/api
```

### Configuration CORS côté Django

Pour que votre API Django accepte les requêtes de cette application frontend, vous devez configurer CORS dans votre projet Django:

1. Installez django-cors-headers:
```bash
pip install django-cors-headers
```

2. Ajoutez-le à vos INSTALLED_APPS dans settings.py:
```python
INSTALLED_APPS = [
    # ...
    'corsheaders',
    # ...
]
```

3. Ajoutez le middleware CORS (idéalement en haut de la liste):
```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...autres middlewares
]
```

4. Configurez CORS dans settings.py:
```python
# Pour le développement (permet toutes les origines)
CORS_ALLOW_ALL_ORIGINS = True

# Pour la production (spécifiez les domaines autorisés)
# CORS_ALLOWED_ORIGINS = [
#     "https://votre-app-frontend.com",
#     "http://localhost:8080",
# ]
```

## Utilisation des services API

### Utilisation des hooks pour accéder aux données

Le projet fournit plusieurs hooks qui utilisent React Query pour interagir avec l'API:

```jsx
import { useEvents, useEvent, useCreateEvent, useUpdateEvent, useDeleteEvent } from '../hooks/useEvents';

// Dans votre composant:
const EventsList = () => {
  const { data: events, isLoading, error } = useEvents();

  if (isLoading) return <p>Chargement...</p>;
  if (error) return <p>Erreur: {error.message}</p>;

  return (
    <div>
      {events?.map(event => (
        <div key={event.id}>{event.title}</div>
      ))}
    </div>
  );
};
```

### Authentification

Pour utiliser l'authentification avec l'API:

1. Remplacez le `AuthProvider` par `ApiAuthProvider` dans App.tsx:

```jsx
import { ApiAuthProvider } from "./contexts/ApiAuthContext";

const App = () => (
  <QueryClientProvider client={queryClient}>
    <ApiAuthProvider>
      {/* Le reste de votre application */}
    </ApiAuthProvider>
  </QueryClientProvider>
);
```

2. Utilisez le hook `useApiAuth` au lieu de `useAuth` dans vos composants:

```jsx
import { useApiAuth } from "../contexts/ApiAuthContext";

const LoginPage = () => {
  const { login, isLoading } = useApiAuth();
  
  // Utiliser la fonction login...
};
```


## Structure de l'API côté Django

Pour que cette intégration fonctionne correctement, votre API Django doit exposer les endpoints suivants:

### Authentification
- POST `/api/auth/login/` - Pour l'authentification
- POST `/api/auth/register/` - Pour l'enregistrement

### Événements
- GET `/api/events/` - Liste des événements
- GET `/api/events/:id/` - Détails d'un événement
- POST `/api/events/` - Créer un événement
- PUT `/api/events/:id/` - Mettre à jour un événement
- DELETE `/api/events/:id/` - Supprimer un événement

### Tickets
- GET `/api/tickets/` - Liste des tickets
- GET `/api/tickets/:id/` - Détails d'un ticket
- POST `/api/tickets/` - Créer un ticket
- POST `/api/tickets/:id/validate/` - Valider un ticket

Vous pouvez adapter ces endpoints selon la structure de votre API Django.

