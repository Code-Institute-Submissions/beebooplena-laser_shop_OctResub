from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Item


def all_items(request):
    """ This code is borrowed from boutique
    Ado project.
    A view to show all items, including search queries """

    items = Item.objects.all()

    query = None

    if request.GET:
        if 's' in request.GET:
            query = request.GET['s']
            if not query:
                messages.error(request,
                               "You didn`t write any search words.")
                return redirect(reverse('items'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            items = items.filter(queries)
    context = {
        'items': items,
        'search_items': query,
    }

    return render(request, 'items/items.html', context)


def item_detail(request, item_id):
    """ A view to be able to show one product and it`s details"""

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'items/item_detail.html', context)
