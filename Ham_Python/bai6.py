class SinhVien:
    def __init__(self, ma_sv, ten_sv, gioi_tinh, lop, tuoi):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.gioi_tinh = gioi_tinh
        self.lop = lop
        self.tuoi = tuoi

    def cap_nhat_sinh_vien(self, ma_sv, ten_sv, gioi_tinh, lop, tuoi):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.gioi_tinh = gioi_tinh
        self.lop = lop
        self.tuoi = tuoi

# Tạo một đối tượng SinhVien
sv = SinhVien("SV001", "Nguyen Van A", "Nam", "K42", 20)

# In thông tin của SinhVien
print(f"Thông tin sinh viên: {sv.ma_sv}, {sv.ten_sv}, {sv.gioi_tinh}, {sv.lop}, {sv.tuoi}")

# Cập nhật thông tin sinh viên
sv.cap_nhat_sinh_vien("SV002", "Tran Thi B", "Nu", "K43", 21)

# In lại thông tin sau khi cập nhật
print(f"Thông tin sinh viên sau cập nhật: {sv.ma_sv}, {sv.ten_sv}, {sv.gioi_tinh}, {sv.lop}, {sv.tuoi}")