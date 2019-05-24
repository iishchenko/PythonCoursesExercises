def find_the_odds(a_list):
       list_of_odds = []
       for i in range(len(a_list)):
           if i % 2 == 1:
               list_of_odds.append(a_list[i])
       return list_of_odds
       
my_list = [1, 5, 4, 4, 2, 1, 5, 9]
my_list = find_the_odds(my_list)
print(my_list)
