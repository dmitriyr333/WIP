  def reverse(head):

        current = head
        previous = None

       while current:
         next = current.next
         current.next = previous   # None, first time round.
         previous = current        # Used in the next iteration.
         current = next            # Move to next node.

       head = previous
