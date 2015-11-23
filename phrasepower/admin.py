from django.contrib import admin
from phrasepower.models import Phrase, Language, Match

# Register your models here.

admin.site.register(Phrase)
admin.site.register(Language)
admin.site.register(Match)

