from django.shortcuts import render

from .models import News


def test(request):

    print('Принял запрос')
    news = News.objects.all()
    for new in news:
        print(new.title)
        print(new.likes)
    #
    # return render(request, 'test.html')

    # news = News.objects.filter(likes__gte=2)
    # news = News.objects.filter(title='новость 2', likes__gte=2)
    # for new in news:
    #     print(new.title)
    #     print(new.likes)
    #
    # return render(request, 'test.html')

    News.objects.create(title='Новость 4', text='просто текст', likes=5)

    return render(request, 'test.html')

