from django.db import models

# We created saperate model because if me do not and use a single model to execute our single url it will also run other view since they are all connected to a single signal that uses same Model.


class SynchronousTestModel(models.Model):
    name = models.CharField(max_length=100)


class ThreadTestModel(models.Model):
    name = models.CharField(max_length=50)


class TransactionTestModel(models.Model):
    name = models.CharField(max_length=200)
