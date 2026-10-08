from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import LostFoundItem
from .forms import LostFoundItemForm, RegisterForm


# =========================
# HOME PAGE
# =========================
def home(request):
    query = request.GET.get('q', '')
    item_type = request.GET.get('type', '')

    items = LostFoundItem.objects.all().order_by('-created_at')

    if query:
        items = items.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query)
        )

    if item_type in ['Lost', 'Found']:
        items = items.filter(item_type=item_type)

    return render(
        request,
        'campusapp/home.html',
        {
            'items': items,
            'query': query,
            'item_type': item_type,
        }
    )


# =========================
# REPORT ITEM
# =========================
@login_required(login_url='/login/')
def item_create(request):

    if request.method == 'POST':
        form = LostFoundItemForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()

            return redirect('home')

    else:
        form = LostFoundItemForm()

    return render(
        request,
        'campusapp/item_form.html',
        {
            'form': form,
            'title': 'Report Lost / Found Item',
        }
    )


# =========================
# ITEM DETAILS
# =========================
def item_detail(request, pk):

    item = get_object_or_404(
        LostFoundItem,
        pk=pk
    )

    return render(
        request,
        'campusapp/item_detail.html',
        {
            'item': item,
        }
    )


# =========================
# EDIT ITEM
# =========================
@login_required(login_url='/login/')
def item_update(request, pk):

    item = get_object_or_404(
        LostFoundItem,
        pk=pk
    )

    if request.method == 'POST':

        form = LostFoundItemForm(
            request.POST,
            request.FILES,
            instance=item
        )

        if form.is_valid():
            form.save()

            return redirect(
                'item_detail',
                pk=item.pk
            )

    else:
        form = LostFoundItemForm(
            instance=item
        )

    return render(
        request,
        'campusapp/item_form.html',
        {
            'form': form,
            'title': 'Edit Item',
        }
    )


# =========================
# DELETE ITEM
# =========================
@login_required(login_url='/login/')
def item_delete(request, pk):

    item = get_object_or_404(
        LostFoundItem,
        pk=pk
    )

    if request.method == 'POST':
        item.delete()
        return redirect('home')

    return render(
        request,
        'campusapp/item_confirm_delete.html',
        {
            'item': item,
        }
    )


# =========================
# REGISTER
# =========================
def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(
                request,
                user
            )

            return redirect('home')

    else:
        form = RegisterForm()

    return render(
        request,
        'campusapp/register.html',
        {
            'form': form,
        }
    )


# =========================
# LOGIN
# =========================
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            return redirect('home')

        return render(
            request,
            'campusapp/login.html',
            {
                'error': 'Invalid username or password.'
            }
        )

    return render(
        request,
        'campusapp/login.html'
    )


# =========================
# LOGOUT
# =========================
def logout_view(request):

    logout(request)

    return redirect('home')