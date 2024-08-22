from django.db import models

# Create your models here.
class Book (models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=250)
    author =  models.CharField(max_length=250)
    category =  models.CharField(max_length=250)
    cover_photo = models.ImageField(upload_to="BookCovers")
    description =  models.TextField(max_length=2000)
    isAvailable =  models.BooleanField(default=True)

class User(models.Model):
    def __str__(self):
        return self.FirstName+ " " + self.LastName
    
    roles = (
        ('admin', 'admin'),
             ('reader', 'reader'),
             )

    FirstName =  models.CharField(max_length=250)
    LastName =  models.CharField(max_length=250)
    UserMail =  models.EmailField(unique=True)
    UserPass =  models.CharField(max_length=128)
    UserRole =  models.CharField(max_length=10, choices=roles, default='reader')

class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    due_date = models.DateField()
    Borrowing_Status =models.BooleanField()
    def __str__(self):
        return f"{self.book.title} - Borrowed by {self.user.FirstName}"