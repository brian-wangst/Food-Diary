def navbar_items(request):
    """
    Context processor to include navbar items.
    """
    navbar_items = {}
    if request.user.is_authenticated:
        navbar_items['logout'] = 'authentication:logout'
    else:
        navbar_items['signup'] = 'authentication:signup'
        navbar_items['login'] = 'authentication:login'
    
    print(navbar_items)
    return {"navbar_items": navbar_items}