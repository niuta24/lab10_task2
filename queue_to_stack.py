"""
Queue to stack converter.
"""

from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack    # or from linkedstack import LinkedStack
import copy

def queue_to_stack(queue):
    """A queue to stack converter."""
    stack = ArrayStack()
    change_queue = copy.deepcopy(queue)
    for i in range(len(change_queue)):
        stack.push(change_queue.peek())
        change_queue.pop()
    return stack
