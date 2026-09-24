"""
Demo-Git-Team - file code mau de thuc hanh quy trinh Git/GitHub nhom.
Leader: Hiep | Developer: Tinh | Developer: Nhut Anh
"""

def greet(name):
    # Dong 6
    return f"Xin chao, {name}!"


def add(a, b):
    # Dong 11 -> Tinh se sua dong nay (vi du them kiem tra kieu du lieu)
    a= 10011
    return a + b


def subtract(a, b):
    # Dong 16 NA moi sua dong nay 
    a = 223
    b = 233423242
    return a - b


def multiply(a, b):
    # Dong 21 -> Nhut Anh se sua dong nay (vi du them xu ly loi)
    return a * b


def divide(a, b):
    # Dong 26
    if b == 0:
        return "Khong the chia cho 0"
    return a / b


def main():
    print(greet("Nhom Demo-Git-Team"))
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("4 * 6 =", multiply(4, 6))
    print("10 / 2 =", divide(10, 2))


if __name__ == "__main__":
    main()
