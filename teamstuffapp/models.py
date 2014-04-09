from django.db import models
from django import forms


# Create your models here.


    

class User(models.Model):

    USER_TYPE_CHOICES = (
        ('PLR', 'Player'),
        ('MAN', 'Manager'),
        ('PAR', 'Parent'),
)

    user_name = models.CharField(max_length = 50)
    email = forms.EmailField()
    password =models.CharField(max_length = 20)
    birth_date = models.DateTimeField('birth date')
    user_type = models.CharField(max_length = 3, choices = USER_TYPE_CHOICES,
                                 default = 'MAN')
    def __unicode__(self):
        return unicode(self.user_name)

class Team(models.Model):
    user = models.ForeignKey(User)
    team_name = models.CharField(max_length = 50)
    sport = models.CharField(max_length = 20)
    club_name = models.CharField(max_length = 40)

    def __unicode__(self):
        return unicode(self.team_name)
    
class TeamEvent(models.Model):
    
    def __unicode__(self):
        return unicode(self.training_session)

    team = models.ForeignKey(Team)
    training_session = models.CharField(max_length = 200)
    start_date = models.DateTimeField('training starts')
    end_date = models.DateTimeField('training ends')
    takes_place_in = models.CharField(max_length = 200)

    def upcoming_trainings(self):
        now = timezone.now()
        return now + datetime.timedelta(days = 1) >= self.start_date > now
