from setuptools import setup, find_packages

MODULE_NAME = 'seolpyo_dstory'
CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.10',
]

setup(
    name='설표 디스토리',
    version='0.0.1',
    description='백업파일을 이용하여 티스토리 블로그를 장고로 이사하기 위한 패키지입니다.',
    author='white-seolpyo',
    author_email='white-seolpyo@naver.com',
    url='https://github.com/white-seolpyo/seolpyo_dstory',
    install_requires=['tqdm', 'BeautifulSoup', 'requests', 'selenium', 'django', 'django-summernote',],
    packages=find_packages(exclude=[]),
    keywords=['장고', '티스토리', '디스토리', '설표', '하얀설표'],
    python_requires='>=3.10',
    package_data={},
    zip_safe=False,
    classifiers=CLASSIFIERS,
)
