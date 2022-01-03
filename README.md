# Mini blog (Pinterest style)
핀터레스트 스타일의 마이크로 사이트로 이미지를 업로드하여 공유할 수 있습니다.  
~~AWS로 호스팅(http://54.180.142.121/) 했었으나 핀터레스트 저작권 문제로 호스팅 중단~~ 

![https://user-images.githubusercontent.com/69188437/115881677-f355ee00-a486-11eb-94a2-f4d7853bea22.png](https://user-images.githubusercontent.com/69188437/115881677-f355ee00-a486-11eb-94a2-f4d7853bea22.png)

## Install
이 프로젝트는 파이썬을 사용하였습니다. 가상환경(Virtualenv)을 생성하여 설치하는 것을 권장합니다. 
Git Clone 전 프로젝트 디렉토리를 생성한 뒤 해당 경로에서 시작할 것을 권장합니다. 

### Git clone
```shell
$ git clone https://github.com/Seungho-Jeong/pinterest_style.git
```

### Django
```shell
$ python -m pip install -r requirements.txt
$ python manage.py migrate --settings=config.settings.local
$ python manage.py runserver --settings=config.settings.local
```

## Usage
Django 서버 실행 후 아래의 주소로 접속하면 로컬환경에서 회원가입, 로그인, 이미지(업로드･수정･삭제), 
댓글(생성･수정･삭제), 게시글 '좋아요' 등을 수행할 수 있습니다.
```text
http://localhost:8000/
```

## Tech & Framework used

### Back-end
- Python 3.8+
- Django 3.2
- MariaDB

### Front-end
- Django 3.2
- Bootstrap 4.0
- 약간의 JavaScript

### Infra
로컬환경이 아닌 배포환경에서 사용하였던 기술입니다.  
현재는 저작권(핀터레스트) 문제로 배포 중단하였습니다.  
- Gunicorn (WSGI)
- Nginx (Web Server)
- AWS EC2
- Docker

### e.t.c.
- [Django-bootstrap4](https://github.com/zostera/django-bootstrap4)
- [Magic grid](https://github.com/e-oj/Magic-Grid)
- [Medium editor](https://github.com/yabwe/medium-editor)
- Pillow
