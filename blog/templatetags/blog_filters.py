from django import template
register=template.Library()

@register.filter(name='leni')
def leni(arr):
    if len(list(arr.all())) ==0:
        return f'0 Likes'
    else:
        num=len(list(arr.all()))-1
        return f'and {num} others'
    

@register.filter(name='first_person')
def first_person(arr):

    arr2=list(arr.all())
    if len(arr2)!=0:
        return f'{arr2[0].first_name} {arr2[0].last_name}'
    else:
        return " "