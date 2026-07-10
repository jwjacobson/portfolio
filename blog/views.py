# portfolio -- Jeff Jacobson's personal portfolio
# Copyright (C) 2024 Jeff Jacobson <jeffjacobsonhimself@gmail.com>
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from blog.models import Post, Tag


def blog_list(request):
    posts = Post.objects.published()

    tag_slug = request.GET.get('tag')
    active_tag = None
    if tag_slug:
        active_tag = Tag.objects.filter(slug=tag_slug).first()
        posts = posts.filter(tags__slug=tag_slug)

    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {'page_obj': page_obj, 'active_tag': active_tag}

    if request.headers.get('HX-Request'):
        return render(request, 'blog/_blog.html', context)

    return render(request, "portfolio/index.html", context)


def post_detail(request, slug):
    post = get_object_or_404(Post.objects.published(), slug=slug)

    if request.headers.get('HX-Request'):
        return render(request, 'blog/_post.html', {'post': post})

    return render(
        request, "portfolio/index.html",
        {'selected_post': post}
    )
