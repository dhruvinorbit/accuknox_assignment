import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SynchronousTestModel, ThreadTestModel, TransactionTestModel
import threading
from django.db import transaction, connection


@receiver(post_save, sender=SynchronousTestModel)
def synchronous_signal(sender, instance, **kwargs):
    """
    Question 1:
    Added some delay -> ( time.sleep(5)) to expirience delay and proves the signal runs synchronously.
    """
    print("Signal started (synchronous test)")
    time.sleep(5)  # intentional delay
    print("5 seconds have passed!")
    print("Signal executed (synchronous test)")


@receiver(post_save, sender=ThreadTestModel)
def thread_test_signal(sender, instance, **kwargs):
    print(f"Signal (thread test) Thread ID: {threading.get_ident()}")


@receiver(post_save, sender=TransactionTestModel)
def transaction_signal(sender, instance, **kwargs):
    # connection.in_atomic_block is True if we're inside a transaction.atomic() block.
    print(f"[Signal Handler] in_atomic_block: {connection.in_atomic_block}")
