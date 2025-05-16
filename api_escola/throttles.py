# api_escola/throttles.py
from rest_framework.throttling import AnonRateThrottle

class MatriculaAnonRateThrottle(AnonRateThrottle):
    rate = '5/min'