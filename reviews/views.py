from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from reviews.models import Category, Comment, Product, UserAccount
from reviews.forms import SearchForm, CategoryForm, ProductForm, CommentForm, UserRegistrationForm, Signinform, UserEditForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json, time


def index(request, username = False):

    products        = Product.objects.order_by('-thumbsUp')[:9]
    comments        = Comment.objects.order_by('-backs')[:9]
    context_dict    = {"product_list":products, "comments": comments}

    if username :
        user = User.objects.get(username = username)
        print(user)
        context_dict    = {"product_list":products, "comments": comments, "user": user}

    return render(request, 'reviews/index.html', context_dict )


def product_detail(request, product_slug):
    form    = CommentForm()
    product =""
    try:
        product=Product.objects.get(slug=product_slug)

    except:
        return render(request, 'reviews/details.html')


    comments = Comment.objects.filter( product__name = product.name ).order_by( '-id' )



    context_dict = {"product": product, "comments": comments, "form": form}


    return render(request, 'reviews/details.html', context_dict)


def search_product(request):
    form    = SearchForm()
    result  = {}
    # if request.method == 'POST':
    # Attempt to grab information from the raw form information.
    # Note that we make use of both UserForm and UserProfileForm.
    search_form = SearchForm(data=request.POST)
    # if search_form.is_valid():
        
    query = request.GET['name']
    print(query)
        
    try:
        result = Product.objects.filter(name__istartswith = query)
        print(query)
        print(result)
        

        return render(request, 'reviews/results.html', {'form': form , 'result' : result, 'query': query})

    except:
        return HttpResponseRedirect('/reviews/')
            
            
    return render(request, 'reviews/results.html', {'form': form })


def add_product(request):

    categories = Category.objects.all()
    form       = ProductForm()
    commentform= CommentForm()


    if request.method == 'POST':
        form = ProductForm(request.POST)
        
         # Have we been provided with a valid form?
        if len(request.POST['category'])<1:
            error = 'please fill a category'

            return render(request, 'reviews/add_category.html', {'form': form, 'categories': categories, 'error': error})

        if form.is_valid():

            try:
                newproduct       = Product(name = request.POST['name'], details = request.POST['details'], 
                                    category = Category.objects.get(name = request.POST['category']))

                # Save the new category to the database.
                try: 
                    if request.FILES['image']:
                        newproduct.image = request.FILES['image']
                        newproduct.save()

                except:

                    newproduct.save()
                # Now that the category is saved
                # We could give a confirmation message
                # But since the most recent category added is on the index page
                # Then we can direct the user back to the index page.
                
            except:
                error = 'sorry category does not exist'

                return render(request, 'reviews/add_product.html', {'form': form, 'categories': categories, 'error': error})


            return index(request)

    else:
        # The supplied form contained errors -
        # just print them to the terminal.
        print(form.errors)
    
    return render(request, 'reviews/add_product.html', {'form': form, 'categories':categories, 'commentform':commentform})


def add_comment(request, product_slug, user_id):

    form    = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            newcomment = Comment(title = request.POST['title'], body = request.POST['body'], 
            product = Product.objects.get(slug = product_slug ), comment_product_slug = product_slug, 
            posted_by = (User.objects.get(id = user_id )))
        
        try: 
            if request.FILES['image']:
                newcomment.image = request.FILES['image']
                newcomment.save()
                newproduct = Product.objects.get(slug = product_slug )
                newproduct.comments = newproduct.comments + 1
                newproduct.save()
                return product_detail(request, product_slug)

        except:
            
            newcomment.save()
            newproduct = Product.objects.get(slug = product_slug )
            newproduct.comments = newproduct.comments + 1
            newproduct.save()

            return product_detail(request, product_slug)
     
    return render(request, 'reviews/index.html')


def back_comment(request, comment_id, username):

    newcomment = Comment.objects.get(id = comment_id )

    try:
        if username not in (newcomment.backedBy).split(" "):
            
            newcomment.backs    = newcomment.backs + 1
            newcomment.backedBy = (username + " " + newcomment.backedBy)
            newcomment.save()
    except:
        newcomment.backedBy = username
        newcomment.backs    = newcomment.backs + 1
        newcomment.save()

    print(newcomment.backedBy)
    backs = json.dumps({'backs':newcomment.backs, 'id': newcomment.id})

    return HttpResponse(backs)


