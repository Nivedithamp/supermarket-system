#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 23:03:10 2022

@author: nivedithamp
"""

class View_Items():
    def __init__(self, items):
        self.items = items
        print("--------View Items--------\n")
        
    def show_item(self):
        print("The number of items in the inventory are: %d" %len(self.items))
        print()
        if len(self.items) != 0:
            print("Here are all the items available in the supermarket")
            for item in self.items:
                for key,val in item.items():
                    print(key,val)
                print()
class Add_Items():
    def __init__(self):
        print("------Add items-------\n")
        
    def add_item_form(self):
        print("To add an item fill in the form")
        item = {}
        item["Item name: "] = input("Item name: ")
        while True:
            try:
                item["Quantity: "] = int(input("Item quantity: "))
                break
            except ValueError:
                print("Quantity should only in digits")
        while True:
            try:
                item["Price: $"] = int(input("Price: $"))
                break
            except ValueError:
                print("Price should only in digits")
        print("\nItem has been successfully added")
        items.append(item)
        
class Purchase_Item():
    def __init__(self, items):
        print("\n----------Purchase Item-----------")
        self.items = items
        
    def user_purchase(self):
        purchase_item = input("Which item do you want to purchase? \nEnter name: ")
        purchase_quantity = int(input("Enter the quantity needed: "))
        for item in items:
            if purchase_item.lower() == item["Item name: "].lower():
                if item["Quantity: "] != 0:
                    if purchase_quantity <= item["Quantity: "]:
                        print("\nPay %d at checkout counter" %(item["Price: $"]*purchase_quantity))
                        item["Quantity: "] -= purchase_quantity
                    else:
                        print("Quantity required is not available")
                else:
                    print("Item out of stock")
                    
class Search_Item():
    def __init__(self, items):
        self.items = items
        print("\n-------------Search Item---------------")
        
    def user_search(self):
        find_item = input("Enter the item name in the inventory: ")
        for item in self.items:
            if item["Item name: "].lower() == find_item.lower():
                print("The item name " + find_item + " is displayed below with is details")
                print(item)
    
class Edit_Items():
    def __init__(self):
        print('\n-------Edit items---------\n')
        
    def user_edit(self):
        item_name = input("Enter the name of the item you want to edit: ")
        for item in items:
            if item_name.lower() == item["Item name: "].lower():
                print("Here are the current deatails of " + item_name)
                print(item)
                item["Item name: "] = input("Item name: ")
                while True:
                    try:
                        item["Quantity: "] = int(input("Item quantity: "))
                        break
                    except ValueError:
                        print("Quantity should only be in digits")
                while True:
                    try:
                        item["Price: $"] = int(input("Item Price: $"))
                        break
                    except ValueError:
                        print("Price should only be in digits")
                print(item)
                
if __name__ == "__main__":
    print("\n----------Welcome to the supermarket-----------\n")
    print("1.View Items \n2.Add Items \n3.Purchase Items \n4.Search Items \n5.Edit Item \n6.Exit")
    items = []
    while(True):
        try:
            user_response = int(input("Enter the number of your choice: "))
        
            if user_response == 1:  #View Items
                view = View_Items(items)
                view.show_item()
            
            elif user_response == 2:   #Add Items
                add = Add_Items()
                add.add_item_form()
            
            elif user_response == 3:
                purchase = Purchase_Item(items)
                purchase.user_purchase()
            
            elif user_response == 4:
                search = Search_Item(items)
                search.user_search()
        
            elif user_response == 5:
                edit = Edit_Items()
                edit.user_edit()
            
            elif user_response == 6:
                print("----------Exited----------")
                break
            
            else:
                print("Invalif Input!")
        
        except Exception as e:
            print(f"{e}---> INVALID INPUT! \n")
            
            
            