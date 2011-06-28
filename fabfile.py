from armstrong.dev.tasks import *

full_name = "armstrong.apps.audio.backends.mutagen"
settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'armstrong.core.arm_content',
        'armstrong.core.arm_content.tests.arm_content_support',
        'armstrong.core.arm_sections',
        'armstrong.utils.backends',
        full_name,
        'south',
        'mptt',
    ),
    'SITE_ID': 1,
    'ROOT_URLCONF': 'armstrong.core.arm_content.tests.arm_content_support.urls',
    'AUTH_PROFILE_MODULE': 'arm_content_support.SimpleProfile',
    'ARMSTRONG_EXTERNAL_VIDEO_BACKEND': 'armstrong.core.arm_content.video.backends.YouTubeBackend',
    'ARMSTRONG_EXTERNAL_AUDIO_METADATA_BACKEND':'armstrong.apps.audio.backends.mutagen.MutagenBackend',

}


main_app = "arm_content"
tested_apps = ("arm_content_support", "arm_content",)
pip_install_first = True
