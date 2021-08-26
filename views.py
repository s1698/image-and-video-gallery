from django.shortcuts import render
def library(request):
    # list out objects 
    # could be search
    qs = None
    template_name = 'Library/library.html'
    context = {'object_list': qs}
    return render(request, template_name, context) 

# Create your views here.
