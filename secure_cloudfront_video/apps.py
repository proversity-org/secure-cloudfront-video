"""
App configuration for secure_cloudfront_video.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class SecureCloudfrontVideoConfig(AppConfig):
    """
    Open edX plugin to generate signed video URLs from Amazon Cloudfront. configuration.
    """
    name = 'secure_cloudfront_video'
    verbose_name = 'Open edX plugin to generate signed video URLs from Amazon Cloudfront.'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'secure_cloudfront_video',
                'regex': r'^secure_cloudfront_video/',
                'relative_path': 'urls',
            },
            'cms.djangoapp': {
                'namespace': 'secure_cloudfront_video',
                'regex': r'^secure_cloudfront_video/',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
            'cms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
                'test': {'relative_path': 'settings.test'},
                'aws': {'relative_path': 'settings.aws'},
                'production': {'relative_path': 'settings.production'},
            },
        }
    }
