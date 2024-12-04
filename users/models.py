from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserChannelPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associates with user
    channel_name = models.CharField(max_length=255)
    channel_url = models.URLField()
    channel_score = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)  # Tracks when the entry was created

    def __str__(self):
        return f"{self.user.username} - {self.channel_name}"



from django.db import models

class CsvData(models.Model):
    user_id = models.IntegerField()  # Example of an integer field
    ch_id = models.IntegerField()  # Example of an integer field
    score = models.FloatField()  # Example of a float field
    created_at = models.DateTimeField(auto_now_add=True)



class name_link_chan(models.Model):
    ch_id=models.IntegerField()
    ch_name=models.CharField(max_length=255)
    ch_link=models.CharField(max_length=255)

    reated_at = models.DateTimeField(auto_now_add=True)


from django.db import models

class Channel(models.Model):
    channel_id = models.IntegerField(primary_key=True)  # Unique identifier
    channel_name = models.CharField(max_length=255)     # Channel name
    channel_url = models.URLField()                    # Channel URL

    def __str__(self):
        return self.channel_name