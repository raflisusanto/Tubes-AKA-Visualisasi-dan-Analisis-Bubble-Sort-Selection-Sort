from tkinter import *
from tkinter import ttk
from threading import Thread
import time
import random

root = Tk()
root.title("Visualisasi Algoritma Bubble Sort dan Selection Sort")
root.maxsize(1400, 900)
root.config(bg = "white")

speed_name = StringVar()
speed_list = ['Cepat', 'Sedang', 'Lambat']

arr = []
arr2 = []

#Create Vertical Bars berdasarkan Value dari Array
def displayArr(arr, colorArray):
    canvas.delete("all")
    canvas_width = 600
    canvas_height = 400
    width_x = canvas_width / (len(arr) + 1)
    ini = 4
    space = 2
    tempArr = [i / max(arr) for i in arr]

    for i in range(len(tempArr)):
        x1 = i * width_x + ini + space
        y1 = canvas_height - tempArr[i] * 390
        x2 = (i + 1) * width_x + ini
        y2 = canvas_height
        canvas.create_rectangle(x1, y1, x2, y2, fill=colorArray[i])

    root.update_idletasks()

def displayArr2(arr2, colorArray):
    canvas2.delete("all")
    canvas_width = 600
    canvas_height = 400
    width_x = canvas_width / (len(arr2) + 1)
    ini = 4
    space = 2
    tempArr = []
    tempArr = [i / max(arr2) for i in arr2]

    for i in range(len(tempArr)):
        x1 = i * width_x + ini + space
        y1 = canvas_height - tempArr[i] * 390
        x2 = (i + 1) * width_x + ini
        y2 = canvas_height
        canvas2.create_rectangle(x1, y1, x2, y2, fill=colorArray[i])

    root.update_idletasks()
    

#GENERATING ARRAY
def createArr():
    global arr
    global arr2

    array_size = 30

    range_begin = 1

    range_end = 200

    arr = list()
    arr2 = list()
    for i in range(0, array_size):  
        random_integer = random.randint(range_begin, range_end) #starting from a higher value and not 0 because the vertical bars wont be visible
        arr.append(random_integer)
        arr2.append(random_integer)

    displayArr(arr, ["#0052a3" for x in range(len(arr))])
    displayArr2(arr2, ["#0052a3" for y in range(len(arr2))])

# SORTING SPEED
def set_speed():
    lambat = 0.5
    sedang = 0.05
    cepat = 0.001

    if speed_comboBox.get() == 'Lambat':
        return lambat
    elif speed_comboBox.get() == 'Sedang':
        return sedang
    elif speed_comboBox.get() =="Cepat":
        return cepat

# SORTING ALGORIHMS
def sort1():
    #Bubble Sort
    tym = set_speed()
    for step in range(0, len(arr)):
        for i in range(0, len(arr)-step-1):
            displayArr(arr, ["yellow" if x == i or x == i+1 else "#0052a3" for x in range(len(arr))])
            time.sleep(tym)
            if(arr[i] > arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                        
    displayArr(arr, ["#99FF99" for x in range(len(arr))])

def sort2():
    tym = set_speed()
    # Selection Sort
    for Pass in range(1, len(arr2)):
        idx = Pass - 1
        for i in range(Pass, len(arr2)):
            if arr2[idx] > arr2[i]:
                idx = i
            
        displayArr2(arr2, ["yellow" if y == Pass-1 or y == idx else "#0052a3" for y in range(len(arr2))])
        time.sleep(tym)

        temp = arr2[Pass-1]
        arr2[Pass-1] = arr2[idx]
        arr2[idx] = temp

    displayArr2(arr2, ["#99FF99" for y in range(Pass)])

display_window = Frame(root, width= 1400, height=900, bg="white")
display_window.grid(row=8, column=0, padx=10, pady=5)

lbl2 = Label(display_window, text="Kecepatan Sorting: ", bg="white")
lbl2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_comboBox = ttk.Combobox(display_window, textvariable=speed_name, values=speed_list)
speed_comboBox.grid(row=1, column=1, padx=5, pady=5)
speed_comboBox.current(0)

lbl3 = Label(root, text="Bubble Sort ", bg="white")
lbl3.grid(row=5, column=0, padx=10, pady=5, sticky=W)

lbl4 = Label(root, text="Selection Sort ", bg="white")
lbl4.grid(row=5, column=1, padx=10, pady=5, sticky=W)

btn1 = Button(display_window, text="Sort", command=lambda:[sort1(), sort2()], bg="#C4C5BF")
btn1.grid(row=4, column=1, padx=5, pady=5)

btn2 = Button(display_window, text="Generate", command=createArr, bg="#C4C5BF")
btn2.grid(row=4, column=0, padx=5, pady=5)

canvas = Canvas(root, width=600, height=400, bg="white")
canvas.grid(row=3, column=0, padx=10, pady=5)

canvas2 = Canvas(root, width=600, height=400, bg="white")
canvas2.grid(row=3, column=1, padx=10, pady=5)

root.mainloop()
