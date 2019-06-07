from django.shortcuts import render


# Create your views here.
def test(request):
    return render(request, 'Test.html')


def main(request):
    return render(request, 'index.html')


def cnt(request):
    text = request.GET['fulltext']
    words = text.split()
    return render(request, 'result.html', {'full': text, 'total': len(words)})
