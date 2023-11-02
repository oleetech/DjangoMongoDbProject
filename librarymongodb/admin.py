from django.contrib import admin

from .models import Author, Book, Member, Loan, Stockbook, Reservation, User

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Loan)
admin.site.register(Stockbook)
admin.site.register(Reservation)
admin.site.register(User)
