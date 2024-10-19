DSTORY_SLUG = False

DSTORY_PAGE = 8

DSTORY_ORDER = ['-date_pub', '-pk']

DSTORY_WIDGET = 'django_summernote.widgets.SummernoteWidget'
DSTORY_FORM = 'seolpyo_dstory.forms.PostForm'
DSTORY_FORM_SEARCH = 'seolpyo_dstory.forms.SearchForm'

DSTORY_LOGIN_NAME = 'seolpyo_dstory:login'
DSTORY_LOGOUT_NAME = 'seolpyo_dstory:logout'

DSTORY_FAVICON = ''
DSTORY_NAVER = ''
DSTORY_RSS = 50
DSTORY_CONTEXT = {
    'site_name': '디스토리',
    'adsense': '',
}
DSTORY_ROBOTS = """
user-agent: *
DISALLOW: /admin/
"""

DSOTRY_LIGHTBOX = {
    'alwaysShowNavOnTouchDevices': False,
    'albumLabel': '%2개 중 %1번째 이미지',
    'disableScrolling': False,
    'fadeDuration': 100,
    'fitImagesInViewport': True,
    'imageFadeDuration': 100,
    'maxWidth': '',
    'maxHeight': '',
    'positionFromTop': 50,
    'resizeDuration': 100,
    'showImageNumberLabel': True,
    'wrapAround': False
}


