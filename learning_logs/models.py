from django.db import models
from django.contrib.auth.models import User  # connect data submitted by a user to its user

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model): # each entry is associate with the topic learned
    """Something specific learned about a topic"""
    # Entry class inherits from Django's base Model class
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # topic is an instance of an attribute ForeignKey
    # code that connects each entry to a specific topic
    # Foreign key refers to a record in a different database
    text = models.TextField()
    # text is an instance of TextField
    # text is a second attribute of Entry class
    date_added = models.DateTimeField(auto_now_add=True)
    # presents entries in the order they were added

    class Meta:
        """ extra info for managing a model"""
        # w/out verbose_, Django would refer to multiple entries as Entrys
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        # tells Django which info to show when it refers to individual entries
        return self.text[:50] + ("..." if len(self.text) > 50 else "")