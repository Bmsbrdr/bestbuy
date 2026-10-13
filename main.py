from products import Product
from store import Store

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

try:
    print(bose.buy(50))
    print(mac.buy(100))
except ValueError as e:
    print(e)
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()

product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]
inactive_product = Product("MeekBook Earth Co2", price=2050, quantity=50)
inactive_product.deactivate()

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(f"Total Quantity: {best_buy.get_total_quantity()}")
print(best_buy.order([(products[0], 1), (products[1], 2)]))
print(f"Total Quantity: {best_buy.get_total_quantity()}")
# additional tests
print(len(best_buy.get_all_products()))
best_buy.remove_product(product_list[0])
print(len(best_buy.get_all_products()))
best_buy.add_product(product_list[0])
print(len(best_buy.get_all_products()))

best_buy.add_product(inactive_product)
print(len(best_buy.get_all_products()))
best_buy.remove_product(inactive_product)
print(len(best_buy.get_all_products()))
inactive_product.activate()
best_buy.add_product(inactive_product)
print(len(best_buy.get_all_products()))
