import csv
import os

def generate_order_prices(in_folder, out_folder):
    output_file = 'order_prices.csv'
    with open(os.path.join(in_folder, 'orders.csv'), 'r') as orders_file, open(os.path.join(out_folder, output_file), 'w', newline='') as order_prices_file:
        orders_reader = csv.DictReader(orders_file)
        order_prices_writer = csv.writer(order_prices_file)
        order_prices_writer.writerow(['id', 'total'])

        for order in orders_reader:
            order_id = order['id']
            product_ids = order['products'].split()

            total = 0
            with open(os.path.join(in_folder, 'products.csv'), 'r') as products_file:
                products_reader = csv.DictReader(products_file)
                for product in products_reader:
                    if product['id'] in product_ids:
                        total += float(product['cost'])

            order_prices_writer.writerow([order_id, total])

    return output_file
