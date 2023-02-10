def insertNodeAtHead(llist,data):
    new_node = SinglyLinkedListNode(data) 
    if not llist:  
        return new_node
    new_node.next = llist  
    return new_node

if __name__ == '__main__':


    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print(llist)
    