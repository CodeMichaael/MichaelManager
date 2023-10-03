from django.db import models

class ConnectionManager(models.Model):
    connection_id = models.CharField(max_length=36)
    user_id = models.IntegerField()
    to_computer_id = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class UserConnection(models.Model):
    connection_id = models.CharField(max_length=36)
    user_id = models.IntegerField()
    request = models.TextField() 

class ConnectionRequest(models.Model):
    task = models.TextField()
    user_id = models.IntegerField()
    connection_id = models.CharField(max_length=36)
    timestamp = models.DateTimeField(auto_now_add=True)



