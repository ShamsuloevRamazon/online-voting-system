from django.db import models

class Election(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Candidate(models.Model):
    name = models.CharField(max_length=50)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

class Vote(models.Model):
    user_id = models.IntegerField()  # Анонимный ID вместо реальных данных
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)