

class Solution {

    public static class ListNode {
        int value;
        ListNode next;

        ListNode() {}

        ListNode(int value) {
            this.value = value;
            next = null;
        }

        ListNode(int value, ListNode next) {
            this.value = value; 
            this.next = next;
        }
    }

    public static class CustomLinkedList {
        private ListNode head;
        private int size;

        public CustomLinkedList() 
        {
            head = null;
            size = 0;
        }

        public void insert(int value)
        {
            ListNode newNode = new ListNode(value);

            if (head == null)
            {
                head = newNode;
            }
            else
            {
                ListNode tempNode = head;
                while (tempNode.next != null) // traverse the list until the last element
                {
                    tempNode = tempNode.next;
                }
                tempNode.next = newNode;
            }
            size++;
        }

        public int getSize()
        {
            return this.size;
        }

        public void printList() 
        { 
            ListNode currentNode = head; 
    
            System.out.print("LinkedList: "); 
    
            // Traverse through the LinkedList 
            while (currentNode != null) { 
                // Print the data at current node 
                System.out.print(currentNode.value + " "); 
    
                // Go to next node 
                currentNode = currentNode.next; 
            } 
        } 

        public ListNode findMiddleNode()
        {
            if (head == null)
                return null;
            
            //ListNode middleNode = new ListNode();

            ListNode slowPtr = head;
            ListNode fastPtr = head;

            //while (fastPtr != null)
            while (fastPtr != null && fastPtr.next != null)
            {
                slowPtr = slowPtr.next;
                fastPtr = fastPtr.next.next;
            }

            //middleNode = slowPtr;
            //middleNode.value = slowPtr.value;

            return slowPtr;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        CustomLinkedList myList = new CustomLinkedList();
        myList.insert(5);
        myList.insert(15);
        myList.insert(3);
        myList.printList();
        System.out.println("\nMiddle node is " + myList.findMiddleNode().value);

        myList.insert(56);
        myList.printList();
        System.out.println("\nMiddle node is " + myList.findMiddleNode().value);
    }
}
