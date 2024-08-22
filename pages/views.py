from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import datetime
from django.contrib import messages
from .models import *


def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about_us.html')

def error_404(request):
    return render(request, 'pages/404_error.html')

def add_book(request):
    if request.method == 'POST':
        Book_Name = request.POST.get('Book_Name')    
        Author = request.POST.get('Author')    
        Category = request.POST.get('Category')    
        Description = request.POST.get('Description')
        Choose_File = request.FILES.get('Choose_File')
      
        data = Book(
            title=Book_Name,
            author=Author,
            category=Category,
            description=Description,
            cover_photo=Choose_File,
            isAvailable = True,
        )
        data.save()
        return redirect('view_books')
    
    return render(request, 'pages/add_book.html')

def admin_book_details(request, book_id):
    if request.method == 'POST':
       
        book_id = request.POST.get('book_id')
        try:
            book = Book.objects.get(pk=book_id)
            book.delete()
            messages.success(request, 'Book has been deleted successfully.')
            return JsonResponse({'success': True})
        except Book.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Book not found'})

    book = get_object_or_404(Book, id = book_id)  
    return render(request, 'pages/admin_book_details.html', {'book': book})


def admin_profile(request):
    return render(request, 'pages/admin_profile.html')


def contact_us(request):
    return render(request, 'pages/contact_us.html')

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book_name = request.POST.get('BookName')
        author = request.POST.get('Author')
        category = request.POST.get('Category')
        description = request.POST.get('Description')

        if  book_name=='' or  author=='' or  category=='' or  description=='':
            return render (request, 'pages/edit_book.html', {'book': book, 'error_message': 'Fields Cannot be Empty!'})
             

        else:    
            book.title = book_name
            book.author = author
            book.category = category
            book.description = description
            book.save()

            return redirect('admin_book_details', book.id )  
    
    return render(request, 'pages/edit_book.html', {'book': book})


from django.shortcuts import render, redirect
from .models import User

def edit_profile(request):
    if 'user_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        FirstName = request.POST.get('FirstName')    
        LastName = request.POST.get('LastName')    
        UserMail = request.POST.get('UserMail')    
        UserPass = request.POST.get('UserPass')

        # Strip and clean the input
        UserPass = str(UserPass).strip()
        UserMail = str(UserMail).strip().lower()

        # Validation
        if FirstName == '' or LastName == '' or UserMail == '' or UserPass == '':
            return render(request, 'pages/edit_profile.html', {'error_message': 'Fields Cannot be Empty!', 'first_name': FirstName, 'last_name': LastName, 'mail': UserMail})
        elif len(UserPass) < 8:
            return render(request, 'pages/edit_profile.html', {'error_message': 'Password Should Consist of 8 or more characters!', 'first_name': FirstName, 'last_name': LastName, 'mail': UserMail})
        else:
            user_id = request.session['user_id']
            try:
                user = User.objects.get(id=user_id)
                
                # Update user details
                user.FirstName = FirstName
                user.LastName = LastName
                user.UserMail = UserMail
                user.UserPass = UserPass
                user.save()
                
                # Update session data
                request.session['FirstName'] = user.FirstName
                request.session['LastName'] = user.LastName
                request.session['UserMail'] = user.UserMail
                request.session['UserPass'] = user.UserPass

                if user.UserRole == 'admin':
                    return redirect('admin_profile')  # Use URL names instead of direct function calls
                else:
                    return redirect('user_profile')  # Use URL names instead of direct function calls
            except User.DoesNotExist:
                return redirect('login')  # Handle case where user does not exist

    else:
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        return render(request, 'pages/edit_profile.html', {
            'first_name': user.FirstName,
            'last_name': user.LastName,
            'mail': user.UserMail,
        })

def library_search(request):
    search_by = request.GET.get('search_by', 'title')
    search_term = request.GET.get('s', '')

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Handle AJAX request
        if search_by == 'title':
            books = Book.objects.filter(title__icontains=search_term)
        elif search_by == 'author':
            books = Book.objects.filter(author__icontains=search_term)
        elif search_by == 'category':
            books = Book.objects.filter(category__icontains=search_term)
        else:
            books = Book.objects.none()

        book_data = [
            {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "category": book.category,
                "cover_photo": book.cover_photo.url
            }
            for book in books
        ]
        return JsonResponse({"books": book_data})
    else:
       
        if search_by == 'title':
            books = Book.objects.filter(title__icontains=search_term)
        elif search_by == 'author':
            books = Book.objects.filter(author__icontains=search_term)
        elif search_by == 'category':
            books = Book.objects.filter(category__icontains=search_term)
        else:
            books = Book.objects.none()

        context = {
            "books": books
        }
        return render(request, "pages/library_search.html", context)


