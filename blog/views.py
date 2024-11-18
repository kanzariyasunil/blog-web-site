from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,BlogComment
from django.contrib import messages

# Create your views here.
def bloghome(request):
    allPost = Post.objects.all()
    return render(request,'blog/blogHome.html',{'allPost':allPost})

def blogpost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()
    
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.filter(sno = postSno).first()
        parentsno = request.POST.get('parentSno')
        if len(comment) < 1:
            messages.error(request,'please enter the commnt before you can send!')
            return redirect(f'/blog/{post.slug}')
        
        if parentsno == "":    
            comment1 = BlogComment(comment = comment,user = user,post = post)
            comment1.save()
            messages.success(request,f' {request.user} Your comment is send successfully.')
        else:
            parent = BlogComment(sno = parentsno)
            comment = BlogComment(comment = comment,user = user,post = post,parent = parent)
            comment.save()
            messages.success(request,'Your request is successfully')
    return redirect(f'/blog/{post.slug}')