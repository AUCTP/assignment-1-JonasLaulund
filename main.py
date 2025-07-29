import random

# 1. Initialize Inventory
items = ["Sandwich", "Salad", "Cake"]
prices = [65, 45, 50]
inventories = [100, 50, 100]


# 2. Simulate Customer Arrivals
def simulate_customers(items, inventories):
    sales = [0, 0, 0]
    sales_list = []
    missed_sales = [0, 0, 0]
    not_buying = 0

    num_of_stud = random.randint(0, 500)
    for student in range(num_of_stud):
        buying = random.randint(0, 1)
        if buying == 1:
            what_to_buy = random.randint(0, 2)
            if inventories[what_to_buy] > 0:
                inventories[what_to_buy] -= 1
                sales[what_to_buy] += 1
                sales_list.append(what_to_buy)
            else:
                missed_sales[what_to_buy] += 1
        else:
            not_buying += 1
    return sales_list, sales, missed_sales, not_buying, num_of_stud, inventories

# 3. Process Sales
def process_sales (sales_list, sales, prices):
    # Method 1
    revenue = 0
    for sale in range(len(sales_list)):
        revenue += prices[sales_list[sale]]
    # Method 2
    revenue1 = sales[0] * prices[0] + sales[1] * prices[1] + sales[2] * prices[2]
    return revenue, revenue1

# 4. Generate Sales Report
def sales_report (items, sales, missed_sales, not_buying, num_of_stud, inventories, revenue, costs):
    print(f"""
    Out of {num_of_stud} student arriving today the following happened:      

    There have been sold the following:
      {items[0]}: {sales[0]}
      {items[1]}: {sales[1]}
      {items[2]}: {sales[2]}

    Leading to a revenue of {revenue} DKK
    
    The remaining inventory is:
      {items[0]}: {inventories[0]}
      {items[1]}: {inventories[1]}
      {items[2]}: {inventories[2]}
    
    The end inventory is leading to {costs} DKK in costs

    The the total profit is {revenue - costs} DKK

    There have been the following in missed sales due to missing inventory:
      {items[0]}: {missed_sales[0]}
      {items[1]}: {missed_sales[1]}
      {items[2]}: {missed_sales[2]}

    Students who did not want to buy: {not_buying}
    """)

# 5. Calculate costs
def costs (inventories, prices):
    item_costs = []
    for price in prices:
        item_costs.append(price / 2)
    costs = inventories[0] * item_costs[0] + inventories[1] * item_costs[1] + inventories[2] * item_costs[2]
    return costs

customer_numbers = simulate_customers(items, inventories)
revenue = process_sales(customer_numbers[0], customer_numbers[1], prices)
costs = costs(customer_numbers[5], prices)
sales_report(items, customer_numbers[1], customer_numbers[2], customer_numbers[3], customer_numbers[4], customer_numbers[5], revenue[1], costs)

# 6. Optimal inventory levels
# One can use the simulations above to test different levels of inventory through many simulation to find what inventory level is the best. 