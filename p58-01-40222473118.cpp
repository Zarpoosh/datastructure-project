#include <iostream>
using namespace std;

int main() {
    int i, j;
    for (i = 20; i > 0; i--) {
        for (j = 0; j < i; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
