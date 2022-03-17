from django.db import models

# Create your models here.


# create a model named conference
class Conference(models.Model):
    # define the fields for the model
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


# create a model named talk
class Talk(models.Model):
    # define the fields for the model
    title = models.CharField(max_length=100)
    description = models.TextField()
    # add duration field
    duration = models.IntegerField()
    # add startdatetime field
    startdatetime = models.DateTimeField()
    # add speakers
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# create a model named CustomUser
class CustomUser(models.Model):
    # create fields named username and email
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


# create a model named speakersList
class SpeakersList(models.Model):
    # create a foreign key to talk
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
    #  create a list of CustomUser objects
    speakers = models.ManyToManyField(CustomUser)

    def __str__(self):
        #  return the talk title
        return self.talk.title


# create a model named ParticipantsList
class ParticipantsList(models.Model):
    # create a foreign key to talk
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
    #  create a list of CustomUser objects
    participants = models.ManyToManyField(CustomUser)

    def __str__(self):
        #  return the talk title
        return self.talk.title
