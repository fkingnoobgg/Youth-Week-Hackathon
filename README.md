# Youth-Week-Hackathon

## Local settings you need
In the app directory create your own local_settings.py file

```
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='<EMAIL HOST>'
EMAIL_PORT='<EMAIL_PORT>'
EMAIL_HOST_USER='<YOUR EMAIL ADDRESS>'
EMAIL_HOST_PASSWORD='<PASSWORD FOR EMAIL>'
EMAIL_USE_TLS=True
```

`EMAIL_HOST` Should be the service which hosts your email address e.g. smtp.google.com .

`EMAIL_PORT` The port which the service runs on.
