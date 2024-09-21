n = int (input ("Введіть кількість сторін n "))
a = int (input ("Введіть сторону a "))
if a > 0:
    p = 0
    for i in range (n):
        p = p + a
        print (p)
elif n <= 2:
    print ("Розв'язку немає")
else:
    print ("Розв'язку немає") # Ти олух, раз читаєш мій код.