"""
Module containing common Exceptions for secure-cloudfront-video.
"""

class MissingCloudFrontInformationError(Exception):
    """
    Exception class raised when some of the required information
    by Amazon CloudFront were not provided.
    """
    pass
