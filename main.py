import pickle

# تحميل المهام من الملف إذا كان موجوداً
def load_tasks():
    try:
        with open('tasks.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

# حفظ المهام إلى الملف
def save_tasks(tasks):
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks, f)

# إضافة مهمة
def add_task(task, tasks):
    tasks.append(task)
    save_tasks(tasks)

# حذف مهمة
def remove_task(task, tasks):
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
    else:
        print("المهمة غير موجودة في القائمة.")

# عرض المهام
def show_tasks(tasks):
    if tasks:
        print("قائمة المهام:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("لا توجد مهام في القائمة.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. عرض المهام")
        print("2. إضافة مهمة")
        print("3. حذف مهمة")
        print("4. الخروج")
        choice = input("اختر عملية (1/2/3/4): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            task = input("أدخل المهمة الجديدة: ")
            add_task(task, tasks)
        elif choice == '3':
            show_tasks(tasks)
            task_index = int(input("اختر رقم المهمة لحذفها: "))
            if 1 <= task_index <= len(tasks):
                remove_task(tasks[task_index - 1], tasks)
            else:
                print("الرقم غير صحيح.")
        elif choice == '4':
            print("إلى اللقاء!")
            break
        else:
            print("اختيار غير صحيح. حاول مرة أخرى.")

if __name__ == "__main__":
    main()
