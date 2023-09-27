#!/usr/bin/env python
# coding: utf-8

# In[9]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in kilograms: "))

height = int(input("Enter your height in centimeters: "))

BMI = (weight) / (height * height * 0.0001)

print(BMI)

if BMI>0:
    if (BMI<18.5):
        print(name + ", You're underweight. Lazem tezwd el calories bta3tk.")
    elif (BMI<=24.9):
        print(name + ", You're normal. Allah yenwar ya dawly.")
    elif (BMI<29.9):
        print(name + ", You're overweight. El3ab reyada w kol 5as.")
    elif (BMI<34.9):
        print(name + ", You're obese. El3ab reyada awy w kol 5as awy")
    elif (BMI<39.9):
        print(name + ", You're severely obese. El3ab reyada awy awy w kol 5as awy awy")
    elif (BMI>39.9):
        print(name + ", You're morbidly obese. El3ab reyada awy awy awy w kol 5as awy awy awy")
    else:
        print("Enter valid input")



# In[8]:


if BMI>0:
    if (BMI<18.5):
        print(name + ", You're underweight. Lazem tezwd el calories bta3tk.")
    elif (BMI<=24.9):
        print(name + ", You're normal. Allah yenwar ya dawly.")
    elif (BMI<29.9):
        print(name + ", You're overweight. El3ab reyada w kol 5as.")
    elif (BMI<34.9):
        print(name + ", You're obese. El3ab reyada awy w kol 5as awy")
    elif (BMI<39.9):
        print(name + ", You're severely obese. El3ab reyada awy awy w kol 5as awy awy")
    elif (BMI>39.9):
        print(name + ", You're morbidly obese. El3ab reyada awy awy awy w kol 5as awy awy awy")
    else:
        print("Enter valid input")


# In[ ]:




