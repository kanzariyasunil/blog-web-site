from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    post = Post.objects.all()
    return render(request,'home/index.html',{'posts':post})

def about(request):
    messages.success(request,'welcome to About page')
    return render(request,'home/about.html')

def contect(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        
        if len(name) < 2 or len(email) < 5 or len(phone) < 10 or len(content) < 1:
            messages.error(request,'Please enter the details currectly')
        else:
            messages.success(request,'message sent succesfully')
            contact = Contact(name = name , email = email , phone = phone,content = content)
            contact.save()
    return render(request,'home/contact.html')

def search(request):
    query=request.GET['query']
    
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains = query)
        allPostsAuthor = Post.objects.filter(author__icontains = query)
        allPostsContent = Post.objects.filter(content__icontains = query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
        
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    
    return render(request, 'home/search.html', params)

def handleSignup(request):
    if request.method == 'POST':
        # information are store 
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        # check the username 
        if len(username) > 10:
            messages.error(request,"please enter the under 10 charecter username")
            return redirect("/")
        
        # check the pass1 and pass2
        if pass1 != pass2:
            messages.error(request,"password does not match entet again password")
            return redirect("/")
        
        # fill the user infomation in admin panal 
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Congrates you have registered successfully')
        return redirect('/')
    else:
        return HttpResponse('404 - Not Found')
    
    
def handlelogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpassword']
        
        user = authenticate(username = loginusername,password = loginpass)
        
        if user is not None:
            login(request,user)
            messages.success(request,'You are successfully login ')
            return redirect('/')
        else:
            messages.error(request,'invalid Credecials')
            return redirect('/')
    return HttpResponse('handle login')

def handlelogout(request):
    logout(request)
    messages.success(request,'User successfully logout!')
    return redirect('/')
    # return HttpResponse('handle logout')