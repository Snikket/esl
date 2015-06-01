from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render_to_response

def plumeria(request):
    template = loader.get_template('plumeria.html')
    context = RequestContext (request, {})
    return HttpResponse(template.render(context))

def signup(request):
  template = loader.get_template('plumeria.html')
  context = RequestContext(request)
  if request.method == 'POST':
    first_name = request.POST['form-first-name']
    last_name = request.POST['form-last-name']
    email = request.POST.get('form-email')
    message = request.POST.get('form-message')
    send_mail('Student Query from Plumeria', "First Name:"+
      		first_name+"\nLast Name:"+
       		last_name+"\nEmail:"+
       		str(email)+"\nMessage:"+
       		str(message), str(email),['erato.nicolaou@outlook.com'], fail_silently=False)
    return render_to_response('plumeria.html', {'emailed':True}, context)
