from django.core.management.base import BaseCommand
from catalogue.models import Genre, SubGenre

class Command(BaseCommand):
    help = 'Populate the database with initial genres and sub-genres'

    def handle(self, *args, **kwargs):
        data = {
            'Fiction': [
                'Literary Fiction', 'Historical Fiction', 'Science Fiction', 'Fantasy', 'Mystery',
                'Thriller', 'Romance', 'Young Adult (YA)', 'Dystopian', 'Magical Realism', 'Adventure'
            ],
            'Non-Fiction': [
                'Biography', 'Memoir', 'Self-Help', 'True Crime', 'History', 'Science', 'Travel',
                'Health & Wellness', 'Business & Economics', 'Politics', 'Philosophy', 'Religion & Spirituality'
            ],
            'Mystery': [
                'Detective Fiction', 'Cozy Mystery', 'Police Procedural', 'Hard-Boiled', 'Legal Thriller',
                'Medical Mystery', 'Noir', 'Crime Thriller'
            ],
            'Science Fiction': [
                'Cyberpunk', 'Space Opera', 'Time Travel', 'Dystopian', 'Apocalyptic/Post-Apocalyptic',
                'Military Science Fiction', 'Alien Invasion', 'Hard Science Fiction'
            ],
            'Fantasy': [
                'High Fantasy', 'Urban Fantasy', 'Dark Fantasy', 'Sword and Sorcery', 'Magical Realism',
                'Paranormal', 'Epic Fantasy', 'Fairy Tale Retelling'
            ],
            'Romance': [
                'Contemporary Romance', 'Historical Romance', 'Romantic Suspense', 'Paranormal Romance',
                'Erotic Romance', 'Young Adult Romance', 'Chick Lit', 'Inspirational Romance'
            ],
            'Thriller': [
                'Psychological Thriller', 'Crime Thriller', 'Legal Thriller', 'Espionage Thriller',
                'Action Thriller', 'Political Thriller', 'Military Thriller', 'Medical Thriller'
            ],
            'Young Adult (YA)': [
                'YA Fantasy', 'YA Science Fiction', 'YA Romance', 'YA Dystopian', 'YA Mystery', 'YA Contemporary',
                'YA Historical Fiction', 'YA Paranormal'
            ],
            'Historical': [
                'Historical Fiction', 'Historical Romance', 'Historical Mystery', 'Historical Fantasy',
                'Alternate History', 'Historical Adventure', 'Biographical Historical'
            ],
            'Horror': [
                'Gothic Horror', 'Paranormal Horror', 'Psychological Horror', 'Slasher', 'Supernatural Horror',
                'Zombie Horror', 'Occult Horror', 'Monster Horror'
            ]
        }

        for genre_name, subgenres in data.items():
            genre, created = Genre.objects.get_or_create(name=genre_name)
            for subgenre_name in subgenres:
                SubGenre.objects.get_or_create(name=subgenre_name, genre=genre)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with genres and sub-genres'))
