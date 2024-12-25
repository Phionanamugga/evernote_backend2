from django.apps import AppConfig




class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'

    def ready(self):
        import evernote.users.signals  # Import signals


class NotesConfig(AppConfig):
    name = 'evernote'  # Replace 'your_app_name' with the actual name of your app
    verbose_name = 'Notes'  # Optionally, add a human-readable name
