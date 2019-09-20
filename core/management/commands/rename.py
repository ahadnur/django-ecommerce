from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = "Renames a django project!..."


    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help="The new django project name.")
        

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']


        files_to_rename = ['dj_boilerplate/settings/base.py', 'dj_boilerplate/wsgi.py', 'manage.py']
        folder_to_rename = 'dj_boilerplate'

        for f in files_to_rename:
            with open(f, 'r') as file:
                fileData = file.read()
                
            fileData = fileData.replace('dj_boilerplate', new_project_name)

            with open(f, 'w') as file:
                file.write(fileData)
        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS('Project has been renamed to {}'.format(new_project_name)))