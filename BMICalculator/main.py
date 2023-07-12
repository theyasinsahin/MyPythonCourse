from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=400,height=400)
window.config(pady=40)

#weight label
weight_label = Label()
weight_label.config(text="Enter Your Weight(kg)",pady=10)
weight_label.pack()

#enter weight
weight_enter = Entry(width=10)
weight_enter.pack()


#height label
height_label = Label()
height_label.config(text="Enter Your Height(cm)",pady=10)
height_label.pack()

#enter height
height_enter = Entry(width=10)
height_enter.config()
height_enter.pack()


#result label
result_label_text = StringVar()
result_label = Label(pady=30)

#button
def calculate_func():
    try:
        height = float(height_enter.get())
        weight = float(weight_enter.get())
        BMI = weight / (height / 100) ** 2
        if BMI < 18.5:
            result_label.config(text=f"Your BMI: {BMI} - Under Weight")
        elif BMI <= 24.9:
            result_label.config(text=f"Your BMI: {BMI} - Normal")
        elif BMI <= 29.9:
            result_label.config(text=f"Your BMI: {BMI} - Over Weight")
        elif BMI <= 34.9:
            result_label.config(text=f"Your BMI: {BMI} - Obesity (Class I)")
        elif BMI <= 39.9:
            result_label.config(text=f"Your BMI: {BMI} - Obesity (Class II)")
        else:
            result_label.config(text=f"Your BMI: {BMI} - Extreme Obesity")

    except:
        if weight_enter.get() == "":
            result_label.config(text="Enter both weight and height!")
        elif height_enter.get() == "":
            result_label.config(text="Enter both weight and height!")
        else:
            result_label.config(text="Enter a valid number!")


calculater_button = Button()
calculater_button.config(text="Calculate", width=10,command=calculate_func)
calculater_button.pack()
result_label.pack()



window.mainloop()