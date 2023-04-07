from django.template.loader import render_to_string
from django.core.signing import Signer

from bboard.settings import ALLOWED_HOSTS

signer = Signer()