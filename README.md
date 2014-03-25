23andCSB
========

Ready to deploy on Heroku.

First, create your app and push the repo:
```bash
$ heroku create <yourappname>
$ git push heroku master
```

After the slug is compiled and running, you will need to supply several environment variables using `heroku config`:
```bash
$ heroku config:set DEBUG=False
$ heroku config:set ENVIRONMENT='PRODUCTION'
$ heroku config:set SECRET_KEY=XXXX
```

These are the settings for the 23andMe API:
```bash
$ heroku config:set CLIENT_ID=XXXX
$ heroku config:set CLIENT_SECRET=XXXX
$ heroku config:set CALLBACK_URL="http://<yourappname>.herokuapp.com/auth/callback/"
```

Promote the database provided to the `DATABASE_URL` config var:
```bash
$ heroku pg:promote HEROKU_POSTGRESQL_<COLOR>_URL
```

Initialize the database tables:
```bash
$ heroku run python manage.py syncdb
```
