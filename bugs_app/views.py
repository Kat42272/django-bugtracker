from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


from .models import MyUser, Ticket
from .forms import LoginForm, AddTicketForm

# Received assistance from Detrich Schilling
# Detrich also gave me a link to Stackoverflow to help with a 
# model issue https://stackoverflow.com/questions/543377/how-can-i-have-two-foreign-keys-to-the-same-model-in-django

def index(request):
  new_ticket = Ticket.objects.filter(current_ticket_process='NEW')
  in_progress_ticket = Ticket.objects.filter(current_ticket_process="IN PROGRESS")
  done_ticket = Ticket.objects.filter(current_ticket_process='DONE')
  invalid_ticket = Ticket.objects.filter(current_ticket_process='INVALID')
  return render(
    request,
    'index.html',
    {
      'new_ticket': new_ticket,
      'in_progress_ticket': in_progress_ticket,
      'done_ticket': done_ticket,
      'invalid_ticket': invalid_ticket,
    }
  )



def user_details(request, username):
  current_user = MyUser.objects.filter(username=username).first()
  filed_user = Ticket.objects.filter(filed_by=current_user)
  assigned_user = Ticket.objects.filter(assigned_to=username)
  completed_user = Ticket.objects.filter(completed_by=username)
  return render(
    request,
    'user_details.html',
    {
      'current_user': current_user,
      'filed_tickets': filed_user,
      'assigned_tickets': assigned_user,
      'completed_tickets': completed_user,
    }
  )


def ticket_detail(request, ticket_id):
  current_ticket = Ticket.objects.filter(id=ticket_id).first()
  return render(
    request,
    'ticket.html',
    {
      'ticket': current_ticket,
    }
  )


@login_required
def ticket_submit_view(request):
  if request.method == 'POST':
    form = AddTicketForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      new_ticket = Ticket.objects.create(
        title=data.get('title'),
        description=data.get('description'),
        filed_user=request.user,
        assigned_user=None,
      )
      return HttpResponseRedirect(reverse('home'))
  form = AddTicketForm()
  return render(request, 'generic_form.html', {'form': form,})


@login_required
def ticket_edit_view(request, ticket_id):
  ticket = Ticket.objects.get(id=ticket_id)
  if request.method == "POST":
    form = AddTicketForm(request.POST)
    if form.is_valid():
      ticket_data = form.cleaned_data
      ticket.title = ticket_data['title']
      ticket.description = ticket_data['description']
      ticket.save()
    return HttpResponseRedirect(reverse('ticket', args=[ticket.id]))
  data = {
    'title': ticket.title,
    'description': ticket.description,
  }
  form = AddTicketForm(initial=data)
  return render(request, 'generic_form.html', {'form': form})


@login_required
def ticket_in_progress(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id).first()
    ticket.assigned_user = request.filed_user.username
    ticket.completed_user = 'NONE'
    ticket.current_ticket_process = 'IN PROGRESS'
    ticket.save()
    return HttpResponseRedirect(reverse('ticket', args=[ticket.id]))

@login_required
def ticket_completed(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id).first()
    ticket.current_ticket_process = 'DONE'
    ticket.completed_user = ticket.assigned_user
    ticket.assigned_user = None
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def ticket_invalid(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.current_ticket_process = 'INVALID'
    ticket.assigned_user = None
    ticket.completed_user = None
    ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      user = authenticate(
        request,
        username=data.get('username'),
        password=data.get('password')
      )
      if user:
        login(request, user)
        return HttpResponseRedirect(request.GET.get('next', reverse('home')))
  form = LoginForm()
  return render(request, 'generic_form.html', {'form': form})

def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse('home'))
