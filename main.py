import random

# 1. Initialize Inventory
items = ["Sandwich", "Salad", "Cake"]
prices = [65, 45, 50]
inventories = [100, 50, 100]
co_inventories = [100, 50, 100]


# 2. Simulate Customer Arrivals
def simulate_customers(inventories):
    # Initial variables
    sales = [0, 0, 0]
    sales_list = []
    missed_sales = [0, 0, 0]
    not_buying = 0

    num_of_stud = random.randint(0, 500)                # Number of students (between 0-500)
    for student in range(num_of_stud):
        buying = random.randint(0, 1)                   # Simulate if the student wants to buy (1) or not (0)
        if buying == 1:
            what_to_buy = random.randint(0, 2)          # If the student is buying - here it finds what it is buying
            if inventories[what_to_buy] > 0:            
                inventories[what_to_buy] -= 1           # Controlling the inventory
                sales[what_to_buy] += 1                 # Keeps track of sales
                sales_list.append(what_to_buy)          # Storing all item IDs of all sales
            else:
                missed_sales[what_to_buy] += 1          # Keeps track of missed sales due to missing inventory
        else:
            not_buying += 1                             # Keeps track of students who don't want to buy anything
    return sales_list, sales, missed_sales, not_buying, num_of_stud, inventories

# 3. Process Sales
def process_sales (sales_list, sales, prices):
    # Method 1
    revenue = 0
    for sale in range(len(sales_list)):
        revenue += prices[sales_list[sale]]             # Looping through the sales_list to calculate revenue
    # Method 2
    revenue1 = sales[0] * prices[0] + sales[1] * prices[1] + sales[2] * prices[2] # Calculating revenue by multiplying thee sale of each item with its price
    return revenue, revenue1

# 4. Generate Sales Report
def sales_report (items, sales, missed_sales, not_buying, num_of_stud, inventories, revenue, disposal_cost, production_cost):
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
    
    The end inventory is leading to {disposal_cost} DKK in disposal cost

    The production cost is {production_cost} DKK

    The the total profit is {revenue - production_cost - disposal_cost} DKK

    There have been the following in missed sales due to missing inventory:
      {items[0]}: {missed_sales[0]}
      {items[1]}: {missed_sales[1]}
      {items[2]}: {missed_sales[2]}

    Students who did not want to buy: {not_buying}
    """)

# 5. Calculate costs
def costs (initial_inventory, inventories, prices):
    item_costs = []
    for price in prices:
        item_costs.append(price / 2)            # Calculating the item cost by dividing each of them in half
    disposal_costs = inventories[0] * item_costs[0] + inventories[1] * item_costs[1] + inventories[2] * item_costs[2] # Calculating the costs by multiplying the the end inventory with the item costs
    production_costs = initial_inventory[0] * item_costs[0] + initial_inventory[1] * item_costs[1] + initial_inventory[2] * item_costs[2] # Calculating the costs by multiplying the the end inventory with the item costs
    return disposal_costs, production_costs

customer_numbers = simulate_customers(inventories)
revenue = process_sales(customer_numbers[0], customer_numbers[1], prices)
costs = costs(co_inventories, customer_numbers[5], prices)
sales_report(items, customer_numbers[1], customer_numbers[2], customer_numbers[3], customer_numbers[4], customer_numbers[5], revenue[1], costs[0], costs[1])

# 6. Optimal inventory levels
# One can use the simulations above to test different levels of inventory through many simulation to find what inventory level is the best. 
# It can also be done more theoretical with a newsvendor problem approach