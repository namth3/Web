from DB_connection import posts
from DB_connection import customers
from DB_connection import rivers
from pprint import pprint
import matplotlib.pyplot as plotter

# 1.  Add a post to collection
def add_post(title:str,author:str,content:str):
    new_post = {"title":title,"author": author, "content":content}
    posts.insert_one(new_post)  
# add_post("Ta Hai Nam","Favorite quotes", "Happiness is a journey, not a destionation")


# 2. Count number of customer group by refs
ref_count = 0
ref_list = {}
customers_list = customers.find()
for customer in customers_list:
    customer_ref = customer["ref"]
    if customer_ref not in ref_list:
        ref_list[customer_ref] = 1
        ref_count += 1
    else:
        ref_list[customer_ref] += 1
# print(ref_count)
# print(ref_list)

# 3. Use MatPlotLib to draw a pie chart showing how much percentage of each reference
pie_labels = []
pie_data = []
for key, value in ref_list.items():
    pie_labels.append(key)
    pie_data.append(value)

plotter.figure('Pie Chart Example', figsize=(4,4), facecolor='white')

plotter.title("Customer group by ref")

sliceColors = ['red', 'yellow', 'green']
plotter.pie(
    pie_data,
    labels=pie_labels,
    colors=sliceColors,
    startangle=90,
    autopct='%.2f'
    )

plotter.show()

# 4. List all rivers in Africa continent
if __name__ == "__main__":
    river_list = rivers.find(
        {
            "continent": "Africa"
        }
    )
    for river in river_list:
        print(river["name"])




#5. ‘S. America’ continent with length less than 1000 km

if __name__ == "__main__":
    river_list = rivers.find(
        {
            "continent": "S. America",
            "length": {"$lt": 1000}
        }
    )
    for river in river_list:
        print(river["name"])



