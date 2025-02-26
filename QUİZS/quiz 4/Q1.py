N = int(input("please enter a number :"))
sum_of_evens = 0
sum_of_odds = 0
number_of_evens = 0
for i in range(1, N+1):
    if i % 2 == 0:
        sum_of_evens += i
        number_of_evens += 1
    else:
        sum_of_odds += i
av_evens = (sum_of_evens/number_of_evens)
print(av_evens)
print(sum_of_odds)
