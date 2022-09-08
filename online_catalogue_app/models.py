from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


#  default variables for position
intern = 'INTERN'
junior = 'JUNIOR'
middle = 'MIDDLE'
senior = 'SENIOR'
team_lead = 'TEAM-LEAD'


class BossModel(models.Model):
    boss_full_name = models.CharField(max_length=255)

    class Meta:
        db_table = "boss_table"
        verbose_name = "Boss"
        verbose_name_plural = "Bosses"

    def __str__(self):
        return "Boss name #%s: %s; \n\t\t" % (self.id, self.boss_full_name)


class EmployeeModel(models.Model):
    POSITION_CHOICES = (
        (intern, 'intern'),
        (junior, 'junior'),
        (middle, 'middle'),
        (senior, 'senior'),
        (team_lead, 'team-lead')
    )

    emp_full_name = models.CharField(max_length=255, null=False, db_column="emp_full_name")
    position = models.CharField(max_length=255, db_column="position", choices=POSITION_CHOICES, default="JUNIOR")
    date_of_employment = models.DateField(auto_now=False, db_column="date_of_employment")
    wage = models.FloatField(db_column="wage", validators=[MaxValueValidator(3000), MinValueValidator(500)])
    boss_name = models.ForeignKey(BossModel, on_delete=models.CASCADE, db_column="boss_name")

    USERNAME_FIELD = 'emp_full_name'

    class Meta:
        db_table = "employee_table"