from django.shortcuts import render


def jqtest(request):
    return render(request, 'pybo/test/jqtest.html')


def imgtest(request):
    return render(request, 'pybo/test/imgtest.html')


def market(request):
    return render(request, 'pybo/test/market.html')


def components(request):
    return render(request, 'pybo/test/boot_components.html')
