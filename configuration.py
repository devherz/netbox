cat > configuration.py << 'EOF'
import os

# Database configuration
DATABASE = {
    'NAME': 'ipam_obf_db',
    'USER': 'netbox',
    'PASSWORD': 'Balkuy@7',
    'HOST': '',
    'PORT': '',
    'CONN_MAX_AGE': 300,
}

# Redis configuration
REDIS = {
    'tasks': {
        'HOST': 'localhost',
        'PORT': 6379,
        'PASSWORD': '',
        'DATABASE': 0,
        'SSL': False,
    },
    'caching': {
        'HOST': 'localhost',
        'PORT': 6379,
        'PASSWORD': '',
        'DATABASE': 1,
        'SSL': False,
    }
}

# Secret key (generate a new one for production)
SECRET_KEY = 'k9x7z#3m$p8@w2c5v!n6j4h1q7r0s8t9u2y5x1z3c6v9b2n4m7k0l3p6s9w2e5r8t1y4u7i0o3p6s9w2e5'

# Allowed hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'HERZ']

# Debug mode (set to False in production)
DEBUG = False

# Base URL
BASE_PATH = ''

# Time zone
TIME_ZONE = 'UTC'
EOF
