// time complexity : O(n)
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    
    Node(int val) : data(val), next(nullptr) {}
};


void printLinkedList(Node* current) {
    if (current == nullptr) {
        return;
    }
    
    cout << current->data << " ";
    printLinkedList(current->next);   
}

int main() {
    
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);
    
   
    printLinkedList(head);
    

    delete head->next->next->next;
    delete head->next->next;
    delete head->next;
    delete head;
    
    return 0;
}
