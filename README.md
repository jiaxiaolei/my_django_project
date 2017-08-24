

>  更多资料：graphql在 django中的实现(一)
  http://www.jianshu.com/p/6db4f24da9cc


基于已有的 `my_django_project`, 建立一个空白分支
```
$ cd my_django_project

$ git checkout --orphan graphql
切换到一个新分支 'graphql'

$ git log
fatal: bad default revision 'HEAD'

$ git rm -rf .
rm '.commit_template'
rm '.gitignore'
rm 'README.md'
rm 'project_001/app_001/__init__.py'
rm 'project_001/app_001/admin.py'
rm 'project_001/app_001/apps.py'
rm 'project_001/app_001/migrations/__init__.py'
rm 'project_001/app_001/models.py'
rm 'project_001/app_001/tests.py'
rm 'project_001/app_001/views.py'
rm 'project_001/db.sqlite3'
rm 'project_001/manage.py'
rm 'project_001/project_001/__init__.py'
rm 'project_001/project_001/settings.py'
rm 'project_001/project_001/urls.py'
rm 'project_001/project_001/wsgi.py'

## 文件夹 `project_001` 可能不会被删除。如果没有删除，手动删除 `rm -rf project_001`;
## project 中如果没有文件，可能无法commit。此时可以建立一个文件(比如.gitignore或者.commit_template)
$ git commit
```
## 安装 graphene-django
```
$ pip install graphene-django
Collecting graphene-django
  Downloading http://mirrors.aliyun.com/pypi/packages/33/34/1b82fe1752c20d2b375d10299c801b8410f5df5c95dd5c739b38ee49ec88/graphene-django-1.3.tar.gz
Requirement already satisfied: six>=1.10.0 in /root/.virtualenvs/py2.7.13cmdb2.0/lib/python2.7/site-packages (from graphene-django)
Collecting graphene>=1.4 (from graphene-django)
  Downloading http://mirrors.aliyun.com/pypi/packages/3a/12/04b4b89eec5f5dd97d06c2143e5db3ec0801f4b940e69db072dd89de8514/graphene-1.4.1.tar.gz
Requirement already satisfied: Django>=1.6.0 in /root/.virtualenvs/py2.7.13cmdb2.0/lib/python2.7/site-packages (from graphene-django)
Collecting iso8601 (from graphene-django)
  Downloading http://mirrors.aliyun.com/pypi/packages/ef/57/7162609dab394d38bbc7077b7ba0a6f10fb09d8b7701ea56fa1edc0c4345/iso8601-0.1.12-py2.py3-none-any.whl
Requirement already satisfied: singledispatch>=3.4.0.3 in /root/.virtualenvs/py2.7.13cmdb2.0/lib/python2.7/site-packages (from graphene-django)
Collecting graphql-core>=1.1 (from graphene>=1.4->graphene-django)
  Downloading http://mirrors.aliyun.com/pypi/packages/b0/89/00ad5e07524d8c523b14d70c685e0299a8b0de6d0727e368c41b89b7ed0b/graphql-core-1.1.tar.gz (70kB)
    100% |████████████████████████████████| 71kB 280kB/s
Collecting graphql-relay>=0.4.5 (from graphene>=1.4->graphene-django)
  Downloading http://mirrors.aliyun.com/pypi/packages/5e/b0/b91fadc180544fc9e3c156d7049561fd5f1e2211d26fd29033548fd50934/graphql-relay-0.4.5.tar.gz
Collecting promise>=2.0 (from graphene>=1.4->graphene-django)
  Downloading http://mirrors.aliyun.com/pypi/packages/62/a4/d979b8cbfef42b695a9c3851d3d918884fb0d2f84f6c43451311a2acb5bf/promise-2.0.2.tar.gz
Requirement already satisfied: pytz in /root/.virtualenvs/py2.7.13cmdb2.0/lib/python2.7/site-packages (from Django>=1.6.0->graphene-django)
Collecting typing (from promise>=2.0->graphene>=1.4->graphene-django)
  Downloading http://mirrors.aliyun.com/pypi/packages/1c/15/aeaae0c01afa895ad774cfd408eca17818fd753817d433f55385d8e36364/typing-3.6.2-py2-none-any.whl
Building wheels for collected packages: graphene-django, graphene, graphql-core, graphql-relay, promise
  Running setup.py bdist_wheel for graphene-django ... done
  Stored in directory: /root/.cache/pip/wheels/f8/f6/09/8e04b5f33720bd00cfc5422090472243033f32658e033b78db
  Running setup.py bdist_wheel for graphene ... done
  Stored in directory: /root/.cache/pip/wheels/40/45/84/4da96e789ddd5cf2fc85d594f1ff96c619da1fd2570fe01bf9
  Running setup.py bdist_wheel for graphql-core ... done
  Stored in directory: /root/.cache/pip/wheels/a8/2d/58/060e91a49245d5515396f455cdfc15d0c1da5ff489dd23df17
  Running setup.py bdist_wheel for graphql-relay ... done
  Stored in directory: /root/.cache/pip/wheels/3a/6b/db/bc482e6a5c41aa0aaa9bcc3626a95f774771d4baeac707f13e
  Running setup.py bdist_wheel for promise ... done
  Stored in directory: /root/.cache/pip/wheels/12/2f/d7/d0f8c817cb6dc37eab930c880f6a9d2b76902703b1a50fa9cd
Successfully built graphene-django graphene graphql-core graphql-relay promise
Installing collected packages: typing, promise, graphql-core, graphql-relay, graphene, iso8601, graphene-django
Successfully installed graphene-1.4.1 graphene-django-1.3 graphql-core-1.1 graphql-relay-0.4.5 iso8601-0.1.12 promise-2.0.2 typing-3.6.2
```

