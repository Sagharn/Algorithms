//third recursive Question

#include <iostream>
using namespace std;
int fibonacci(int n) {
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;
    cin >> n;
    int fib_num = fibonacci(n);
    cout<< fib_num << endl;

    return 0;
}

