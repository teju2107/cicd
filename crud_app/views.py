from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm


from django.db.models import Q
from django.shortcuts import render
from .models import Item

def item_list(request):
    query = request.GET.get('q')  # Get the query from the search box

    if query:
        # Filter items based on the query. You can search across multiple fields.
        items = Item.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        # If there's no query, show all items.
        items = Item.objects.all()

    # Calculate the total based on a specific field, e.g., price
    total = sum(item.price for item in items)  # Ensure to adjust 'price' to the appropriate field name

    return render(request, 'crud_app/item_list.html', {'items': items, 'query': query, 'total': total})

# Create (and Update)
def create_or_edit_item(request, id=None):
    if id:
        item = get_object_or_404(Item, id=id)
    else:
        item = None

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    
    return render(request, 'crud_app/item_form.html', {'form': form})

# # Read (List)
# def item_list(request):
#     items = Item.objects.all()
#     return render(request, 'crud_app/item_list.html', {'items': items})

# Delete
def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    
    return render(request, 'crud_app/confirm_delete.html', {'item': item})
