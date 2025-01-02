



// سؤال: برنامه‌ای بنویسید که یک مربع توخالی از ستاره‌ها چاپ کند. تعداد ردیف‌ها و ستون‌های مربع باید توسط کاربر وارد شود.


#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the size of the square: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == 1 || i == n || j == 1 || j == n) {
                cout << "*"; // Print stars for boundary
            } else {
                cout << " "; // Print spaces for inside
            }
        }
        cout << endl;
    }
    return 0;
}
