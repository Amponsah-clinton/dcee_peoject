from django.db import models
from django.contrib.auth.models import User

class PDFDocument(models.Model):
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    
class QuestionAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} asked: {self.question}"
    
    class Meta:
        unique_together = ('user', 'question')

        
from django.utils import timezone
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_answer = models.ForeignKey(QuestionAnswer, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10, default=None)  
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.user.username} voted on {self.question_answer.id} as {self.vote_type}"

