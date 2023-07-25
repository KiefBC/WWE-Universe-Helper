from django.core.management import call_command, BaseCommand
from django.db import connection
import WWEUniverseWebApp.models
import time


class Command(BaseCommand):
    help = 'Reset database and populate it with data'

    def handle(self, *args, **options):
        # Reset DB
        call_command('flush', interactive=False)
        print('Doing our initial migrations')
        call_command('makemigrations')
        # time.sleep(1)
        call_command('migrate')

        # Populate Our Wrestlers Table With Some Data
        print('Populating Wrestler Table')
        wrestlers = {
            'Roman Reigns': {'weight_class': 'HW'},
            'Jey USO': {'weight_class': 'HW'},
            'Jimmy USO': {'weight_class': 'HW'},
            'Drew McIntyre': {'weight_class': 'HW'},
            'Bobby Lashley': {'weight_class': 'HW'},
            # etc.
        }

        for name, attrs in wrestlers.items():
            wrestler, created = WWEUniverseWebApp.models.Wrestlers.objects.update_or_create(
                name=name,
                weight_class=attrs['weight_class'],
            )
            if created:
                wrestler.save()
                print(f'Added {name} to the Wrestlers Table')
            else:
                print(f'{name} already exists in the Wrestlers Table')

        # Populate Our Shows Table With Some Data
        print('Populating Shows Table')
        shows = {
            'RAW': {'show_date': 'MON'},
            'Smackdown': {'show_date': 'FRI'},
            'NXT': {'show_date': 'TUE'},
            'AEW': {'show_date': 'WED'},
        }

        for show, attrs in shows.items():
            show, created = WWEUniverseWebApp.models.Shows.objects.update_or_create(
                show_name=show,
                show_date=attrs['show_date'],
            )
            if created:
                show.save()
                print(f'Added {show} to the Shows Table')
            else:
                print(f'{show} already exists in the Shows Table')

        # Populate Our Title Belts Table With Some Data
        print('Populating Title Belts Table')
        title_belts = {
            'WWE Universal Championship': {'weight_class': 'HW'},
            'WWE Championship': {'weight_class': 'HW'},
            'WWE Intercontinental Championship': {'weight_class': 'LHW'},
            'WWE United States Championship': {'weight_class': 'CW'},
        }

        for title, attrs in title_belts.items():
            title_belt, created = WWEUniverseWebApp.models.TitleBelts.objects.update_or_create(
                name=title,
                weight_class=attrs['weight_class'],
            )
            if created:
                title_belt.save()
                print(f'Added {title} to the Title Belts Table')
            else:
                print(f'{title} already exists in the Title Belts Table')
