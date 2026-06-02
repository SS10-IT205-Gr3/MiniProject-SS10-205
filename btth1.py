cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("\n" + "="*50)
    print("          SHOPEE CART MANAGEMENT SYSTEM          ")
    print("="*50)
    print("[1] Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("[2] Thêm sản phẩm mới / Cộng dồn số lượng")
    print("[3] Cập nhật số lượng của một sản phẩm")
    print("[4] Xóa sản phẩm khỏi giỏ hàng")
    print("[5] Thoát chương trình")
    print("="*50)
    choice = int(input("Mời bạn chọn chức năng (1-5): "))
        
    if choice == 1:
        print("\n" + "-"*30 + " CHI TIẾT GIỎ HÀNG " + "-"*30)
        print(f"{'STT':<5} | {'Mã SP':<7} | {'Tên Sản Phẩm':<25} | {'SL':<5} | {'Đơn Giá':<12} | {'Thành Tiền'}")
        print("-"*85)
        
        total_quantity = 0
        total_amount = 0
        
        for index, item in enumerate(cart_items, start=1):
            product_id = item[0]
            product_name = item[1]
            quantity = item[2]
            price = item[3]
            
            subtotal = quantity * price
            total_quantity += quantity
            total_amount += subtotal
            
            print(f"{index:<5} | {product_id:<7} | {product_name:<25} | {quantity:<5} | {price:,.0f}đ{'' :<4} | {subtotal:,.0f}đ")
            
        print("-"*85)
        print(f"⇒ Tổng số lượng sản phẩm trong giỏ: {total_quantity}")
        print(f"⇒ TỔNG TIỀN THANH TOÁN: {total_amount:,.0f}đ")
        print("-" * 85)
        
    elif choice == 5:
        print("\nThoát chương trình!")
        break
