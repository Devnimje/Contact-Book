import re
import sys
import csv

#sys module is used to interact with the operating system and the csv module is used to read and write csv files
#The csv module is used to read and write csv files. It provides classes for reading and writing

def add(i):
    with open('data.csv', 'a+' , newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)

def view():
    data = []
    with open ('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data


#view()

def remove(i):
    def save(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)
            
    new_list = []
    telephone = i
    
    with open('data.csv', 'r') as file:
        reader =  csv.reader(file)
        for row in reader:
            new_list.append(row)
                
            for element in row:
                if element == telephone:
                    new_list.remove(row)
    save(new_list)
    
#remove('999999999')
#view()

def update(i):
    
    def update_newlist(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)
            
            
    new_list = []
    telephone = i[0]



    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == telephone:
                    name = i[1]
                    gender = i[2]
                    telephone = i[3]
                    
                    data = [name,gender,telephone]
                    index = new_list.index(row)
                    new_list[index] = data 
                
    update_newlist(new_list)
    
#sample = ['123','Girl','Female']
#update(sample)

def search(i):
    data = []
    telephone = i
    
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == telephone:
                    data.append(row)
                    
    print(data)
    return data
search('123')