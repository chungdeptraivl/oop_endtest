class CongDoan:
    list_CD = []

    def __init__(self, tenCD, tenCasi, tenBaiHat, GiaThanh):
        self.tenCD = tenCD
        self.tenCasi = tenCasi
        self.tenBaiHat = tenBaiHat
        self.GiaThanh = int(GiaThanh)

    def set_tenCD(self, tenCD):
        self.tenCD = tenCD

    def set_tenCasi(self, tenCaSi):
        self.tenCasi = tenCaSi

    def set_tenBaiHat(self, tenBaiHat):
        self.tenBaiHat = tenBaiHat

    def set_GiaThanh(self, GiaThanh):
        self.GiaThanh = GiaThanh

    @classmethod
    def show_list(cls):
        print("Danh sách CD:")
        for i, cd in enumerate(cls.list_CD, start=1):
            print(f"{i}. {cd.tenCD} - {cd.tenCasi} - {cd.tenBaiHat} - {cd.GiaThanh}")

    @classmethod
    def add_cd(cls, cd):
        cls.list_CD.append(cd)

    @classmethod
    def find_cd(cls, tenCdUpdate):
        for cd in cls.list_CD:
            if cd.tenCD == tenCdUpdate:
                return cd
        return None

    @classmethod
    def sum_price(cls):
        tongGiaThanh = 0
        for i in CongDoan.list_CD:
            tongGiaThanh += i.GiaThanh
        print(f"Tong gia thanh: {tongGiaThanh}")


CongDoan.list_CD = [
    CongDoan("as", "chung", "chung", 123),
    CongDoan("as1", "chung", "chung", 123),
    CongDoan("as2", "chung", "chung", 123),
    CongDoan("as3", "chung", "chung", 123),
    CongDoan("as4", "chung", "chung", 123),
]

while True:
    print('''
        Menu lựa chọn:
        0. Thoát chương trình
        1. Thêm CD
        2. Sửa CD
        3. Xóa CD
        4. In danh sách CD
        5. Tìm CD
        6. Tổng giá thành
    ''')

    select = input("Nhập vào lựa chọn của bạn: ")

    if not select.isdigit():
        print("Yêu cầu nhập vào một số nguyên")
    else:
        select = int(select)
        if select < 0 or select > 6:
            print("Nhập vào một lựa chọn có trong Menu")
        else:
            if select == 0:
                break
            elif select == 1:
                print("Thông tin CD")
                tenCD = input("Nhập vào tên CD: ")
                tenCaSi = input("Nhập vào tên Ca Sĩ: ")
                tenBaiHat = input("Nhập vào tên bài hát: ")
                giaThanh = int(input("Nhập vào giá thành: "))

                cd = CongDoan(tenCD, tenCaSi, tenBaiHat, giaThanh)
                CongDoan.add_cd(cd)
            elif select == 2:
                tenCdUpdate = input("Nhập vào tên CD cần sửa: ")
                cd = CongDoan.find_cd(tenCdUpdate)
                if cd:
                    cd.set_tenCD(input("Nhập tên CD mới: "))
                    cd.set_tenCasi(input("Nhập tên Ca Sĩ mới: "))
                    cd.set_tenBaiHat(input("Nhập tên bài hát mới: "))
                    cd.set_GiaThanh(input("Nhập giá thành mới: "))
                else:
                    print("Tên CD không tồn tại !!!")
            elif select == 3:
                tenCdUpdate = input("Nhập vào tên CD cần xóa: ")
                cd = CongDoan.find_cd(tenCdUpdate)
                if cd:
                    CongDoan.list_CD.remove(cd)
                    print("Xóa thành công <3")
                else:
                    print("Tên CD không tồn tại !!!")
            elif select == 4:
                CongDoan.show_list()
            elif select == 5:
                tenCdUpdate = input("Nhập vào tên CD cần tìm: ")
                cd = CongDoan.find_cd(tenCdUpdate)
                if cd:
                    print(
                        f"Tên CD: {cd.tenCD} - Tên ca sĩ: {cd.tenCasi} - Tên bài hát: {cd.tenBaiHat} - Giá thành: {cd.GiaThanh}")
                else:
                    print("Tên CD không tồn tại !!!")
            elif select == 6:
                CongDoan.sum_price()
