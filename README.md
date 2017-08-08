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

通过 http://ip:8000/ 在浏览器中进行访问，提示：

```
无法访问此网站

172.28.32.49 拒绝了我们的连接请求。
请在 Google 中搜索“172 8000”
ERR_CONNECTION_REFUSED
```
