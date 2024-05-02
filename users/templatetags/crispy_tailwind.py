from django import template
register = template.Library()

@register.filter(name='tailwindcss')
def tailwindcss(field, classes):
    return field.as_widget(attrs={"class": classes})