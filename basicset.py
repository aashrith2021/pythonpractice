def average(array):
    # your code goes here
    f=array
    d=set(f)
    return sum(d)/len(d)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)