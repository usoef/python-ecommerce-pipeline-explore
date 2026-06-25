class Order:
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount
    
    def calculate_tax(self, tax_rate):
        return self.total_amount * tax_rate
    
    def display_order(self):
        print (f"""
                Order ID: {self.order_id}
                Nama: {self.customer_name}
                Tanggal: {self.order_date}
                Total: Rp. {self.total_amount}
            """)

class OrderProcessor:
    def __init__(self):
        self.orders = []
    
    def add_order(self, order):
        self.orders.append(order)

    def calculate_total_revenue(self):
        total = 0
        for order in self.orders:
            total += order.total_amount
        return total
    
    def calculate_total_tax(self, tax_rate):
        total_tax = 0
        for order in self.orders:
            total_tax += order.calculate_tax(tax_rate)
        return total_tax
    
    def display_orders(self):
        for order in self.orders:
            order.display_order()
            print("-" * 50)

order1 = Order("A11", "Yusuf", "2026-06-25", 30000)
order2 = Order("A12", "Abdulloh", "2026-06-25", 100000)
prosesor = OrderProcessor()
prosesor.add_order(order1)
prosesor.add_order(order2)

print("====== DAFTAR ORDER ======")
prosesor.display_orders()
print("Total Pendapatan: Rp.", prosesor.calculate_total_revenue())
print("Total Pajak: Rp.", prosesor.calculate_total_tax(0.1))