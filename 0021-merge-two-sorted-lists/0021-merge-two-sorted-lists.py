from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
        
            current = current.next
    
        if list1:
            current.next = list1
        if list2:
            current.next = list2
    
        return dummy_head.next

# Примеры связанных списков
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Создаем экземпляр класса Solution
solution = Solution()

# Вызываем метод для объединения списков
merged_list = solution.mergeTwoLists(list1, list2)

# Выводим результат
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
print("None")
