from django.shortcuts import render, redirect
from models import Book, Author
from ..reviews.models import Review
from ..login_registration.models import User

def index(request):
	if not 'logged_in' in request.session:
		return redirect('user_signin')
	reviews = Review.objects.all().order_by('-created_at')[:3]
	books_to_exclude = [review.book.title for review in reviews]
	books = Book.objects.all().exclude(title__in=books_to_exclude)
	context = {
		'reviews': reviews,
		'books': books
	}
	return render(request, 'books/index.html', context)

def new(request):
	if not 'logged_in' in request.session:
		return redirect('user_signin')
	authors = Author.objects.all()
	context = {'authors':authors}
	return render(request, 'books/new.html', context)

def create(request):
	# extract out complete list for author since can have multiple input fields
	valueList = request.POST.getlist('author')
	# create new author or just retrieve author if already exists
	if valueList[0] == '':
		newAuthor = Author(name = valueList[1])
		newAuthor.save()
		book_author = newAuthor
	else:
		book_author = Author.objects.get(id=valueList[0])
	newBook = Book(title = request.POST['title'], author = book_author)
	newBook.save()
	reviewed_book = Book.objects.get(id=newBook.id)
	review_creator = User.objects.get(id=request.session['logged_in'])
	review = {
		'content': request.POST['review'],
		'rating': request.POST['rating'],
		'book': reviewed_book,
		'reviewer': review_creator
	}
	newReview = Review(**review)
	newReview.save()
	return redirect('books_show', id=newBook.id)

def show(request, id):
	if not 'logged_in' in request.session:
		return redirect('user_signin')
	book = Book.objects.get(id=id)
	context = {'book':book}
	return render(request, 'books/show.html', context)