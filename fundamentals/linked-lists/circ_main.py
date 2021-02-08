import circ_linked_list as cll
cllist = cll.CircularLinkedList()
cllist.print_list()

a = cll.Node("a")
b = cll.Node("b")
c = cll.Node("c")
d = cll.Node("d")

a.next = b
b.next = c
c.next = d
d.next = a

cllist.head = a
cllist.print_list()

cllist.print_list(b)

cllist.print_list(d)
