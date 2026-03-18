import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create or update a default test user for local/dev environments."

    def handle(self, *args, **options):
        email = os.getenv("TEST_USER_EMAIL", "user@test.dev")
        password = os.getenv("TEST_USER_PASSWORD", "test1234")
        User = get_user_model()

        user, created = User.objects.get_or_create(email=email, defaults={"is_active": True})
        user.set_password(password)
        user.save(update_fields=["password", "is_active"])

        if created:
            self.stdout.write(self.style.SUCCESS(f"Created test user: {email}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Updated test user password: {email}"))
