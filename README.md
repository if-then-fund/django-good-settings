django-good-settings
====================

A Django 1.8+ `settings.py` that gets you going with good, secure settings.

Copy (or symbolically link) this `settings.py` and `helper_middleware.py` into your main application.

You get:

* A random secret key on each launch, until you make an `environment.json` to store a key.
* The usual set of `INSTALLED_APPS` and `MIDDLEWARE_CLASSES`.
* The usual settings for `ROOT_URLCONF`, `TIME_ZONE`, etcetera --- see the settings.py for details.
* [allauth](http://www.intenct.nl/projects/django-allauth/) is configured for user accounts, in login-with-username mode.
* A default Sqlite database stored in `local/db.sqlite`.
* A default `LocMemCache` cache.
* A default console EMAIL_BACKEND so you can debug emails quickly.
* When `DEBUG` is `True`, stack traces of exceptions in views are written to the runserver console so you can see them more easily.
* When `DEBUG` is `False`, the cached template loader is used.
* When `test_without_migrations` is installed, it is added to `INSTALLED_APPS`.

Then you configure this:

* Create a file `settings_application.py` next to `settings.py` with your additional settings. You can `import .settings` at the top of your file to access/adjust any of the defaults.

* Create a file `local/environment.json` with additional settings.

Your `local/environment.json` file should look like this:

	{
	  "debug": true,
	  "host": "localhost:8000",
	  "https": false,
	  "secret-key": "....",
	  "admins": [["name1", "email1"], ["name2", "email2"], ...]
	}

The keys are:

`debug`: `true` or `false`. Sets `DEBUG` and other settings.

`secret-key`: A random string of 50 characters unique to you for SECRET_KEY. See how others generate Django SECRET_KEY values.

`host`: Sets `ALLOWED_HOSTS` and `EMAIL_SUBJECT_PREFIX`.

`db`: Sets `DATABASES['default']`. If `db` is set, then `CONN_MAX_AGE` is automatically given a sane default.

`memcached`: If `true`, then Django's MemcachedCache backend is activated.

`https`: If `true` (and you should do this if true!), then sets settings good for HTTPS sites (e.g. SESSION_COOKIE_SECURE).

`static`: A path for `collectstatic`. If set, turns on the `ManifestStaticFilesStorage` backend.
