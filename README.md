# izCert
Source code for izCert.com

# Deployment
## Dev
Add a `.env.dev` file in projects root

In `.env.dev`, populate environmental variables using following template
```{bash}
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_dev
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
DJANGO_SUPERUSER_PASSWORD=admin
```

Run `docker-compose up -d --build`

Access dev server at `localhost:8100`
