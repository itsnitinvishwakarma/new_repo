from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from taggit.models import Tag

from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag = None
    if tag_slug:
        tag = Tag.objects.get(slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    pgntr_obj=Paginator(post_list,2)
    page_num=request.GET.get('page')
    try:
        post_list=pgntr_obj.page(page_num)
    except PageNotAnInteger:
        post_list=pgntr_obj.page('1')
    except EmptyPage:
        post_list=pgntr_obj.page(pgntr_obj.num_pages)

    return render(request, 'post_list.html',{'post_list':post_list,'tag':tag})

from .forms import EmailForm, CommentForm
from django.core.mail import send_mail
def sharebymail(request,id):
    post=Post.objects.get(id=id,status='published')
    form=EmailForm()
    sent=False
    if request.method=="POST":
        form=EmailForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{}({}) recomments u to read {}'.format(cd['Name'],cd['by'],post.title)
            url=request.build_absolute_uri(post.get_absolute_url())
            message='{}\n{}'.format(url,cd['Comment'])
            send_mail(subject,message,'djframework123@gmail.com',[cd['to']])
            sent=True

    return render(request,"sharebymail.html",{'form':form,'post':post,'sent':sent})

def post_detail_view(request,year,month,day,title):
    post=Post.objects.get(slug=title,status='published',publish__day=day,
                          publish__year=year,publish__month=month)
    #post=get_object_or_404(Post,status='publish',publish__year=year)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()

    return render(request,"post_detail.html",{'post':post,'form':form,'csubmit':csubmit,'comments':comments})