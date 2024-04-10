from django.core.management.base import BaseCommand
from django.utils import timezone
from sncfapp.models import Trains
from datetime import time

class Command(BaseCommand):
    help = 'Ajoute des trains à la base de données'

    def handle(self, *args, **options):
        # Liste des données des trains à ajouter
        trains_to_add = [
            {
                'name': 'TGV',
                'image': 'https://upload.wikimedia.org/wikipedia/fr/thumb/3/31/Logo_TGV_inOui_2017.svg/1280px-Logo_TGV_inOui_2017.svg.png',
                'departure': time(10, 45),
                'arrive': time(16, 45),
                'destination': 'Paris',
                'description': 'Train à grande vitesse de la SNCF.'
            },
            {
                'name': 'RER A',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Logo_RER_A.svg/800px-Logo_RER_A.svg.png',
                'departure': time(12, 45),
                'arrive': time(19, 35),
                'destination': 'Marne-la-Vallée',
                'description': 'Réseau Express Régional reliant Paris à sa banlieue.'
            },
            {
                'name': 'TGV',
                'image': 'https://upload.wikimedia.org/wikipedia/fr/thumb/3/31/Logo_TGV_inOui_2017.svg/1280px-Logo_TGV_inOui_2017.svg.png',
                'departure': time(11, 45),
                'arrive': time(19, 22),
                'destination': 'Paris',
                'description': 'Train à grande vitesse de la SNCF.'
            },
            {
                'name': 'RER A',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Logo_RER_A.svg/800px-Logo_RER_A.svg.png',
                'departure': time(3, 45),
                'arrive': time(12, 45),
                'destination': 'Marne-la-Vallée',
                'description': 'Réseau Express Régional reliant Paris à sa banlieue.'
            },
            {
                'name': 'TER',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Logo_TER.svg/1280px-Logo_TER.svg.png',
                'departure': time(8, 20),
                'arrive': time(12, 12),
                'destination': 'Lyon',
                'description': 'Train Express Régional desservant les régions.'
            },
            {
                'name': 'Intercités',
                'image': 'https://upload.wikimedia.org/wikipedia/fr/thumb/2/29/SNCF_Intercit%C3%A9s.svg/2560px-SNCF_Intercit%C3%A9s.svg.png',
                'departure': time(16, 45),
                'arrive': time(22, 21),
                'destination': 'Bordeaux',
                'description': 'Train interurbain de la SNCF.'
            },
            {
                'name': 'Transilien',
                'image': 'https://upload.wikimedia.org/wikipedia/fr/thumb/2/2c/Logo_SNCF_Transilien_2019.svg/1200px-Logo_SNCF_Transilien_2019.svg.png',
                'departure': time(1, 45),
                'arrive': time(10, 10),
                'destination': 'Versailles',
                'description': 'Réseau de trains de banlieue de la SNCF.'
            },
            {
                'name': 'RER B',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Logo_RER_B.svg/1024px-Logo_RER_B.svg.png',
                'departure': time(1, 45),
                'arrive': time(18, 20),
                'destination': 'Aéroport Charles de Gaulle',
                'description': 'Réseau Express Régional reliant Paris à l\'aéroport Charles de Gaulle.'
            },
            {
                'name': 'RER C',
                'image': 'https://upload.wikimedia.org/wikipedia/fr/thumb/c/c1/Logo_RER_C.svg/2560px-Logo_RER_C.svg.png',
                'departure': time(8, 15),
                'arrive': time(23, 30),
                'destination': 'Versailles-Château Rive Gauche',
                'description': 'Réseau Express Régional reliant Paris à Versailles-Château Rive Gauche.'
            },
            {
                'name': 'RER D',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/IDF_RER_D_logo.svg/1280px-IDF_RER_D_logo.svg.png',
                'departure': time(19, 30),
                'arrive': time(23, 45),
                'destination': 'Melun',
                'description': 'Réseau Express Régional reliant Paris à Melun.'
            },
            {
                'name': 'RER E',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/IDF_RER_E_logo.svg/1280px-IDF_RER_E_logo.svg.png',
                'departure': time(21, 45),
                'arrive': time(23, 40),
                'destination': 'Chelles-Gournay',
                'description': 'Réseau Express Régional reliant Paris à Chelles-Gournay.'
            },
        ]

        # Parcours de la liste des trains à ajouter
        for train_data in trains_to_add:
            # Création d'une nouvelle instance de Trains et ajout à la base de données
            train = Trains.objects.create(
                name=train_data['name'],
                image=train_data['image'],
                departure=train_data['departure'],
                arrive=train_data['arrive'],
                destination=train_data['destination'],
                description=train_data['description']
            )
            # Affichage d'un message de succès dans la console
            self.stdout.write(self.style.SUCCESS(f"Train '{train.name}' ajouté avec succès."))
        # Affichage d'un message de fin dans la console
        self.stdout.write(self.style.SUCCESS("Tous les trains ont été ajoutés avec succès à la base de données."))