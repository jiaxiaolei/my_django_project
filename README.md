# my_django_project
```
$ django-admin startproject project_001

$ cd project_001

$ python manage.py runserver

Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

August 08, 2017 - 05:34:41
Django version 1.11.3, using settings 'project_001.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
按照提示，执行 migrate

```
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
```
再次启动：

```
 python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
August 08, 2017 - 05:44:02
Django version 1.11.3, using settings 'project_001.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

访问页面：

$ w3m http://127.0.0.1:8000

```
It worked!

Congratulations on your first Django-powered page.

Next, start your first app by running python manage.py startapp [app_label].

You're seeing this message because you have DEBUG = True in your Django settings file and you haven't configured any URLs. Get to work!
```

创建app

$ python manage.py startapp app_001



通过 http://ip:8000/ 在浏览器中进行访问，提示：

```
无法访问此网站

172.28.32.49 拒绝了我们的连接请求。
请在 Google 中搜索“172 8000”
ERR_CONNECTION_REFUSED
```

修改 project_001/settings.py 文件

```
ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = []
```
再次启动 
$ python manage.py runserver

启动项目新增 0.0.0.：8000
```
$ python manage.py runserver 0.0.0.0:8000
Performing system checks...

System check identified no issues (0 silenced).
August 08, 2017 - 05:51:40
Django version 1.11.3, using settings 'project_001.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.


[08/Aug/2017 05:51:43] "GET / HTTP/1.1" 200 1716
```

此时，通过浏览器可以访问。默认提供 /admin url.

http://172.28.32.49:8000/admin


创建一组账号：root/jia123456
$ python manage.py createsuperuser
Username (leave blank to use 'root'):
Email address:
Password:
Password (again):
Superuser created successfully.

