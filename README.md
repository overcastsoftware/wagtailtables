# Wagtail Tables
jspreadsheet tables in Wagtail, edited and customised from the Wagtail admin

## Getting started

Assuming you have a Wagtail project up and running:

`pip install wagtailtables`

Add `wagtailtables` to your settings.py in the INSTALLED_APPS section, before the core wagtail packages:

```python
INSTALLED_APPS = [
    # ...
    'wagtailtables',
    # ...
]
```

Add a wagtailtables TableBlock to one of your StreamFields:

```python
from wagtailtables.blocks import TableBlock

class ContentBlocks(StreamBlock):
    table_block = TableBlock()
```

Include your streamblock in one of your pages

```python
class HomePage(Page):
    body = StreamField(ContentBlocks())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
```

Simply render your table block as you would render any other block.

```django
{% load wagtailcore_tags %}

{% block content %}
<div class="container-fluid">
    <div class="row">
        <div class="col-6">
            <h1>{{self.title}}</h1>
            <div class="excerpt">{{self.excerpt|richtext}}</div>
        </div>
    </div>
    {% for block in self.body %}
        {% include_block block %}
    {% endfor %}
</div>
{% endblock %}
```

## Configuration

### Customized toolbar
`TableBlock` accepts a toolbar argument in addition to the standard `StructBlock` arguments.

The toolbar is an array of dicts, this is the default:
```python
TOOLBAR = [
    {'type': 'i', 'content': 'format_align_left', 'k': 'text-align', 'v': 'left'},
    {'type': 'i', 'content': 'format_align_center', 'k':'text-align', 'v':'center'},
    {'type': 'i', 'content': 'format_align_right', 'k': 'text-align', 'v': 'right'},
    {'type': 'i', 'content': 'format_bold', 'k': 'font-weight', 'v': '600'},
    {'type': 'i', 'content': 'format_italic', 'k': 'font-style', 'v': 'italic'},
    {'type': 'i', 'content': 'border_left', 'k': 'border-left', 'v': '1px solid'},
    {'type': 'i', 'content': 'border_right', 'k': 'border-right', 'v': '1px solid'},
    {'type': 'i', 'content': 'border_top', 'k': 'border-top', 'v': '1px solid'},
]

class ContentBlocks(StreamBlock):
    table_block = TableBlock(toolbar=TOOLBAR)
```

`type` should for now always be `i` for icon, we will provide more types later

`content` defines the icon (from material icons) [click here for all possible keys](https://fonts.google.com/icons?selected=Material+Icons)

`k` means the style that should be apply to the cell

`v` means the value of the style should be apply to the cell


## Dependencies
* This project relies on [Jspreadsheet Community Edition](https://bossanova.uk/jspreadsheet/v4/) for data entry and manipulation. 