def login(request):
    if request.method == 'POST':
        email = request.POST.get('Email address')
        password = request.POST.get('Password')

        try:
            user = User.objects.get(UserMail = email)
            if user.UserPass == password:
                request.session['user_id'] = user.id
                request.session['user_role'] = user.UserRole
                request.session['FirstName'] = user.FirstName
                request.session['LastName'] = user.LastName
                request.session['UserMail'] = user.UserMail
                request.session['UserPass'] = user.UserPass
                
                return redirect('index')
            else:
                 return render(request, 'pages/login.html', {'error_message':'Wrong Credentials'})
        except User.DoesNotExist:
                 return render(request, 'pages/login.html', {'error_message':'Wrong Credentials'})       
    return render(request, 'pages/login.html')

def logout_confirmation(request):
    return render(request, 'pages/logout_confirmation.html')


def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')


def sign_up(request):
    if request.method=='POST':
      
        FirstName = request.POST.get('FirstName')    
        LastName = request.POST.get('LastName')    
        UserMail = request.POST.get('UserMail')    
        UserPass = request.POST.get('UserPass')
        ConfirmPass = request.POST.get('ConfirmPass')
        UserRole = request.POST.get('is_admin')  

        UserPass=str(UserPass).strip()
        ConfirmPass = str(ConfirmPass).strip() 
        UserMail = str(UserMail).strip().lower()

        if  FirstName =='' or  LastName =='' or UserMail =='' or UserPass=='':
            return render (request, 'pages/sign_up.html', {'error_message':'Fields Cannot be Empty!'}) 
        elif UserRole not in ['admin', 'reader']:
            return render (request, 'pages/sign_up.html', {'error_message':'Please Choose A Role!'}) 
        elif len(UserPass) < 8:
            return render (request, 'pages/sign_up.html', {'error_message':'Password Should Consist of 8 or more characters!'}) 

        elif ConfirmPass != UserPass:
             return render (request, 'pages/sign_up.html', {'error_message':'Passwords Do Not Match!'})
        else:
            data= User(FirstName = FirstName, LastName=LastName, UserMail =UserMail, UserPass =UserPass,UserRole =UserRole)
            data.save()
            return redirect('login')
        
    return render(request, 'pages/sign_up.html')


def user_book_details(request, user_id, book_id):
    try:
        borrowed_book = BorrowedBook.objects.get(user_id=user_id, book_id=book_id, Borrowing_Status = True)
    except BorrowedBook.DoesNotExist:
        borrowed_book = None

    book = get_object_or_404(Book, pk=book_id)
    user = get_object_or_404(User, pk=user_id)

    if request.method == "POST":
        due_date_str = request.POST.get('date')
        
        if not due_date_str:
            return render(request, 'pages/user_book_details.html', {
                'borrowed_book': borrowed_book,
                'book': book,
                'error': 'This Field Cannot Be Empty!'
            })
        
        try:
            date_input = datetime.strptime(due_date_str, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'pages/user_book_details.html', {
                'borrowed_book': borrowed_book,
                'book': book,
                'error': 'Invalid Date!'
            })
        
        if date_input <= timezone.now().date():
            return render(request, 'pages/user_book_details.html', {
                'borrowed_book': borrowed_book,
                'book': book,
                'error': 'Invalid Date!'
            })
        
        if not book.isAvailable:
            return render(request, 'pages/user_book_details.html', {
                'borrowed_book': borrowed_book,
                'book': book,
                'error': 'Book is not available currently!'
            })
        
        # Update book availability and create borrowed book record
        else: 
            book.isAvailable = False
            book.save()

            
            borrowed_book = BorrowedBook(
            user=user,
            book=book,
            start_date=timezone.now().date(),
            due_date=date_input,
            Borrowing_Status=True
            )
            borrowed_book.save()
        
         

    context = {
        'borrowed_book': borrowed_book,
        'book': book
    }

    return render(request, 'pages/user_book_details.html', context)


def user_borrowed_books(request, user_id):
    context = {
        'books' : BorrowedBook.objects.all(),
        'user_id': user_id,
    }

    return render(request, 'pages/user_borrowed_books.html', context)

# return book function

@require_POST
def return_book(request):
    import json
    data = json.loads(request.body)
    book_id = data.get('book_id')
    
    try:
        borrowed_book = BorrowedBook.objects.get(book_id=book_id, Borrowing_Status=True)
        borrowed_book.Borrowing_Status = False
        borrowed_book.save()

        book = borrowed_book.book
        book.isAvailable = True
        book.save()

        return JsonResponse({'success': True})
    except BorrowedBook.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Book not found or already returned'})

def user_profile(request):
    return render(request, 'pages/user_profile.html')

def view_books(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'pages/view_books.html', context)



# logout function
@csrf_exempt
def logout(request):
    if request.method == 'POST':
        request.session.flush()
        return JsonResponse({'status':'loggedout'})
    return JsonResponse({'status':'error'}, status = 400)

