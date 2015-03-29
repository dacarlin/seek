from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from app.models import DataEntry, DataEntryForm, Entry

def adam(request):
  if request.method == 'POST':
    form = DataEntryForm(request.POST)
    if form.is_valid():
      analyses = form.process()
      return render(request, 'app/preview.html', { 'analyses': analyses, 'form': form, } )
    else:
      return render(request, 'app/cookbook.html', { 'form': form, } )
  else:
    form = DataEntryForm()
    return render(request, 'app/cookbook.html', {'form': form} )

def thanks(request):
  if request.method == 'POST':
    form = DataEntryForm(request.POST)
    
    if form.is_valid():
      analyses = form.process() # dict analyses = form.process( self )
      
      # process the form before saving 
      for sample, dic in analyses.items():
        entry = Entry()
        entry.mutant = sample
        entry.mm = dic['mm_plot']
        entry.lin = dic['linear_plot']
        entry.__dict__.update( analyses[sample] )
        entry.save()      
      return render(request, 'app/thanks.html', { 'analyses': analyses, 'form': form, } )
    
    else: # form isn't valid
      # why? bad password? 
      return render(request, 'app/error.html', { 'form': form, } )
      
  else:
    return redirect(index) # Why redirect to home here? 

def browse(request):
  # clearly this could get a lot better
  
  # get all Entry objects and order by newest first 
  entry_list = Entry.objects.all().order_by('-date')
  
  # pass to the template browse.html as a dict 
  return render( request, 'app/browse.html', { 'entry_list': entry_list } )
  # I guess django.shortcuts.render( object request, path template, dict stuff for template )

def index(request):
  # should serve these as flat HTML from /static/
  return render( request, 'app/index.html' )

def help(request):
  return render( request, 'app/help.html' )
