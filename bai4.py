# (1) Phân tích thiết kế hàm
# Tên hàm: calculate_average(student)
# Input: student (dictionary chứa thông tin sinh viên).
# Output: float (điểm trung bình của sinh viên).
# Mô tả luồng xử lý: Lấy điểm Toán, Lý, Hóa từ dictionary sinh viên, tính trung bình cộng của 3 môn rồi trả về kết quả bằng lệnh return.
# Tên hàm: get_rank(average)
# Input: average (float).
# Output: string.
# Mô tả luồng xử lý: Kiểm tra điểm trung bình. Nếu từ 8.0 trở lên trả về "Giỏi", từ 6.5 đến dưới 8.0 trả về "Khá", từ 5.0 đến dưới 6.5 trả về "Trung bình", còn lại trả về "Yếu".
# Tên hàm: display_grades(records)
# Input: records (list chứa các dictionary sinh viên).
# Output: None.
# Mô tả luồng xử lý: Kiểm tra danh sách có rỗng hay không. Nếu rỗng hiển thị thông báo dữ liệu trống. Nếu có dữ liệu thì duyệt từng sinh viên, gọi hàm calculate_average() để tính ĐTB, gọi hàm get_rank() để lấy học lực và hiển thị bảng điểm.
# Tên hàm: update_student_score(records)
# Input: records (list chứa các dictionary sinh viên).
# Output: None.
# Mô tả luồng xử lý: Nhập mã sinh viên, chuẩn hóa dữ liệu bằng strip() và upper(), tìm sinh viên trong danh sách. Nếu không tìm thấy thì báo lỗi. Nếu tìm thấy thì yêu cầu chọn môn học, nhập điểm mới, kiểm tra hợp lệ rồi cập nhật điểm cho sinh viên.
# Tên hàm: generate_report(records)
# Input: records (list chứa các dictionary sinh viên).
# Output: None.
# Mô tả luồng xử lý: Kiểm tra danh sách rỗng. Nếu có dữ liệu thì duyệt toàn bộ sinh viên, tính ĐTB bằng hàm calculate_average(), đếm số lượng sinh viên đỗ và trượt, tính tỷ lệ phần trăm rồi hiển thị báo cáo.
# Tên hàm: find_valedictorian(records)
# Input: records (list chứa các dictionary sinh viên).
# Output: None.
# Mô tả luồng xử lý: Kiểm tra danh sách rỗng. Nếu có dữ liệu thì tìm sinh viên có điểm trung bình cao nhất bằng hàm calculate_average(), sau đó hiển thị thông tin thủ khoa.
# # (2) Triển khai code

student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]


def calculate_average(student):
    return (
        student["math"] +
        student["physics"] +
        student["chemistry"]
    ) / 3


def get_rank(average):
    if average >= 8:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5:
        return "Trung bình"
    return "Yếu"


def display_grades(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):
        average = calculate_average(student)
        rank = get_rank(average)

        print(
            f"{index}. [{student['student_id']}] {student['name']} | "
            f"Toán: {student['math']} | "
            f"Lý: {student['physics']} | "
            f"Hóa: {student['chemistry']} | "
            f"ĐTB: {average:.2f} - {rank}"
        )

def input_score():
    while True:
        try:
            score = float(input("Nhập điểm mới: "))

            if 0 <= score <= 10:
                return score

            print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")

        except ValueError:
            print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")


def update_student_score(records):
    student_id = input(
        "Nhập mã sinh viên cần cập nhật: "
    ).strip().upper()

    student = None

    for item in records:
        if item["student_id"] == student_id:
            student = item
            break

    if student is None:
        print(
            f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!"
        )
        return

    print("1. Toán")
    print("2. Lý")
    print("3. Hóa")

    subject = input("Chọn môn học: ")

    if subject == "1":
        score = input_score()
        student["math"] = score
        print(
            f"Đã cập nhật điểm Toán của sinh viên '{student['name']}' thành {score}."
        )

    elif subject == "2":
        score = input_score()
        student["physics"] = score
        print(
            f"Đã cập nhật điểm Lý của sinh viên '{student['name']}' thành {score}."
        )

    elif subject == "3":
        score = input_score()
        student["chemistry"] = score
        print(
            f"Đã cập nhật điểm Hóa của sinh viên '{student['name']}' thành {score}."
        )

    else:
        print("Lựa chọn môn học không hợp lệ!")


def generate_report(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    passed = 0
    failed = 0

    for student in records:
        average = calculate_average(student)

        if average >= 5:
            passed += 1
        else:
            failed += 1

    total = len(records)

    passed_percent = (passed / total) * 100
    failed_percent = (failed / total) * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total}")
    print(
        f"Số lượng qua môn (ĐTB >= 5.0): {passed} sinh viên ({passed_percent:.2f}%)"
    )
    print(
        f"Số lượng trượt (ĐTB < 5.0): {failed} sinh viên ({failed_percent:.2f}%)"
    )

def find_valedictorian(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    top_student = records[0]
    top_average = calculate_average(records[0])

    for student in records:
        average = calculate_average(student)

        if average > top_average:
            top_average = average
            top_student = student

    print("\n--- VINH DANH THỦ KHOA ---")
    print(
        f"Sinh viên: {top_student['name']} (Mã: {top_student['student_id']})"
    )
    print(f"Điểm Trung Bình: {top_average:.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")
    print("--------------------------")


def display_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
    print("1. Xem bảng điểm và học lực")
    print("2. Cập nhật điểm thi sinh viên")
    print("3. Báo cáo thống kê (Đỗ/Trượt)")
    print("4. Tìm sinh viên Thủ khoa")
    print("5. Thoát chương trình")

def main():
    while True:
        display_menu()
        choice = input("Chọn chức năng (1-5): ")
        match choice:
            case "1":
                display_grades(student_records)
            case "2":
                update_student_score(student_records)
            case "3":
                generate_report(student_records)
            case "4":
                find_valedictorian(student_records)
            case "5":
                print("Cảm ơn bạn đã sử dụng hệ thống!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")
main()
