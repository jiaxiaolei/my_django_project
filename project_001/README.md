
A simple project usting Django as web framework.



login:
-------

http://<ip:port>/admin/
``
http://172.28.32.49:7771/admin/

user: root
passwd: jia123456
```

test
=======
django.test
----------

nosetest
----------

pytest
--------

coverage
------
```
$ coverage run --source='.' manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
FF
======================================================================
FAIL: test_http (app_001.tests.SendviewsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/my_django_project_test/project_001/app_001/tests.py", line 16, in test_http
    self.assertEqual(ret.status_code, 200)
AssertionError: 404 != 200

======================================================================
FAIL: test_http2 (app_001.tests.SendviewsTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/opt/my_django_project_test/project_001/app_001/tests.py", line 21, in test_http2
    self.assertEqual(ret.status_code, 200)
AssertionError: 404 != 200

----------------------------------------------------------------------
Ran 2 tests in 0.012s

FAILED (failures=2)
Destroying test database for alias 'default'...

```


```
$ coverage report -m
Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
app_001/__init__.py                  0      0   100%
app_001/admin.py                     2      2     0%   2-4
app_001/apps.py                      4      4     0%   2-8
app_001/migrations/__init__.py       0      0   100%
app_001/models.py                    2      2     0%   2-4
app_001/tests.py                    15      0   100%
app_001/views.py                     2      2     0%   2-4
manage.py                           13      6    54%   9-21
project_001/__init__.py              0      0   100%
project_001/settings.py             18      0   100%
project_001/urls.py                  3      0   100%
project_001/wsgi.py                  4      4     0%   10-16
--------------------------------------------------------------
TOTAL                               63     20    68%
```
