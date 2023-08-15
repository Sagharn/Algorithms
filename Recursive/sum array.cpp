#include <iostream>
using namespace std;
int sumArray(int arr[], int size) {

    if (size <= 0) {
        return 0;
    }
    
    return arr[size - 1] + sumArray(arr, size - 1);
}

int main() {
    int size;
    cin >> size;
    
    int arr[size];
    cout << endl;
    for (int i = 0; i < size; i++) {
        cin >> arr[i];
    }
    
    int totalSum = sumArray(arr, size);
    cout<< totalSum << endl;
    
    return 0;
}
