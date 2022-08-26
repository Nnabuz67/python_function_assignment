#python code to split even and odd numbers


def splitevenodd(A):
    evenlist = []
    oddlist = []
    for i in A:
        if (i % 2 == 0):
            evenlist.append(i)
        else:
            oddlist.append(i)

    print("Even lists:", evenlist)
    print("Odd list:", oddlist)

# Driver code

A = list()
n = int(input("Enter the size of the First list::"))
print("Enter the element of First list::")
for i in range (int(n)):
    k = int(input(""))
    A.append(k)

splitevenodd(A)