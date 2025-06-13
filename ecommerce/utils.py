def search(request, obj):
    search_query = request.GET.get('q', '')
    if search_query:
        obj = obj.filter(name__icontains=search_query)
        return obj
    return obj