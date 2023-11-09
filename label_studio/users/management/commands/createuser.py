from django.core.management.base import BaseCommand, CommandError
from users.forms import UserSignupForm

class Command(BaseCommand):
    help = "Crea usuarios utilizando los datos proporcionados por el usuario"
    # La idea es que este comando funcione de manera similar a createsuperuser pero para un usuario comun
    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Correo electrónico')
        parser.add_argument('password', type=str, help='Contraseña')



    def handle(self, *args, **options):
        email = options['email']
        password = options['password']
        form = UserSignupForm({'email': email, 'password': password})
        print(form)
        #form.allow_newsletters = False
        if form.is_valid():
            form.save()
            self.stdout.write(self.style.SUCCESS(f'Se ha creado el usuario: {email}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Invalido {email}'))
 