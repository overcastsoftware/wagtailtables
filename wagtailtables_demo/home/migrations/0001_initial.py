# Generated by Django 4.0.4 on 2022-04-26 22:34

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
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
                ('body', wagtail.fields.StreamField([('title', wagtail.blocks.CharBlock()), ('table_block', wagtail.blocks.StructBlock([('table_data', wagtail.blocks.TextBlock(default='[]')), ('caption', wagtail.blocks.CharBlock(required=False)), ('header_row', wagtail.blocks.BooleanBlock(required=False)), ('header_col', wagtail.blocks.BooleanBlock(required=False)), ('table_type', wagtail.blocks.ChoiceBlock(choices=wagtailtables.blocks.get_choices))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
