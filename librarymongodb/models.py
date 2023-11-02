from django.db import models

# Author model
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} by {self.author}"

# Member model
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Loan model
class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"Loan of {self.book.title} to {self.member.name}"

# Stockbook model
class Stockbook(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Stockbook record for {self.book.title}"

# Reservation model
class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default='pending')

    def __str__(self):
        return f"Reservation of {self.book.title} by {self.member.name}"

# User model
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
