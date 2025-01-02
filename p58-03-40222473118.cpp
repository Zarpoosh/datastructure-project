// سؤال: برنامه‌ای بنویسید که یک مثلث متقارن از ستاره‌ها به تعداد مشخصی ردیف چاپ کند. به طوری که کاربر تعداد ردیف‌ها را وارد کند.


#include <iostream>
using namespace std;

int main() {
    int rows;
    cout << "Enter the number of rows: ";
    cin >> rows;

    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= rows - i; j++) {
            cout << " "; // Print spaces
        }
        for (int k = 1; k <= (2 * i - 1); k++) {
            cout << "*"; // Print stars
        }
        cout << endl;
    }
    return 0;
}



