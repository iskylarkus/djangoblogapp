from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article, Comment


def index(request):
    # return HttpResponse("<h3>Deneme Ana Sayfa</h3>")
    # return render(request, "index.html")
    # return render(request, "article/index.html")
    context = {"number1": 10, "number2": 20, "numbers": [1, 2, 3, 4, 5]}
    return render(request, "index.html", context=context)


def about(request):
    return render(request, "about.html")


def article_list(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
    else:
        articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "article_list.html", context=context)


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def article_add(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    if form.is_valid():
        new = form.save(commit=False)
        new.author = request.user
        new.save()
        messages.success(request, 'Makaleniz başarıyla kayıt edildi..!')
        return redirect("article:dashboard")
    else:
        return render(request, "article_add.html", context)


@login_required(login_url="user:login")
def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None,
                       request.FILES or None, instance=article)
    context = {
        "form": form
    }
    if form.is_valid():
        new = form.save(commit=False)
        new.author = request.user
        new.save()
        messages.success(request, 'Makaleniz başarıyla güncellendi..!')
        return redirect("article:dashboard")
    else:
        return render(request, "article_edit.html", context)


@login_required(login_url="user:login")
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, 'Makaleniz başarıyla silindi..!')
    return redirect("article:dashboard")


def article_detail(request, id):
    #article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    context = {
        "article": article,
        "comments": comments
    }
    return render(request, "article_detail.html", context)


def article_comment(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        new = Comment(comment_author=comment_author,
                      comment_content=comment_content)
        new.article = article
        new.save()
    # return redirect("/article/detail/" + str(id))
    return redirect(reverse("article:detail", kwargs={"id": id}))


def detail(request, id):
    # return render(request, "about.html")
    return HttpResponse("Detail: " + str(id))
