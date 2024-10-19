# 프로젝트 문의 / 제안
프로젝트와 관련한 내용은 <https://django.seolpypo.com/>에 이야기해주시면 감사합니다.

# 프로젝트 목적
백업파일을 이용하여 티스토리 블로그에 작성한 글들을 Django로 이전하여 운영할 수 있도록 합니다.
티스토리와 동일한 url 구조를 사용합니다.

## 사용방법
### 패키지 설치
디스토리 패키지를 설치합니다.
tqdm, requests, bs4(BeautifulSoup), selenium, django, django-summenote를 필요로 합니다.
>> pip install seolpyo_dstory

### 장고 프로젝트 생성
mysite라는 폴더를 생성하고, 폴더 안에 장고 프로젝트를 생성합니다.
>> mkdir mysite
>> cd mysite
>> django-admin startproject config .

### 기초 설정
INSTALLED_APPS에 seolpyo_dstory, django_summenote, django.contrib.sites, django.contrib.sitemaps를 추가합니다.
seolpyo_dsotry.settings 파일에 기초설정을 위한 기본 변수들을 작성해놓았으니 이를 활용할 수 있습니다.

별도의 이용자 모델이 없는 경우, AUTH_USER_MODEL을 seolpyo_dstory.User로 선언합니다.

MEDIA_ROOT를 선언합니다.

TEMPLATES > OPTIONS > context_processors에 seolpyo_dstory.processors.get_context를 추가합니다.
또는 seolpyo_dsotry.settings의 processor를 추가합니다.

### 마이그레이션
관리자를 추가하기 위해 마이그레이션을 생성하고, 적용합니다.
>> python manage.py makemigrations
>> python manage.py migrate

#### 관리자 추가하기
createsuperuser 명령을 통해 관리자를 추가합니다.
>> python manage.py createsuperuser

### 티스토리 백업파일을 이용해 글 복구하기
이 패키지는 티스토리 이사를 위한 2가지 방법을 제공합니다.
하나는 백업파일만을 이용한 단순 복구, 다른 하나는 백업파일과 티스토리 블로그에 접속해 공개설정, 비밀번호, 문자 주소 등의 정보를 가져와 적용하는 것입니다.
다운로드한 티스토리 백업파일을 mysite 폴더에 이동시킨 다음, tistory.zip이라는 이름으로 변경합니다.

#### 백업파일을 통한 단순복구
장고 shell을 실행하고, 다음 명령어를 입력합니다.
>> python manage.py shell
>> from seolpyo_dstory.utils import resotre as r
>> r()

#### 백업파일과 티스토리 블로그를 통한 복구
장고 shell을 실행하고, 다음 명령어를 입력합니다.
복구 과정에서 티스토리에 로그인하기 위한 로그인 아이디와 로그인 비밀번호를 요구합니다.
2단계 인증을 사용 중인 경우 로그인에 실패하기 때문에 2단계 인증을 사용하지 않는 계정이어야 합니다.
>> python manage.py shell
>> from seolpyo_dstory.utils import resotre2 as r
>> r()

### 확인하기
장고 프로젝트를 실행하고, 복구된 글을 확인해봅니다.
로컬 서버에서 실행하는 경우 기본 주소는 127.0.0.1:8000입니다.
>> python manage.py runserver


# 샘플 이미지
다음은 해당 패키지를 통해 티스토리 블로그를 이사하여 운영 중인 사이트의 샘플 이미지입니다.
샘플 블로그 : <https://dstory.seolpyo.com/>
티스토리 블로그 : <https://white-seolpyo.tistory.com/>

![이미지 1](https://github.com/white-seolpyo/seolpyo_dstory/blob/main/img1.png?raw=true)
![이미지 2](https://github.com/white-seolpyo/seolpyo_dstory/blob/main/img2.png?raw=true)