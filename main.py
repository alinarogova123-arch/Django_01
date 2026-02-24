import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402


def main():
    passcards = Passcard.objects.all()
    active_passcards = passcards.filter(is_active=True)
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    print('Активных пропусков:', len(active_passcards))


if __name__ == '__main__':
    main()
