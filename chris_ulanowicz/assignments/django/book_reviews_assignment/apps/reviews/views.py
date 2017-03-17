from django.shortcuts import render, redirect
from models import Review
from ..books.models import Book
from ..login_registration.models import User

def index(request):
	pass

def destroy(request, id):
	print id
	review = Review.objects.get(id=id)
	book_id = review.book.id
	review.delete()
	return redirect('books_show', id=book_id)

def create(request):
	print request.POST.__dict__
	book = Book.objects.get(id=request.POST['book_id'])
	user = User.objects.get(id=request.session['logged_in'])
	reviewData = {
		'content': request.POST['review'],
		'rating': request.POST['rating'],
		'book': book,
		'reviewer': user
	}
	newReview = Review(**reviewData)
	newReview.save()
	return redirect('books_show', id=book.id)