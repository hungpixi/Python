sinh_vien = ["Hường", "Phương Anh", "Hồng Nga", "Long", "Hiếu", "Khôi"]
diem_toan = [9, 8, 7, 8, 9, 9]
diem_ly = [10, 8, 9, 9, 8, 10]
diem_hoa = [9, 10, 8, 9, 9, 9]

# In ra tên của sinh viên thứ 3
ten_sinh_vien_3 = sinh_vien[2]
print("Tên của sinh viên thứ 3 là:", ten_sinh_vien_3)

# In ra điểm hóa của sinh viên cuối cùng
diem_hoa_sinh_vien_cuoi_cung = diem_hoa[-1]
print("Điểm hóa của sinh viên cuối cùng là:", diem_hoa_sinh_vien_cuoi_cung)

# Tính điểm trung bình của sinh viên đầu tiên
diem_trung_binh = (diem_toan[0] + diem_ly[0] + diem_hoa[0]) / 3
print("Sinh viên", sinh_vien[0], "có điểm trung bình là:", diem_trung_binh)
