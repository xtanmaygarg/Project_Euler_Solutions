num_str = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

# Takes a list of numbers and the length of the window.
# Finds the product of the numbers within the window, adds it to a new list.
# Slides the window and repeats. Returns the max product. 
def max_prod(num_list, length):
    start = 0
    prod_list = []
    while start + length <= len(num_list):
        prod = 1
        for i in num_list[start: start+length]:
            prod = prod * i
        prod_list.append(prod)
        start += 1
    return max(prod_list)

# Main
if __name__ == "__main__":
    
    # Splits the large number into smaller numbers using 0 as the delimiter.
    num_str_list = num_str.split('0')

    # Casts digits as ints, creates 2d list of numbers of 13 digits or more.
    num_list = [[int(i) for i in num] for num in num_str_list if len(num) >= 13]
    
    prods = [max_prod(num, 13) for num in num_list]
    print(max(prods))
