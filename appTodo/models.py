from django.db import models

class Task(models.Model):
    STATUS_CHOICE = (
        ('dn', 'Completo'),
        ('ic', 'Incompleto'),
        ('ip', 'Em Andamento')
    )
    
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    status = models.CharField(max_length=2, choices=STATUS_CHOICE, null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['status']