from django.shortcuts import render

posts = [
    {'id':1, 'name': 'First Post'},
    {'id':2, 'name': 'Second Post'},
    {'id':3, 'name': 'Third Post'},
]

def home(request):
    dic = {'posts':posts}
    return render(request, 'baseApp/home.html', dic)

def post(request, pk):
    post = None
    for i in posts:
        if i['id'] == int(pk):
            post = i
    dic = {'post':post}

    return render(request, 'baseApp/post.html', dic)
