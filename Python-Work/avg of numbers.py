def avg(list):
  
        list = []

        nums = int(input("Hány számot akarsz átlagolni? "))

        for i in range(0, nums):
            ele = int(input(""))

        list.append(ele)

        return sum(list) / len(list)

print(avg(list))