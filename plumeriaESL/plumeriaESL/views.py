from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def plumeria(request):
    template = loader.get_template('plumeria.html')
    context = RequestContext (request, {})
    return HttpResponse(template.render(context))

def signup(request):
	if request.method == 'POST':
		first_name = request.POST['form-first-name']
       	last_name = request.POST['form-last-name']
       	email = request.POST.get('form-email')
       	message = request.POST.get('form-message')
       	print 
       	send_mail('Student Query from Plumeria', "First Name:"+
       		first_name+"\nLast Name:"+
       		last_name+"\nEmail:"+
       		str(email)+"\nMessage:"+
       		str(message), str(email),
    ['mamas.nicolaou@outlook.com'], fail_silently=False)
	return HttpResponse(status=200)