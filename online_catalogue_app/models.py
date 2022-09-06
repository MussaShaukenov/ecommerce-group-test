from django.db import models


class BossModel(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    boss_full_name = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "boss_table"
        verbose_name = "Boss"
        verbose_name_plural = "Bosses"

    def __str__(self):
        return "Boss name #%s: %s; \n\t\t" % (self.id, self.boss_full_name)


class EmployeeModel(models.Model):
    emp_full_name = models.CharField(max_length=255, null=False, db_column="emp_full_name")
    position = models.CharField(max_length=255, db_column="position")
    date_of_employment = models.DateField(auto_now=False, db_column="date_of_employment")
    wage = models.FloatField(db_column="wage")
    boss_name = models.ForeignKey(BossModel, on_delete=models.CASCADE, db_column="boss_name")

    class Meta:
        db_table = "employee_table"

    def __str__(self):
        return self.emp_full_name
