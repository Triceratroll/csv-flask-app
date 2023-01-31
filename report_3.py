import csv
import os
from collections import defaultdict


def generate_customer_ranking(in_folder, out_folder):
    output_file = 'customer_ranking.csv'
    with open(os.path.join(in_folder, 'customers.csv'), 'r') as customers_file, open(os.path.join(in_folder, 'products.csv'), 'r') as products_file, open(os.path.join(in_folder, 'orders.csv'), 'r') as orders_file, open(output_file, 'w', newline='') as customer_ranking_file:
        customers_reader = csv.DictReader(customers_file)
        products_reader = csv.DictReader(products_file)
        orders_reader = csv.DictReader(orders_file)

        product_prices = {row['id']: float(row['cost']) for row in products_reader}
        customer_totals = defaultdict(float)
        for order in orders_reader:
            customer_id = order['customer']
            product_ids = order['products'].split(' ')
            total = sum([product_prices[product_id] for product_id in product_ids])
            customer_totals[customer_id] += total

        customer_ranking = []
        for customer in customers_reader:
            customer_id = customer['id']
            total = customer_totals[customer_id]
            customer_ranking.append((customer_id, customer['firstname'], customer['lastname'], total))

        customer_ranking.sort(key=lambda x: x[3], reverse=True)

        customer_ranking_writer = csv.writer(customer_ranking_file)
        customer_ranking_writer.writerow(['id', 'firstname', 'lastname', 'total'])

        for customer in customer_ranking:
            customer_ranking_writer.writerow(customer) 

    return output_file