from django.shortcuts import render
from post.models import Post


def upload(request):
    if request.method == 'POST':
        new_post = Post(
            user=request.user,
            description=request.POST.get('description',None),
            img=request.FILES.get('img'),
        )
        new_post.save()
    return render(request, 'post/upload.html')
