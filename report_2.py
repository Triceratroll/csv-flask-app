import csv
import os


def generate_product_customers(in_folder, out_folder):
    output_file = 'product_customers.csv'
    with open(os.path.join(in_folder, 'orders.csv'), 'r') as orders_file, open(os.path.join(out_folder, 'product_customers.csv'), 'w', newline='') as product_customers_file:
        orders_reader = csv.DictReader(orders_file)
        product_customers = {}

        for order in orders_reader:
            customer_id = order['customer']
            product_ids = order['products'].split()

            for product_id in product_ids:
                if product_id in product_customers:
                    product_customers[product_id].add(customer_id)
                else:
                    product_customers[product_id] = {customer_id}

        product_customers_writer = csv.writer(product_customers_file)
        product_customers_writer.writerow(['id', 'customer_ids'])

        for product_id, customer_ids in product_customers.items():
            customer_ids_str = ' '.join(customer_ids)
            product_customers_writer.writerow([product_id, customer_ids_str])
    
    return output_file