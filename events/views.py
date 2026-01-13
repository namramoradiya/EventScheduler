from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm,RegisterUser
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required



@login_required
def event_list(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'events/event_list.html', {'events': events})


@login_required
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()

    return render(request, 'events/event_form.html', {'form': form})


@login_required
def event_update(request, id):
    event = get_object_or_404(Event, id=id, user=request.user)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)

    return render(request, 'events/event_form.html', {'form': form})


@login_required
def event_delete(request, id):
    event = get_object_or_404(Event, id=id, user=request.user)

    if request.method == "POST":
        event.delete()
        return redirect('event_list')

    return render(request, 'events/event_confirm_delete.html', {'event': event})


def register(request):
    if request.method=='POST':
        form=RegisterUser(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('event_list')
    else:
        form=RegisterUser()

    return render(request,'registration/register.html',{'form':form})