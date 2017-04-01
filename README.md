# Youth-Week-Hackathon

## Local settings you need
In the app directory create your own local_settings.py file

ALLOWED_HOSTS = ['127.0.0.1']

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='<EMAIL HOST>'
EMAIL_PORT='<EMAIL_PORT>'
EMAIL_HOST_USER='<YOUR EMAIL ADDRESS>'
EMAIL_HOST_PASSWORD='<PASSWORD FOR EMAIL>'
EMAIL_USE_TLS=True
```

`ALLOWED_HOSTS` should be configured to a list of domains that the server is allowed to serve ([more information](https://docs.djangoproject.com/en/1.10/ref/settings/)).

`EMAIL_HOST` Should be the service which hosts your email address e.g. smtp.google.com .

`EMAIL_PORT` The port which the service runs on.
