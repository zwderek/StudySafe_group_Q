from django.db import models

class HKU_member(models.Model):
    hku_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.hku_id} {self.name}'
    
    class Meta:
        verbose_name = 'HKU member'
        verbose_name_plural = 'HKU members'

class Venue(models.Model):
    VENUE_TYPES = (
        ('LT', 'Lecture Theatre'),
        ('CR', 'Classroom'),
        ('TR', 'Tutorial Room'),
    )
    venue_code = models.CharField(max_length=20, primary_key=True)
    location = models.CharField(max_length=150)
    type = models.CharField(max_length=2, choices=VENUE_TYPES)
    capacity = models.IntegerField()

    def __str__(self):
        return self.venue_code

class EntryExit(models.Model):
    member = models.ForeignKey(HKU_member, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    enter_time = models.DateTimeField()
    exit_time = models.DateTimeField()

    def __str__(self):
        return f'{self.member} {self.venue}'

    class Meta:
        verbose_name = "EntryExit"
        verbose_name_plural = 'EntriesExits'
