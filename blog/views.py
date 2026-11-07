from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post, UserQuote
from django.contrib.auth.decorators import login_required


@login_required
def page(request):
    search_query = request.GET.get('q', '').strip()
    posts = Post.objects.order_by('-created_at')

    if search_query:
        posts = posts.filter(title__icontains=search_query) | posts.filter(content__icontains=search_query)

    quote_entry, _ = UserQuote.objects.get_or_create(user=request.user)
    saved_quote = quote_entry.quote or ''

    if request.method == 'POST' and 'saved_quote' in request.POST:
        quote = request.POST.get('saved_quote', '').strip()
        if quote:
            quote_entry.quote = quote
            quote_entry.save()
            saved_quote = quote
            request.session['saved_quote'] = quote

    welcome_message = request.session.get('welcome_message', "What's Going On in the World")

    return render(
        request,
        'blog/page.html',
        {
            'posts': posts,
            'saved_quote': saved_quote,
            'welcome_message': welcome_message,
            'search_query': search_query,
        },
    )


@login_required
def post_create(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        image = request.FILES.get('image')

        if not title or not content or not category_id:
            return render(request, 'blog/category_create.html', {
                'categories': categories,
                'error': 'Please fill in all fields.'
            })

        category = get_object_or_404(Category, id=category_id)

        post = Post.objects.create(
            author=request.user,
            title=title,
            content=content,
            img=image,
        )
        post.category.add(category)

        return redirect('blog_page')

    return render(request, 'blog/category_create.html', {'categories': categories})


@login_required
def category_create(request):
    return post_create(request)


@login_required
def category_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/category_detail.html', {'post': post})