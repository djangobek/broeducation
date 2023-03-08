from django.db import models

# Create your models here.
class Post(models.Model):
    ism_familya = models.CharField(max_length=200)
    guruhi = models.CharField(max_length=200)
    umumiy_bali  = models.IntegerField()
    choices1 = (
        ("Passed", "O`tdi"),
        ("failed","O`ta olmadi")
    )
    testda_ishtirok_etishi= models.CharField(
        max_length= 6,
        choices = choices1,
        default = "O`tdi"
    )
    exams = (
        ("kunlik imtihon", "kunlik imtihon"),
        ("haftalik imtihon", "haftalik imtihon"),
        ("Oylik Imtihon", "Oylik Imtihon"),
        ("Yillik Imtihon", "Yillik Imtihon"),
    )
    exam_day= models.CharField(
        max_length= 22 ,
        choices = exams,
        default= 'Haftalik'
    )
    exam_date= models.DateField()

    class Meta:
        ordering = ['-umumiy_bali']
    def __str__(self):
        return str(self.umumiy_bali) + '/' + self.ism_familya
