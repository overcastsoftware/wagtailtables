from sre_constants import CHARSET

from wagtail.core.blocks import (CharBlock, ChoiceBlock, RichTextBlock,
                                 StreamBlock, StructBlock, TextBlock)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailtables.blocks import TableBlock


class ContentBlocks(StreamBlock):
    title = CharBlock()
    table_block = TableBlock()
