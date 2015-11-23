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
    #equivalent_phrase = models.ForeignKey(Phrase) -this doesn't work yet
    #equivalent_phrase = models.ForeignKey(self)
  
    def __unicode__(self):
        return self.phrase_alphabet  

# class Match(models.Model):
#    notes = language = models.CharField(max_length=100)
#    phrase1 = models.ForeignKey(Phrase)
#    phrase2 = models.ForeignKey(Phrase)


