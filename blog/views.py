from django.shortcuts import render,HttpResponseRedirect
from django.views import View
from blog.models import ArticleModel

class ViewArticles(View):
    template_name='index.html'
    def get(self,request,*args,**kwargs):
        context={}
        first10=ArticleModel.objects.all()[:10]
        if len(first10)>0:
            context['new_article'] = first10[0]
        context['other_articles'] = first10[1:10]
        return render(request,self.template_name,context)

class CreateArticleView(View):
    template_name = 'add_article.html'

    def get(self, request):
        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        article = ArticleModel()
        article.title = request.POST.get("title")
        article.body = request.POST.get("body")
        article.image = request.FILES.get("image")
        article.save()
        return HttpResponseRedirect("/")


