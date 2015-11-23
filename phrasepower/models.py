from django.db import models

# Create your models here.

class Language(models.Model):
    language = models.CharField(max_length=100) # e.g. "English" or "Italian"

    def __unicode__(self):
        return self.language

class Phrase(models.Model):
    phrase_original = models.CharField(max_length=200) # e.g. "Konnichiwa" in Kanji
    phrase_alphabet = models.CharField(max_length=200) # e.g. "Konnichiwa" in Roman Alphabet
    language = models.ForeignKey(Language) # e.g. "Japanese"
    equivalent_phrases = models.ManyToManyField('self', through='Match', symmetrical=False, related_name='equivalent_to+') #Facebook-style relationship

    #equivalent_phrases = models.ManyToManyField('self', through='Match', symmetrical=False, related_name='equivalent_to') 
    #tags = some field for tags...e.g. Greeting, Casual, Formal, BBQ, Expressing Surprise, Agreement,...
 
    # how can equivalent_phrases be displayed on the admin page?

    def __unicode__(self):
        return self.phrase_alphabet

    def add_match(self, phrase, notes): #this works!
        match, created = Match.objects.get_or_create(phrase1=self, phrase2=phrase, notes=notes)
        return match

    def remove_match(self, phrase):
        Match.objects.filter(phrase1=self, phrase2=phrase).delete()
        return

    def get_matches(self): #this works!
        return self.equivalent_phrases.filter(phrase2__phrase1=self)

    def get_equivalent_to(self):
        return self.equivalent_to.filter(phrase1__phrase2=self) # is this method a waste of time? 

class Match(models.Model):
    phrase1 = models.ForeignKey(Phrase, related_name='phrase1')
    phrase2 = models.ForeignKey(Phrase, related_name='phrase2')
    notes = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "Matches"

#    def __unicode__(self):
#        return phrase1__phrase_alphabet + " -- " + phrase2__phrase_alphabet



