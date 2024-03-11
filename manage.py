from student import Student

# Tạo danh sách sinh viên
student_list = [
    Student("01", "Chung"),
    Student("02", "Chung02"),
    Student("03", "Chung03"),
    Student("04", "Chung04"),
    Student("05", "Chung05")
]

while True:
    print('''
        0. Thoát chương trình
        1. Thêm sinh viên
        2. Sửa thông tin sinh viên
        3. Xóa sinh viên
        4. Xem thông tin tất cả sinh viên
        5. Tìm kiếm sinh viên
        6. Số lượng sinh viên
    ''')

    select = input("Nhập lựa chọn của bạn: ")

    if not select.isdigit():
        print("Vui lòng nhập số !!!")
    else:
        select = int(select)
        if select < 0 or select > 6:
            print("Vui lòng nhập số có trong hệ thống !!")
        else:
            if select == 0:
                break
            elif select == 1:
                id = input("Nhập ID sinh viên: ")
                name = input("Nhập Tên sinh viên: ")
                sv = Student(id, name)
                student_list.append(sv)

            elif select == 2:
                # Code cho việc sửa thông tin sinh viên
                id_to_find = input("Nhập ID sinh viên cần sua thông tin: ")
                for student in student_list:
                    if student.get_id() == id_to_find:
                        student.set_Name(input("Nhap ten moi: "))
                        student.show_Infor()
                        break
                else:
                    print("Không tìm thấy sinh viên có ID này.")
            elif select == 3:
                # Code cho việc xóa sinh viên
                id_to_find = input("Nhập ID sinh viên cần xoa: ")
                for student in student_list:
                    if student.get_id() == id_to_find:
                        student_list.remove(student)
                        print("Ban da xoa thanh cong")
                        break
                else:
                    print("Không tìm thấy sinh viên có ID này.")
            elif select == 5:
                # Code cho việc xem thông tin sinh viên
                id_to_find = input("Nhập ID sinh viên cần xem thông tin: ")
                for student in student_list:
                    if student.id == id_to_find:
                        student.show_Infor()
                        break
                else:
                    print("Không tìm thấy sinh viên có ID này.")
            elif select == 4:
                # In thông tin tất cả sinh viên
                print("Thông tin tất cả sinh viên:")
                for student in student_list:
                    student.show_Infor()
            elif select == 6:
                print(f"Hiện có {len(student_list)} sinh viên")
