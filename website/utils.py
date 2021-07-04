from django.utils.text import slugify
import random
import string

def generate_random_string(N): 
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    return res

def generate_slug(text):
    new_slug = slugify(text)
    from .models import Blog
    if Blog.objects.filter(slug=new_slug).first():
        new_slug = generate_slug(text+ generate_random_string(5))

    return new_slug