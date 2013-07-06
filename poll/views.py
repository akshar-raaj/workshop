# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.core.urlresolvers import reverse

from poll.models import Poll, Choice


def index(request):
    polls_list = Poll.objects.all()
    return render(request, "index.html", {'polls': polls_list})

def detail(request, poll_id):
    p = Poll.objects.get(id=poll_id)
    return render(request, 'detail.html', {'poll': p})

@require_POST
def vote(request, poll_id):
    p = Poll.objects.get(id=poll_id)
    selected_choice = request.POST['ch']
    c = p.choice_set.get(id=selected_choice)
    c.votes = c.votes + 1
    c.save()
    redirect_url = reverse('result_of_polls', args=[p.id])
    print redirect_url
    return HttpResponseRedirect(redirect_url)


def result(request, poll_id):
    p = Poll.objects.get(id=poll_id)
    return render(request, "result.html", {'poll': p})
