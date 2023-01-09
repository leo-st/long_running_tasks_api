from datetime import timedelta
import os


class Config(object):
    DEVELOPMENT = os.getenv("DEVELOPMENT", 'True').lower() in ('true', '1', 't')
    DEBUG = os.getenv("DEBUG", 'True').lower() in ('true', '1', 't')
    TESTING = os.getenv("TESTING", 'True').lower() in ('true', '1', 't')
    CSRF_ENABLED = os.getenv("CSRF_ENABLED", 'False').lower() in ('true', '1', 't')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024 # 10mb max content length
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6380) )
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", 'super-secret')