## 建立一个project `dmyz`
```
$ django-admin startproject dmyz

$ cd dmyz/
## 执行migrate创建表
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


## 建立用户。
$ python manage.py createsuperuser
Username (leave blank to use 'root'): root
Email address:
Password:
Password (again):
Superuser created successfully.

## 为方便后续测试，可以建立多个用户

$ python manage.py createsuperuser
Username: jiaxiaolei
Email address:
Password:
Password (again):
Superuser created successfully.
$ python manage.py createsuperuser
Username: wkp
Email address:
Password:
Password (again):
Superuser created successfully.
$ python manage.py createsuperuser
Username: wzb
Email address: wzb@qq.com
Password:
Password (again):
Superuser created successfully.

```

## 编辑settings.py，将graphene-django加入INSTALLED_APPS：
```
INSTALLED_APPS = (
    # ...
    'graphene_django',
)
```

再编辑urls.py，导入GraphQLView，加上graphql的设置：
```
from graphene_django.views import GraphQLView

urlpatterns = [
    # ...
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]
```



```
$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
August 24, 2017 - 02:16:46
Django version 1.11.3, using settings 'dmyz.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

在浏览器中输入： http://172.28.32.49:8000/graphql(主机ip为172.28.32.49)， 提示访问失败：
```
ERR_CONNECTION_REFUSED
```

修改 runserver 的启动参数：
```
$ python manage.py runserver 0.0.0.0:8000
```
在浏览器中访问，提示：
```
DisallowedHost
```

修改 settings.py, 允许所有host访问。
```
#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = []
```

再次访问 /graphql会报错，显示没有提供schema。
```
$ python manage.py runserver 0.0.0.0:8000
Performing system checks...

System check identified no issues (0 silenced).
August 24, 2017 - 02:17:14
Django version 1.11.3, using settings 'dmyz.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
Not Found: /
[24/Aug/2017 02:17:17] "GET / HTTP/1.1" 404 2020
Internal Server Error: /graphql
Traceback (most recent call last):
  File "/root/.virtualenvs/py2.7.13cmdb2.0/lib/python2.7/site-packages/django/core/handlers/exception.py", line 41, in inner
    response = get_response(request)
  File "/root/.virtualenvs/py2.7.13cmdb2.0/lib/python2.7/site-packages/django/core/handlers/base.py", line 187, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/root/.virtualenvs/py2.7.13cmdb2.0/lib/python2.7/site-packages/django/core/handlers/base.py", line 185, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/root/.virtualenvs/py2.7.13cmdb2.0/lib/python2.7/site-packages/django/views/generic/base.py", line 62, in view
    self = cls(**initkwargs)
  File "/root/.virtualenvs/py2.7.13cmdb2.0/lib/python2.7/site-packages/graphene_django/views.py", line 84, in __init__
    assert isinstance(self.schema, GraphQLSchema), 'A Schema is required to be provided to GraphQLView.'
AssertionError: A Schema is required to be provided to GraphQLView.
[24/Aug/2017 02:17:31] "GET /graphql HTTP/1.1" 500 73787
```

在dmyz目录中新建schema.py文件，目录结构如下：

```
dmyz
├── db.sqlite3
├── dmyz
│   ├── __init__.py
│   ├── schema.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

编辑schema.py文件，导入DjangoObjectType和graphene，处理django自带的User Model，代码如下：

```
from django.contrib.auth.models import User as UserModel

from graphene_django import DjangoObjectType
import graphene

class User(DjangoObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    users = graphene.List(User)

    @graphene.resolve_only_args
    def resolve_users(self):
        return UserModel.objects.all()

schema = graphene.Schema(query=Query)
```

最后编辑settings.py，加上配置：
```
GRAPHENE = {
    'SCHEMA': 'dmyz.schema.schema'
}
```

现在重新访问/graphql，可以看到自带的前端界面，在左上方文本框中输入：

```
{
  users {
    username
    email
  }
}
```

运行（点击上方![▶️]按钮）返回admin用户的username和email。右侧的Docs会显示Query信息，下划线命名也会自动转成驼峰命名。
查询语句完整格式是 *query 名称{}*，上面的查询语句省掉了*query*，因为GraphQL默认会作为*query*语句执行，如果是*mutation*就需要加上了。关于查询语句可以参考官方文档：[http://graphql.org/learn/queries/](http://graphql.org/learn/queries/)



扩展阅读：
===========

GRAPHQL+DJANGO提供基本API
http://dmyz.org/archives/778
简介：
graphql 在 django 中的实现。


https://github.com/graphql-python/graphene-django
简介：
github上`graphene-django`的地址。其中有几个实用的demo，还是很有用的。


http://graphql.org/learn/queries/
简介：
graphql 官方文档，可以看到查询语句的API.

Queries and Mutations
On this page, you'll learn in detail about how to query a GraphQL server.



在GIT中创建一个空分支
https://segmentfault.com/a/1190000004931751
简介：
建立一个空分支。

