from django import template

register=template.Library()

@register.filter()
def swap(data):
    return data.swapcase()



@register.filter()
def remove(data,arg):
    return data.replace(arg,'')


@register.filter()
def mdswap(data):
    l=data.split()
    res=[]
    for i in range(len(l)):
        if i==0 or i==-1:
            res.append(l[i])
        else:
            res.append(l[i].lower())
    
    return ' '.join(res)

@register.filter()
def counting(data,sub):

    c=0
    for i in range(len(data)):
        if data[i:i+len(sub)]==sub:
            c+=1
    return c