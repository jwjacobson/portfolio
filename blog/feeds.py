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

from django.contrib.syndication.views import Feed
from django.urls import reverse

from blog.models import Post
from blog.templatetags.markdown_extras import markdown as render_markdown


class LatestPostsFeed(Feed):
    title = "Jeff Jacobson"
    link = "/"
    description = "Latest posts from Jeff Jacobson's blog."

    def items(self):
        return Post.objects.published()[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return render_markdown(item.body)

    def item_link(self, item):
        return reverse('post_detail', args=[item.slug])

    def item_pubdate(self, item):
        return item.published_at
