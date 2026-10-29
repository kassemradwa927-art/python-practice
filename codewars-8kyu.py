# 1- convert number to reversed array of digits (8kyu)
def main():
    n = int(input("Enter anumber: "))
    print(digitize(n))


def digitize(n):
    result = []
    for d in str(n)[::-1]:
       result.append(int(d))
    return result

main()   