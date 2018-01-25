# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create,
#     modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field
# names.
from django.db import models


class JobLog(models.Model):
    job_id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(blank=True, null=True)
    status = models.TextField()
    status_message = models.TextField(blank=True, null=True)
    bulk_or_delta = models.TextField()
    log_file = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_log'

    def __str__(self):
        return (str(self.job_id) + ': ' + self.bulk_or_delta + ' - ' +
                self.status + ' (' + str(self.start_datetime) + ')')


class JobSchedule(models.Model):
    job_id = models.IntegerField(primary_key=True)
    sequence = models.AutoField(primary_key=True)
    function_name = models.TextField()
    stage = models.TextField()
    status = models.TextField()
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_schedule'
        unique_together = (('job_id', 'sequence'),)
