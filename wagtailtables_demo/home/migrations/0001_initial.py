# Generated by Django 4.0.4 on 2022-04-26 22:34

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtailtables.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock()), ('table_block', wagtail.core.blocks.StructBlock([('table_data', wagtail.core.blocks.TextBlock(default='[]')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('header_row', wagtail.core.blocks.BooleanBlock(required=False)), ('header_col', wagtail.core.blocks.BooleanBlock(required=False)), ('table_type', wagtail.core.blocks.ChoiceBlock(choices=wagtailtables.blocks.get_choices))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
