from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import RequestContext, loader

from phrasepower.models import Language, Phrase, Match

# Create your views here.

def index(request):
    # 1st version - Hello, World
    # return HttpResponse("Hello, World. You're at the PhrasePower index.")

    # 2nd version - getting stuff from the DB
    # display all languages and phrases
    # language_list = Language.objects.all()
    # phrase_list = Phrase.objects.all()
    # phrase_output = 'Phrases:   ' + ', -- '.join([p.phrase_alphabet for p in phrase_list])
    # language_output = 'Languages:   ' + ', -- '.join([l.language for l in language_list])
    # output = phrase_output + ' :::::: ' + language_output
    # return HttpResponse(output)

    # 3rd version - using a template
    # phrase_list = Phrase.objects.all()
    # template = loader.get_template('phrasepower/index.html')
    # context = RequestContext(request, {
    #     'phrase_list': phrase_list,
    # })
    # return HttpResponse(template.render(context))

    # 4th version - using render()
    phrase_list = Phrase.objects.all()
    context = {'phrase_list': phrase_list}
    return render(request, 'phrasepower/index.html', context)

def test(request):
    # merely a test
    return HttpResponse("Check..1...2...Testing...Testing...I'm here!!")

# this is similar to the detail view from the tutorial
def showphrase(request, phrase_id): 
    # 1st version - using ..try 'get()' ..except '404'
    # try:
    #     phrase = Phrase.objects.get(pk=phrase_id)
    # except Phrase.DoesNotExist:
    #     raise Http404
    # return render(request, 'phrasepower/phrase.html', {'phrase': phrase})

    # 2nd version - using 'get_object_or_404'

    phrase = get_object_or_404(Phrase, pk=phrase_id)
    return render(request, 'phrasepower/showphrase.html', {'phrase': phrase})

def addphrase(request):
    # ask the user for a new phrase
    # return HttpResponse("Add Phrase...TEST")

    return render(request, 'phrasepower/addphrase.html', )

def submitphrase(request):
    # add a new phrase to the DB

    newphrase = request.POST['newphrase']
    language = request.POST['language']

    # Add a new phrase to the DB - language chosen using numbers input from form (Yuck)- data not validated yet

    p = Phrase(phrase_original=newphrase, phrase_alphabet=newphrase, language_id=language)
    p.save()
    return HttpResponse("Phrase submitted..MAYBE:   " + newphrase)
    
    

    
