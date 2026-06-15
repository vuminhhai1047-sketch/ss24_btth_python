class Drink:

    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def price(self):
        return self.__price

    def toggle_available(self):
        self.is_available = not self.is_available


# Danh sách đồ uống ban đầu
menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]


# Tìm mã món
def find_drink(menu, code):

    for index, drink in enumerate(menu):

        if drink.code == code:
            return index

    return -1


# Hiển thị danh sách
def display_menu(menu):

    print("\n--- DANH SÁCH ĐỒ UỐNG ---\n")

    print(
        f"{'Mã món':<10}"
        f"{'Tên món':<20}"
        f"{'Giá bán':<10}"
        f"{'Trạng thái'}"
    )

    print("-" * 55)

    for drink in menu:

        status = (
            "Đang bán"
            if drink.is_available
            else "Ngừng bán"
        )

        print(
            f"{drink.code:<10}"
            f"{drink.name:<20}"
            f"{drink.price:<10}"
            f"{status}"
        )


# Thêm đồ uống
def add_drink(menu):

    code = input("Nhập mã món: ").strip().upper()

    if find_drink(menu, code) != -1:

        print("Mã món đã tồn tại trong hệ thống!")

        return

    name = input("Nhập tên món: ").strip()

    try:

        price = int(input("Nhập giá bán: "))

        if price <= 0:

            print("Giá bán không hợp lệ!")

            return

    except ValueError:

        print("Giá bán không hợp lệ!")

        return

    new_drink = Drink(
        code,
        name,
        price
    )

    menu.append(new_drink)

    print(
        f"Thành công: Đã thêm món {name} vào thực đơn!"
    )


# Cập nhật trạng thái
def update_status(menu):

    code = input(
        "Nhập mã món cần cập nhật: "
    ).strip().upper()

    index = find_drink(menu, code)

    if index == -1:

        print(
            "Không tìm thấy món có mã này!"
        )

        return

    menu[index].toggle_available()

    status = (
        "Đang bán"
        if menu[index].is_available
        else "Ngừng bán"
    )

    print(
        f"Đã cập nhật trạng thái món {code}."
    )

    print(
        f"Trạng thái hiện tại: {status}"
    )


# Chương trình chính
while True:

    print("""
=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===

1. Xem danh sách đồ uống
2. Thêm đồ uống mới
3. Cập nhật trạng thái kinh doanh
4. Thoát chương trình

==============================================
""")

    try:

        choice = int(
            input("Chọn chức năng (1-4): ")
        )
        match choice:
            case 1:
                display_menu(menu)
            case 2:
                add_drink(menu)
            case 3:
                update_status(menu)
            case 4:
                print(
                    "Cảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!"
                )
                break
            case _:
                print(
                    "Lựa chọn không hợp lệ!"
                )
    except ValueError:
        print(
            "Bạn phải nhập số!"
        )