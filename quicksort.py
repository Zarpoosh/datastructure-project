import random
import time

# تابع partition برای تقسیم کردن آرایه
def partition(array, low, high):
    pivot = array[high]  # انتخاب آخرین عنصر به عنوان محور
    i = low - 1  # شاخص برای عناصر کمتر از محور

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]  # جابجایی عناصر کوچک‌تر به سمت چپ

    array[i + 1], array[high] = array[high], array[i + 1]  # جابجایی محور به مکان مناسب
    return i + 1

# تابع quickSort برای مرتب‌سازی آرایه
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)  # مکان محور بعد از تقسیم
        quickSort(array, low, pi - 1)     # مرتب‌سازی نیمه چپ
        quickSort(array, pi + 1, high)    # مرتب‌سازی نیمه راست

# تابع جستجوی باینری
def binary_search(arr, target, low, high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid  # یافتن شاخص عدد مورد نظر
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid - 1)  # جستجو در نیمه چپ
        else:
            return binary_search(arr, target, mid + 1, high)  # جستجو در نیمه راست
    else:
        return -1  # عدد مورد نظر یافت نشد

# اجرای برنامه با داده‌های ورودی
data = [random.randint(0, 100) for _ in range(50)]
print("Unsorted Array")
print(data)

# مرتب‌سازی داده‌ها
size = len(data)
quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)

# دریافت عدد از کاربر و اندازه‌گیری زمان جستجو
target = int(input("یک عدد از ۰ تا ۹ وارد کنید: "))
start_time = time.time()  # شروع زمان جستجو
index = binary_search(data, target, 0, size - 1)
end_time = time.time()  # پایان زمان جستجو

# محاسبه و نمایش زمان جستجو
search_time = end_time - start_time
if index != -1:
    print(f"عدد {target} در شاخص {index} پیدا شد.")
else:
    print(f"عدد {target} در لیست موجود نیست.")
print(f"زمان جستجو: {search_time:.10f} ثانیه")
