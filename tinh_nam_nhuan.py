# Nhập năm từ bàn phím
year = int(input("Nhập năm: "))

# Kiểm tra xem năm có phải là năm nhuận hay không
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Năm", year, "là năm nhuận!")
        else:
            print("Năm", year, "không phải là năm nhuận!")
    else:
        print("Năm", year, "là năm nhuận!")
else:
    print("Năm", year, "không phải là năm nhuận!")
