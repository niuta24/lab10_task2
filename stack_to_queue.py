"""
Stack to queue converter.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack
from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue
import copy

def stack_to_queue(stack):
    """A stack to queue converter.
    """
    queue = ArrayQueue()
    change_stack = copy.deepcopy(stack)
    for i in range(len(change_stack)):
        queue.add(change_stack.pop())
    return queue