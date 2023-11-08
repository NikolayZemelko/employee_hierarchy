from django.db import models
from django.utils.translation import gettext as _


class Employee(models.Model):
    JUNIOR = "JR"
    MIDDLE = "MD"
    SENIOR = "SR"

    TITLES = [
        (JUNIOR, _("Junior")),
        (MIDDLE, _("Middle")),
        (SENIOR, _("Senior"))
    ]
    first_name = models.CharField(
        max_length=150
    )

    last_name = models.CharField(
        max_length=150
    )

    job_title = models.CharField(
        max_length=100,
        choices=TITLES,
        default=JUNIOR
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    date_offered = models.DateField(
        editable=False,
    )
    salary = models.IntegerField()
    supervisor = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='employees'
    )

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(
                salary__gte=50000), name="salary_gte_50000_RUB")
        ]
        indexes = [
            models.Index(fields=["first_name", "last_name"]),
            models.Index(fields=["last_name", "salary"]),
            models.Index(fields=["last_name", "job_title"])
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
