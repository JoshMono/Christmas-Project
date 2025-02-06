from django.db import models

# Create your models here.

class Company(models.Model):

    class IndustryChoices(models.TextChoices):
        MANUFACTURING = 'M', 'Manufacturing'
        FINANCE = 'F', 'Finance'
        OTHER = 'O', 'Other'
    
    name = models.TextField(verbose_name="Company Name")
    industry = models.CharField(verbose_name="Industry", choices=IndustryChoices.choices, max_length=100)
    
    def __str__(self) -> str:
        return f"{self.name}"

class Person(models.Model):
    first_name = models.TextField(verbose_name="First Name")
    last_name = models.TextField(verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email")
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name="people")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
