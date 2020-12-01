# language: Python 3.8 or higher as the new Walrus operator (:=) has been used.

#  SOLUTION 1:
expense_report = # a list
target = 2020

for i,value1 in enumerate(expense_report[:-1]):
  if (value2 := target - value1) in expense_report[i+1:]:
    print(f'Numbers found are {value1} and {value2}')
    print('Therefore solution is: ', value1*value2)
    break
else:
   print('No solution')

#  SOLUTION 2:
expense_report = # a list
target = 2020
exit_now = False

for i,value1 in enumerate(expense_report[:-1]):
    for j,value2 in enumerate(expense_report[i+1:]):
        value_sum = value1 + value2
        if (value3 := target - value_sum) in expense_report:
            print(f'Numbers found are {value1}, {value2} and {value3}')
            print('Therefore solution is: ', value1*value2*value3)
            exit_now = True 
            break
        if exit_now:
            break
    if exit_now:
        break    
else:
    print('No solution')

