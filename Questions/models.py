from django.db import models

# Create your models here.
class Questions_Crud(models.Model):
    
    question =models.CharField(max_length=500)
    
    option_a = models.CharField(max_length=200)
    
    option_b = models.CharField(max_length=200)

    option_c = models.CharField(max_length=200)

    option_d = models.CharField(max_length=200)

    correct_answer = models.CharField(max_length=500)
    
    
    
class AnswerSubmissionDB(models.Model):
    
    student_name = models.CharField(max_length=200)
    
    question_id = models.IntegerField()
    
    selected_answer = models.CharField(max_length=200)
    
    submitted_at = models.DateTimeField(auto_now_add=True)