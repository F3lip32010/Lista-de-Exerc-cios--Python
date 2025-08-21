date_str = input("Digite uma data no formato dd/mm/aaaa: ")

if len(date_str) != 10 or date_str[2] != '/' or date_str[5] != '/':
    print("Formato de data inválido. Use dd/mm/aaaa.")
else:
    day, month, year = map(int, date_str.split('/'))

    if year < 1 or month < 1 or month > 12 or day < 1:
        print("Data inválida.")
    else:
        if month in [4, 6, 9, 11]:
            max_days = 30
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                max_days = 29
            else:
                max_days = 28
        else:
            max_days = 31
            
        if day > max_days:
            print("Data inválida.")
        else:
            print("Data válida.")