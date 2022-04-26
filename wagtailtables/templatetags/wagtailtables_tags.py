from django import template
import json

register = template.Library()

def col_to_num(col_str):
    """ Convert base26 column string to number. """
    expn = 0
    col_num = 0
    for char in reversed(col_str):
        col_num += (ord(char) - ord('A')+1) * (26 ** expn)
        expn += 1

    return col_num

def colrowsplit(s):
    head = s.rstrip('0123456789')
    tail = s[len(head):]
    return head, tail

@register.simple_tag
def get_table_data(table_data):
    t_data = json.loads(table_data)
    t_styles = []
    for row in t_data["data"]:
        t_styles.append([None]*len(row))

    if t_data["style"] == '':
        t_data["style"] = {}
    for pos in t_data["style"].keys():
        col, row = colrowsplit(pos)
        col2num = col_to_num(col)
        t_styles[int(row)-1][col2num-1] = t_data["style"][pos]

    return {'data': t_data["data"], 'styles': t_styles}

@register.simple_tag
def get_styles(t_styles, row, col):
    return t_styles[row][col]