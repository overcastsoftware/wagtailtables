from sre_constants import CHARSET

from wagtail.core.blocks import (CharBlock, ChoiceBlock, RichTextBlock,
                                 StreamBlock, StructBlock, TextBlock)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailtables.blocks import TableBlock

TOOLBAR = [
    {'type': 'i','content': 'format_align_left', 'k': 'text-align', 'v': 'left'},
    {'type': 'i','content': 'format_align_center', 'k':'text-align', 'v':'center'},
    {'type': 'i','content': 'format_align_right', 'k': 'text-align', 'v': 'right'},
    {'type': 'i','content': 'format_bold', 'k': 'font-weight', 'v': '600'},
    {'type': 'i','content': 'format_italic', 'k': 'font-style', 'v': 'italic'},
    {'type': 'i','content': 'border_left', 'k': 'border-left', 'v': '1px solid'},
    {'type': 'i','content': 'border_right', 'k': 'border-right', 'v': '1px solid'},
    {'type': 'i','content': 'border_top', 'k': 'border-top', 'v': '1px solid'},
]

class ContentBlocks(StreamBlock):
    title = CharBlock()
    table_block = TableBlock(toolbar=TOOLBAR)
