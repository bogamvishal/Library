
from Book.models import ActiveBooksManager, Book
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from datetime import date
from Book.model_enum import Math,Names
from subscribe.views import *


# from subscribe import *
# Create your views here.

# def func(request):
#     return render(request,"base.html")
    # print(request.method)
    # print("Inside View function..")
    # return HttpResponse("Hi...How are you?")
    # return JsonResponse({"name":"Vishal"})


def homepage(request):
    if request.method == "POST":
        data = request.POST
        print("Recieved data from POST: ",data)
        if not data.get("id"):    # for add book record
            print("Add a book...")
            if data["IsPublished"] == "Yes":
                print("published")
                Book.all_books.create(name=data["name"],           # create obj and insert record into table
                qty=data["qty"],
                price=data["price"],
                is_published=True,
                published_date = date.today())
                # b_obj.save()
                # print(b_obj)
            elif data["IsPublished"] == "No":
                print("Not published")
                Book.all_books.create(name=data["name"],
                qty=data["qty"],
                price=data["price"],
                is_published=False)
                # b_obj.save()
                # print(b_obj)
            
            return redirect("home")                    # After successful post redirect to same page to insert more records 
        
        elif data.get("id"):                     # for updating a book record
            u_id = data.get("id")
            if data["IsPublished"] == "Yes":
                b = Book.all_books.get(id=u_id)            #first get the book object to be modified
                print("Recieved data for updation:",b)        
                b.qty=data["qty"]
                b.price=data["price"]

                if data["IsPublished"] == "Yes":
                    if b.is_published:
                        pass
                    else:
                        b.is_published = True              # No to Yes change is significant
                        b.published_date = date.today()

                elif data["IsPublished"] == "No":
                    if b.is_published == True:
                        pass
                b.save()  
            return redirect("home")

    else:
        return render(request,template_name="home.html")

def get_book_data(request):
    # books = Book.objects.all()
    books = Book.all_books.all()
    return render(request,template_name="books.html",context={"all_books":books})      #context: always pased as dict

def delete_book(request,id):
    book = Book.all_books.get(id = id)
    book.delete()
    print(id,"delete book id")   
    return redirect("show_books")

def soft_delete_book(request,id):
    book = Book.all_books.get(id = id)
    book.is_deleted = "Y"
    book.save()
    return redirect("show_books")

def update_book(request,id):
    book = Book.all_books.get(id=id)
    return render(request,"home.html",context= {"target_book":book})

def active_books(request):
    # books = Book.objects.filter(is_deleted = 'N')
    active_books = Book.active_books.all()
    return render(request,template_name ="books.html",context= {"all_books":active_books})

def inactive_books(request):
    # books = Book.objects.filter(is_deleted = 'Y')
    inactive_books = Book.inactive_books.all()
    return render(request,template_name ="books.html",context= {"all_books":inactive_books,"book_status" : "InActive"})

def restore_book(request,id):         # Restore a soft deleted book.
    books = Book.all_books.all()
    book = Book.all_books.get(id=id)
    book.is_deleted = "N"
    book.save()
    # return render(request,"books.html",context= {"target_book":book})
    return render(request,template_name="books.html",context={"all_books":books})

