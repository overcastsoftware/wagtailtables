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

## Dependencies
* This project relies on [Jspreadsheet Community Edition](https://bossanova.uk/jspreadsheet/v4/) for data entry and manipulation. 
