
// سؤال: برنامه‌ای بنویسید که تعداد n عدد را از کاربر بگیرد و میانگین آن‌ها را محاسبه و نمایش دهد.

#include <iostream>
using namespace std;

int main() {
    int n;
    double x, sum = 0;

    cout << "Enter the number of elements (n): ";
    cin >> n;

    cout << "Enter " << n << " numbers to calculate their average:" << endl;
    for (int i = 0; i < n; i++) {
        cin >> x;
        sum += x;
    }

    double average = sum / n;
    cout << "The average of the entered numbers is: " << average << endl;

    return 0;
}
