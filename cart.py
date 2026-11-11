from product import Product

class Cart:
    def __init__(self):
        # 빈 장바구니 생성
        self.items = {} # {상품: 수량}

    def add(self, product, qty):
        self.items[product] = self.items.get(product, 0) + qty
        print(f"{product.name} {qty}개를 담았습니다.")

# -------------------------------------------
# 테스트 코드
# -------------------------------------------
# 제품 인스턴스 생성
tumbler = Product("텀블러", 15_000, 10)
# 카트 인스턴스 생성
cart = Cart()
cart.add(tumbler, 9)
cart.add(tumbler, 2)