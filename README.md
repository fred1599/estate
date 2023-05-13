# Projet Immobilier

Ce projet suit les principes de la Clean Architecture de Robert C. Martin (Uncle Bob). 

## Structure du projet

Le projet est organisé en plusieurs répertoires, chacun ayant un rôle spécifique :

- `adapters` : Ce répertoire contient le code qui convertit les données de la forme qu'elles ont dans une entité ou un cas d'utilisation à la forme dont l'interface utilisateur ou la base de données a besoin.
- `domain` : Ici se trouvent les objets du domaine métier, les services et les cas d'utilisation. Ces éléments sont au cœur de l'application.
- `infrastructure` : Cette couche contient les détails techniques de l'application, par exemple l'interaction avec la base de données Postgres.
- `interface` : Ce répertoire contient les présentateurs et les routeurs, qui sont responsables de l'interaction avec l'utilisateur ou d'autres systèmes.

Voici une illustration de la structure du projet :

```text
estate_project/
├── estate_project
│   ├── adapters
│   ├── domain
│   │   ├── entities
│   │   ├── services
│   │   └── use_cases
│   ├── infrastructure
│   │   └── db_postgres
│   └── interface
│       ├── presenters
│       └── routers
└── tests
    └── unit
        ├── adapters
        ├── domain
        │   ├── entities
        │   └── use_cases
        └── interface
