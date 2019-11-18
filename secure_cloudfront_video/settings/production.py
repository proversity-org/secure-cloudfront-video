"""
Production Django settings for secure_cloudfront_video project.
"""

from __future__ import unicode_literals


def plugin_settings(settings):
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """
    settings.SCV_CLOUDFRONT_ID = getattr(settings, 'ENV_TOKENS', {}).get(
        'SCV_CLOUDFRONT_ID',
        settings.SCV_CLOUDFRONT_ID,
    )
    settings.SCV_CLOUDFRONT_URL = getattr(settings, 'ENV_TOKENS', {}).get(
        'SCV_CLOUDFRONT_URL',
        settings.SCV_CLOUDFRONT_URL,
    )
    settings.SCV_CLOUDFRONT_PRIVATE_SIGNING_KEY = getattr(settings, 'AUTH_TOKENS', {}).get(
        'SCV_CLOUDFRONT_PRIVATE_SIGNING_KEY',
        settings.SCV_CLOUDFRONT_PRIVATE_SIGNING_KEY,
    )