def thumbsUp(request,product_slug, username):
    
    newproduct = Product.objects.get(slug = product_slug )
    
    try:
        if username not in (newproduct.thumbsUpBy).split(" "):
            newproduct.thumbsUp = newproduct.thumbsUp + 1
            newproduct.thumbsUpBy = (username + " " + newproduct.thumbsUpBy)
            newproduct.save()
    except:
        newproduct.thumbsUpBy = username
        newproduct.thumbsUp = newproduct.thumbsUp + 1
        newproduct.save()

    print(newproduct.thumbsUpBy)
    like = json.dumps({'like':newproduct.thumbsUp, 'slug': newproduct.slug})

    return HttpResponse(like)


def thumbsDown(request, product_slug, username):
    print("loooooooooooooooooooo",product_slug)

    newproduct            = Product.objects.get(slug = product_slug )
    try:
        if username not in (newproduct.thumbsDownBy).split(" "):
            newproduct.thumbsDown = newproduct.thumbsDown + 1
            newproduct.thumbsDownBy = (username + " " + newproduct.thumbsDownBy)
            newproduct.save()
    except:
        newproduct.thumbsDownBy = username
        newproduct.thumbsDown = newproduct.thumbsDown + 1
        newproduct.save()

    print(newproduct.thumbsDownBy)

    dislike               = json.dumps({'dislike':newproduct.thumbsDown, 'slug': newproduct.slug})

    return HttpResponse(dislike)


def was_added(request):
    timenow    = time.time()
    now        = json.dumps({'time': timenow})
    return HttpResponse(now)


def signup(request):
    form = UserRegistrationForm()
    error = ""
    print("got herre-----------")
    image=""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj     = form.cleaned_data
            username    = userObj['username']
            email       =  userObj['email']
            first_name  =  userObj['first_name']
            last_name   =  userObj['last_name']
            password    =  userObj['password']
        

            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):

                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                user = User.objects.get(username=username)
                user.first_name = first_name
                user.last_name  = last_name

                user.save()
                try: 
                    if request.FILES['image']:
                        image = request.FILES['image']
                        new_uac = UserAccount.objects.create(User=user, image = image, joined = time.time() )
                        new_uac.save()
                        return index(request, user.username)
                except:
                   
                    new_uac = UserAccount.objects.create(User=user, image = "", joined = time.time() )
                    new_uac.save()
                    return index(request, user.username)

            else:
                error ='Looks like a username with that email or password already exists'
                print("Looks like a username with that email or password already exists")
    else:
        form = UserRegistrationForm()

    return render(request, 'reviews/login.html', {'form' : form, "error":[error]})


def signin(request):
    form = Signinform()
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return index(request, user.username)
    return render(request, 'reviews/login.html', {'form' : form})

def profile_view(request, username):

    form = UserRegistrationForm()
    error = ""
    image=""
    userprofile = User.objects.get(username = username)

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            userObj     = form.cleaned_data
            username    = userObj['username']
            email       =  userObj['email']
            first_name  =  userObj['first_name']
            last_name   =  userObj['last_name']

        if not User.objects.filter(email=email).exists():

            userprofile.first_name = first_name
            userprofile.last_name = last_name
            userprofile.email = email

        
            try: 
                if request.FILES['image']:
                    image = request.FILES['image']
                    userprofile.user.image = image
                    userprofile.save()
                    return index(request, user.username)
            except:
                userprofile.save()
            
        else:
            error = "sorry that email address is taken"

    comments= Comment.objects.filter(posted_by = userprofile.id )
      
    context_dict    = { "comments": comments, 'form': form, "error":error}    
    return render(request, 'reviews/profile_view.html', context_dict)

def edit_profile_view():
    form = UserRegistrationForm()
    error = ""
    image=""

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj     = form.cleaned_data
            username    = userObj['username']
            email       =  userObj['email']
            first_name  =  userObj['first_name']
            last_name   =  userObj['last_name']

    userprofile.first_name = first_name
    userprofile.last_name = last_name
    userprofile.email = email
    try: 
        if request.FILES['image']:
            image = request.FILES['image']
            userprofile.user.image = image
            userprofile.save()
            return index(request, user.username)
    except:
        userprofile.save()