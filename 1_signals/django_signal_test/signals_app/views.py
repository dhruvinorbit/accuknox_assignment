from django.http import JsonResponse
from .models import SynchronousTestModel, ThreadTestModel, TransactionTestModel
import threading
from django.db import transaction, connection


def test_synchronous_signal(request):
    """
    Question 1
        when the a new object of SynchronousTestModel is created it will run
        synchronous signal method and delay it for 5 seconds.

    Args:
        request (_type_): _description_

    Returns:
        JsonResponse: To show that the whole method ran and ended on the broswer.
    """

    SynchronousTestModel.objects.create(name="Synchronous Test")
    return JsonResponse({"message": "Synchronous signal test completed"})


def test_thread_signal(request):
    """
    Question 2
        Print the thread ID from both the view (caller) and the signal handler, If the thread IDs
        matches this will prove that signals are executed in the same thread.

    Args:
        request (_type_): _description_

    Returns:
        JsonResponse: To show that the whole method ran and ended on the broswer.
    """
    view_thread_id_start = threading.get_ident()
    print(f"[View] Start - Thread ID: {view_thread_id_start}")

    # This will trigger the post_save signal for ThreadTestModel
    ThreadTestModel.objects.create(name="Thread Test")

    view_thread_id_end = threading.get_ident()
    print(f"[View] End - Thread ID: {view_thread_id_end}")

    return JsonResponse({"message": "Thread test completed"})


def test_transaction_signal(request):
    """
    Question3:
    We start a transaction using transaction.atomic() 

    Returns:
        JsonResponse: To show that the whole method ran and ended on the broswer.
    """
    with transaction.atomic():
        # Before saving, we are inside a transaction block
        print(f"[View] Before save - in_atomic_block: {connection.in_atomic_block}")

        # This  triggers the post_save signal for TransactionTestModel.
        TransactionTestModel.objects.create(name="Transaction Test")

        # After saving, still inside the same transaction block.
        print(f"[View] After save - in_atomic_block: {connection.in_atomic_block}")

    return JsonResponse({"message": "Transaction test completed"})
