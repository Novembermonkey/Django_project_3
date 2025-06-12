from django.core.paginator import Paginator


def pagination(request, obj, per_page = 3):
    paginator = Paginator(obj, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def search(request, obj):
    search_query = request.GET.get('q', '')
    if search_query:
        obj = obj.filter(name__icontains=search_query)
        return obj
    return obj