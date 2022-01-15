import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car.settings')
application = get_wsgi_application()

application = WhiteNoise(application, root='/web/car')
application.add_files('/web/car/static/', prefix='')