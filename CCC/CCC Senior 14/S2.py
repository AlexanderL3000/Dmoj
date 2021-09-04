count = int(input())
first = list(input().split(" "))
second = list(input().split(" "))
partners = []

def solve(first,second):
    zipped_lists = zip(first, second)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    first, second = [ list(tuple) for tuple in  tuples]

    partners= second[:]

    zipped_lists = zip(second, first)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    list2, list1 = [ list(tuple) for tuple in  tuples]
    if partners == list1:
        for count, item in enumerate(list1):
                if item == list2[count]:
                    return "bad"
        if len(list1) != len(set(list1)) :
            return("bad")
        if len(list2) != len(set(list2)):
            return "bad"
        return "good" 
    return("bad")

print(solve(first,second))


