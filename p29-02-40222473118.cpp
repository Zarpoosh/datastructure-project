// سؤال: برنامه‌ای بنویسید که 50 عدد از کاربر بگیرد و مجموع آن‌ها را محاسبه و نمایش دهد.

#include <iostream>
using namespace std;

int main() {
    double x, sum = 0;
    int i;

    cout << "Enter 50 numbers to calculate their sum:" << endl;
    for (i = 0; i < 50; i++) {
        cin >> x;
        sum += x;
    }

    cout << "The sum of the entered numbers is: " << sum << endl;

    return 0;
}
