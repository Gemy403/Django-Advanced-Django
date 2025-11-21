from django import template

register = template.Library()

@register.filter
def format_price(value):
    return f'$ {value}'


@register.filter
def average_rate(reviews):
    total = sum((review.rate for review in reviews))
    count = len(reviews)
    if count > 0 :
        avg = round(total / count,2)
        return avg
    else:
        return 0