from django.db.models import TextChoices


class LevelChoices(TextChoices):
    Junior = 'Junior'
    Junior_plus = 'Junior+'
    Middle = 'Middle'
    Middle_plus = 'Middle+'
    Senior = 'Senior'
    Senior_plus = 'Senior+'
