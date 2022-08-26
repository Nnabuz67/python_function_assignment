def my_function(num):
    for n in range(2, int(num**0.5)+1):
        if num%n==0:
            return False

        return True 

print(my_function(7))
print(my_function(8))