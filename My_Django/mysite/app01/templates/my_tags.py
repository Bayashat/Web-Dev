from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register的名字是固定的, 不可以改变

##              1) 自定义标签
@register.simple_tag  # 装饰器, 用来定制标签
def mul(v1, v2, v3): # 定义了一个乘法的标签
    return v1 * v2 * v3 


@register.simple_tag
def my_input(v1, v2):
    temp_html = '''<div class="input-group mb-3">
                        <span class="input-group-text" id="%s">@</span>
                        <input type="text" class="form-control" placeholder="%s" aria-label="Username" />
                    </div>''' %(v1,v2)
    return mark_safe(temp_html)

##              2) 自定义过滤器
@register.filter  
def my_filter(v1, v2):  # 装饰器参数最多为2个
    return v1 * v2