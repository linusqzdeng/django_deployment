# 使用Apache+mod_wsgi部署Django

## 1. 下载Apache和mod_wsgi

[Apache Lounge下载地址](https://www.apachelounge.com)

推荐安装Apache Lounge，其他distro可能会因文件缺失而导致其他模组编译失效

[mod_wsgi的安装](https://github.com/GrahamDumpleton/mod_wsgi)

Windows下只能通过`pip install mod_wsgi`的方式进行安装

`mod_wsgi`安装成功后，运行指令`mod_wsgi-express module-config`，产生结果
```
LoadModule wsgi_module /usr/local/lib/python2.7/site-packages/mod_wsgi/server/mod_wsgi-py27.so

WSGIPythonHome /usr/local/lib
```

以上结果需要添加到Apache配置文件⬇️

<br/>

## 2. 更改配置文件

在Apache目录下找到配置文件`httpd.conf`并进行如下更改

```
WSGIScriptAlias / /path/to/mysite.com/mysite/wsgi.py
WSGIPythonHome /path/to/venv
WSGIPythonPath /path/to/mysite.com

LoadModule wsgi_module /usr/local/lib/python2.7/site-packages/mod_wsgi/server/mod_wsgi-py27.so

<Directory /path/to/mysite.com/mysite>
<Files wsgi.py>
Require all granted
</Files>
</Directory>

# 详情见参考文档2
```

<br/>

## 3. 更改项目代码

### `mysite/setting.py`

更改`ALLOWED_HOST = ["*"]`

### `wsgi.py`

```python
import os
import sys
from django.core.wsgi import get_wsgi_application
from os.path import dirname, abspath

# Add project directory to sys.path
proj_dir = '/Users/linus/Nothinghere/django_setup/web_setup/polls'
if proj_dir not in sys.path:
	print(proj_dir)
	sys.path.append(proj_dir)
	
PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)
```

<br/>

## 4. 运行

以上配置完成后，运行`apachectl start`，成功后在项目中运行`python manage.py runserver 0:8000`

---
# 可能出现的错误

```
AH00557: httpd: apr_sockaddr_info_get() failed for Sureshs-MacBook-Pro.local
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 127.0.0.1. Set the 'ServerName' directive globally to suppress this message
httpd not running, trying to start
```

解决方法：注释掉`httpd.conf`中的`ServerName`并改成

```
ServerName localhost
```

如果不行，重启Apache

---
# 参考文档

1. [mod_wsgi官方安装说明](https://modwsgi.readthedocs.io/en/master/)
2. [如何使用 Apache 和 mod_wsgi 托管 Django](https://docs.djangoproject.com/zh-hans/2.2/howto/deployment/wsgi/modwsgi/)
3. [无涯日记 - Windows下Django + Apache + mod_wsgi 部署](https://www.wuyariji.com/windows-huan-jing-xia-django-apache-mod_wsgi-bu-shu.html)
4. [开源博客 - apache+mod_wsgi+django的环境配置](https://my.oschina.net/u/2000932/blog/1507215)
5. [AH00557错误](https://apple.stackexchange.com/questions/280099/apache-on-macos-sierra-ah00557-httpd-apr-sockaddr-info-get-failed-for-macbo)
