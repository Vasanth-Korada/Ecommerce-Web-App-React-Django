from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(
            name="vasanth",
            email="vasanthkorada999@gmail.com",
            is_staff=True,
            is_superuser=True,
            phone="8106237018",
            gender="Male"
        )

        user.set_password("vktech")
        user.save()
    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
