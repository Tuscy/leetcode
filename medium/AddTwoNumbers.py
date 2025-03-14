# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        #While there is still values in the linked list or a carry
        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry #Get the sum of the current pointers
            digit = sum % 10 #Calculate the value < 10 using modulo
            carry = sum // 10 #Getting the remainder (to be carried)

            newNode = ListNode(digit) #Create a new node to store the value
            tail.next = newNode #Store the newNode as the tail of the previous node
            tail = tail.next #Set the tail to current node (making it the tail again)

            #Find the next nodes in the list (unless None)
            l1 = l1.next if l1 is not None else None 
            l2 = l2.next if l2 is not None else None

        
        result = dummyHead.next #Sets the output to the first node in the list
        dummyHead.next = None #Remove the dummy node from the list
        return result