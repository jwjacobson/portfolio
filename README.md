# Personal Portfolio/Blog

This is a simple portfolio to showcase my projects. As of July 2026, it is also a personal blog, mainly as a persistent archive for my LinkedIn posts.

### Tech stack
The portfolio is built using [Django 5](https://www.djangoproject.com/) and [htmx](https://htmx.org/) and styled with [Tailwind CSS](https://tailwindcss.com/). Project data and blogposts are stored in a [PostgreSQL](https://www.postgresql.org/) database in production and in a [SQLite](https://sqlite.org/) database when run locally. Static assets are served by [WhiteNoise[(https://whitenoise.readthedocs.io/en/stable/django.html), images from an [AWS S3](https://aws.amazon.com/s3/) bucket.

The live site is deployed to [Hetzner](https://www.hetzner.com/) using [Dokku](https://dokku.com/).

### License
This project is [free software](https://www.fsf.org/about/what-is-free-software), released under version 3.0 of the GPL. Everyone has the right to use, modify, and distribute this project subject to the [stipulations](https://github.com/jwjacobson/portfolio/blob/main/LICENSE) of that license.

### Acknowledgments
I used Real Python's [portfolio tutorial](https://realpython.com/get-started-with-django-1/) as a major reference, though I also deviate from it quite a bit.
