
#Categories
categories = { 
    "1": "score", 
    "2": "rating", 
    "3": "popularity"
}


def prompt_category(choice):
    while True: 
        if choice in categories:  
            print(f"you chose filter by {categories[choice]}")
            return categories[choice]
        else:
            break
    print("Invalid choice, please enter valid number")
        
  
print(" what list you want to see from category? ")
for key, value in categories.items():
    print(f" {key}.{value}")

choice = input("choose a category:")
chose = prompt_category(choice)
#print(f'you chose category: {chose}')
               