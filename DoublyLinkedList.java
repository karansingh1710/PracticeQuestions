
class Node{
    Node next,prev;
    int data;
    Node(int data){
        this.data=data;
        next=null;
        prev=null;
    }
}

public class DoublyLinkedList {
    Node head;

    void addInFirst(int data){
        Node newNode=new Node(data);
        if (head==null) {
            head=newNode;
            return;
        }
        newNode.next=head;
        head.prev=newNode;
        head=newNode;
    }

    void  addInLast(int data){
        Node newNode=new Node(data);
        if(head==null){
            head=newNode;
            return;
        }
        Node temp=head;
        while (temp.next!=null) {
            temp=temp.next;
        }
        temp.next=newNode;
        newNode.prev=temp;
    }

    void display(){
        Node temp=head;
        while (temp!=null) {
            System.out.print(temp.data+" ");
            temp=temp.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        DoublyLinkedList dl=new DoublyLinkedList();
        dl.addInLast(23);
        dl.addInLast(20);
        dl.display();
        dl.addInFirst(12);
        dl.display();
        dl.addInFirst(5);
        dl.display();
    }
    
}