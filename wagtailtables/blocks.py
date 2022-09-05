import json
from django import forms
from django.conf import settings
from django.utils.functional import cached_property

from wagtail.core.telepath import register
from wagtail import VERSION

# Backwards compatibility
if VERSION[0] < 3:
    from wagtail.core.blocks.struct_block import StructBlockAdapter
    from wagtail.core.blocks import (BooleanBlock, CharBlock, ChoiceBlock,
                                 StructBlock, TextBlock)
else:
    from wagtail.blocks.struct_block import StructBlockAdapter
    from wagtail.blocks import (BooleanBlock, CharBlock, ChoiceBlock,
                                 StructBlock, TextBlock)

def get_choices():
    default_choices = (
        ('table', 'Table'),
    )
    table_types = getattr(settings, 'WAGTAILTABLE_TYPES', None)
    if table_types:
        return table_types
    return default_choices


class TableBlock(StructBlock):
    table_data = TextBlock(default="[]")
    caption = CharBlock(required=False)
    header_row = BooleanBlock(required=False)
    header_col = BooleanBlock(required=False)
    table_type = ChoiceBlock(choices=get_choices, default=get_choices()[0][0])

    def get_searchable_content(self, value):
        data = json.loads(value['table_data'])
        if isinstance(data, dict) and 'data' in data.keys():
            return data['data']
        return ""

    class Meta:
        icon = 'fa-table'
        label = 'Table Block'
        template = 'wagtailtables/table_block.html'


class TableAdapter(StructBlockAdapter):
    js_constructor = 'streams.blocks.TableBlock'

    @cached_property
    def media(self):
        structblock_media = super().media
        return forms.Media(
            js=structblock_media._js + ['wagtailtables/js/table-dataset.js', 'wagtailtables/js/jspreadsheet.js', 'wagtailtables/js/jsuites.js'],
            css={** structblock_media._css, **{'all': ('wagtailtables/css/jspreadsheet.css', 'wagtailtables/css/jspreadsheet.theme.css', 'wagtailtables/css/jsuites.css', 'https://fonts.googleapis.com/css?family=Material+Icons')}}
        )

register(TableAdapter(), TableBlock)
