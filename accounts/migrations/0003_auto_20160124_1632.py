# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customeruser_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeruser',
            old_name='is_admin',
            new_name='is_superuser',
        ),
    ]
