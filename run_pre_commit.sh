#!/bin/bash

source env/bin/activate  # Active l'environnement virtuel
pre-commit "$@"           # Exécute pre-commit avec tous les arguments transmis
