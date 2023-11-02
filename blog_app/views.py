from django.shortcuts import render,get_object_or_404,redirect


from .models import BlogPost
from django.core.paginator import Paginator

def blog_post_list(request):
    blog_posts = BlogPost.objects.all()
    
    paginator = Paginator(blog_posts, 1)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    context = {
        'blog_posts': page.object_list,
        'page': page,
    }

    return render(request, 'index.html', context)

from .forms import CommentForm
def blog_post_detail(request, id):
    blog_post = BlogPost.objects.get(id=id)
    comment_form = CommentForm()
    


    # Exclude the current blog post from the list of related posts.
    related_posts = BlogPost.objects.filter(tags__in=blog_post.tags.all()).exclude(id=blog_post.id).distinct()
    context = {
        'blog_post': blog_post,
        'comment_form': comment_form,
        "related_posts":related_posts
    }

    return render(request, 'blog_post_detail.html', context)

def create_comment(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
    return redirect('blog_post_detail', id=id)


from django.db.models import Q

def search_posts(request):
    query = request.GET.get('query')

    # Create a `q` object to filter the `BlogPost` queryset by the search query.
    q = Q(title__contains=query) | Q(content__contains=query)

    # Filter the `BlogPost` queryset using the `q` object.
    blog_posts = BlogPost.objects.filter(q)
    
    paginator = Paginator(blog_posts, 1)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    context = {
        'blog_posts': page.object_list,
        'page': page,
    }
    context = {
        'blog_posts': blog_posts,
    }

    return render(request, 'index.html', context)