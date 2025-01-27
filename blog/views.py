
from django.shortcuts import render,get_object_or_404
from .models import Posts

def starting_page(request):
   latest_post = Posts.objects.all().order_by("-date")[:3] # - sign show decending order 
   return render(request, "blog/index.html", {
        "posts": latest_post
    })

def posts(request):
    all_posts = Posts.objects.all().order_by("-date")
    # Pass all_posts to the template
    return render(request, "blog/all-post.html", {
        "posts": all_posts
    })

def post_details(request, id):
    identified_post = get_object_or_404(Posts, id=id)

    return render(request, "blog/post-details.html", {
        "post": identified_post
    })