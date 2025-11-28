import os
import shutil
import sys



def copy_files_recursive(src_dir, dst_dir):
    try:
        items = os.listdir(src_dir)
    except Exception as e:
        print(f"Помилка доступу до директорії {src_dir}: {e}")
        return

    for item in items:
        full_path = os.path.join(src_dir, item)

        if os.path.isdir(full_path):  # якщо це папка-викликаємо функцію ще раз
            copy_files_recursive(full_path, dst_dir)
        else:
            
            # якщо це файл – копіюємо його
            ext = os.path.splitext(item)[1].lower().replace(".", "")
            if ext == "":
                ext = "no_ext"

            target_folder = os.path.join(dst_dir, ext)

            try:
                os.makedirs(target_folder, exist_ok=True)
                shutil.copy2(full_path, target_folder)
                print(f"Скопійовано: {item} → {target_folder}")
            except Exception as e:
                print(f"Помилка копіювання {item}: {e}")



def main():
    if len(sys.argv) < 2:
        print("Використання: python script.py <source_folder> [destination_folder]")
        return

    src = sys.argv[1]

    if len(sys.argv) >= 3:
        dst = sys.argv[2]
    else:
        dst = "dist"

    if not os.path.exists(src):
        print("Вихідна директорія не існує.")
        return

    os.makedirs(dst, exist_ok=True)

    print("...Копіювання...\n")
    copy_files_recursive(src, dst)
    print("\n Файли скопійовано")




if __name__ == "__main__":
    main()
