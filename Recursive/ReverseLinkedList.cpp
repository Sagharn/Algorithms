// time complexity : O(n)
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;

    Node(int val) : data(val), next(nullptr) {}
};


void printReverseLinkedList(Node* current) {
    if (current == nullptr) {
        return;
    }


    printReverseLinkedList(current->next);

    cout << current->data << " ";
}

int main() {

    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);


    printReverseLinkedList(head);


    delete head->next->next->next;
    delete head->next->next;
    delete head->next;
    delete head;

    return 0;
}
