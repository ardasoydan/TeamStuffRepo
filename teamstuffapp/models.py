from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.


    

class TeamStuffUser(models.Model):

    USER_TYPE_CHOICES = (
        ('PLR', 'Player'),
        ('MAN', 'Manager'),
        ('PAR', 'Parent'),
)
    user= models.OneToOneField(User)
    birth_date = models.DateField(auto_now = False, auto_now_add = False)
    user_type = models.CharField(max_length = 3, choices = USER_TYPE_CHOICES,
                                 default = 'MAN')
    def __unicode__(self):
        return unicode(self.username)

class Team(models.Model):
    player = models.ForeignKey(TeamStuffUser)
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
