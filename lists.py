


sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
profit = 1.50

sales = sales_w1 + sales_w2
new_day = int(input("what is the latest sales?: "))
sales_w2.append(new_day)
worst_day = min(sales) * profit
best_day = max(sales) * profit

print(worst_day, best_day)

print(f'My total units sold for the two weeks are {sum(sales)} my lowest profit being {worst_day} and my highest profit being {best_day} and my overall profit was {sum(sales)*profit}')