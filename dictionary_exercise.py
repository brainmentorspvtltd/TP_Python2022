products = [
    {"p_name":"Apple Iphone 11","brand":"Apple","Category":"Mobile","price":98000},
    {"p_name":"Redmi Note 6","brand":"Xiaomi","Category":"Mobile","price":15000},
    {"p_name":"Sports Shoes","brand":"Puma","Category":"Shoes","price":3400},
    {"p_name":"JBL Headphones bluetooth","brand":"JBL","Category":"Headphones","price":1200},
    {"p_name":"Leather Jacket","brand":"Zara","Category":"Clothes","price":4500},
    {"p_name":"Puma Shoes","brand":"Puma","Category":"Shoes","price":2070},
    {"p_name":"Adidas Sports Shoes","brand":"Adidas","Category":"Shoes","price":1900},
    {"p_name":"Macbook Pro","brand":"Apple","Category":"Laptop","price":128000},
    {"p_name":"Lenovo thinkpad","brand":"Lenovo","Category":"Laptop","price":78000},
    {"p_name":"Asus Zenbook","brand":"Asus","Category":"Laptop","price":88000},
    ]

def sortData(x):
    return x["price"]

while True:
    searchResults = []
    toSearch = input("Enter product : ")
    toSearch = toSearch.lower()

    '''
    - user can enter product name, product brand or category
    - now store the data in a different list (searchResults = [])
    - ask user if he wants to sort data based on price
    - ask the order of sorting
    '''

    for i in range(len(products)):
        '''
        condition_1 = products[i]['p_name'].lower() == toSearch
        condition_2 = products[i]['brand'].lower() == toSearch
        condition_3 = products[i]['Category'].lower() == toSearch
        '''
        condition_1 = toSearch in products[i]['p_name'].lower()
        condition_2 = toSearch in products[i]['brand'].lower()
        condition_3 = toSearch in products[i]['Category'].lower()
        if condition_1 or condition_2 or condition_3:
            print(products[i])
            searchResults.append(products[i])

    choice = input("You want to sort data based on price : [Y/N] ")
    choice = choice.lower()
    if choice == "y":
        print("1. Low to High")
        print("2. High to Low")
        sortChoice = input(": ")
        if sortChoice == "1":
            sortedOutput = sorted(searchResults, key=sortData)
            print(sortedOutput)
        else:
            sortedOutput = sorted(searchResults, key=sortData, reverse=True)
            print(sortedOutput)









