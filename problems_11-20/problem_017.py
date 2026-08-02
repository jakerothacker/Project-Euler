# nubmer of letters in numbers 1-1000

def letter_count_including(n):
    tot = 0
    for n in range(1,n+1):
        str = num_to_word(n)
        tot += len(str.replace(" ","").replace("-",""))
    return tot


def num_to_word(n):
    if len(str(n))>6:
        raise ValueError("7+ digits not impimented")
    elif len(str(n)) == 1:
        if n == 0:
           num_str = "zero"
        else:
            num_str = num_to_word_ones_place(n)
        return num_str
    elif len(str(n)) == 2:
        num_str = num_to_word_two_digits(n)
    elif len(str(n)) == 3:
        num_str = num_to_word_three_digits(n)
    elif len(str(n)) <=6:
        num_str = num_to_words_four_to_six_digits(n)
    return(num_str)


def num_to_words_four_to_six_digits(n):
    if n // 1000 == 0 and n // 10000 == 0 and n //100000 == 0:
        num_str = num_to_word_three_digits(n)
    elif n % 1000 == 0:
        thousands = n // 1000 % 1000
        num_str = num_to_word_ones_place(thousands) + " thousand"
    else:
        thousands = n // 1000 %1000
        num_str = num_to_word_three_digits(thousands) + " thousand " + num_to_word_three_digits(n % 1000)
    return(num_str)
    


def num_to_word_three_digits(n):
    if n // 100 == 0:
        num_str = num_to_word_two_digits(n)
    elif n % 100 == 0:
        hundreds_place = n // 100 % 10
        num_str = num_to_word_ones_place(hundreds_place) + " hundred"
    else:
        hundreds_place = n // 100 % 10
        num_str = num_to_word_ones_place(hundreds_place) + " hundred and " + num_to_word_two_digits(n % 100)
    return(num_str)

def num_to_word_two_digits(n):
    if n // 10 == 0:
        num_str = num_to_word_ones_place(n)
    elif n == 10:
        num_str = "ten"
    elif n == 11:
        num_str = "eleven"
    elif n == 12:
        num_str = "twelve"
    elif n == 13:
        num_str = "thirteen"
    elif n == 14:
        num_str = "fourteen"
    elif n == 15:
        num_str = "fifteen"
    elif n == 16:
        num_str = "sixteen"
    elif n == 17:
        num_str = "seventeen"
    elif n == 18:
        num_str = "eighteen"
    elif n == 19:
        num_str = "nineteen"
    elif n % 10 == 0:
        tens_place = n // 10 % 10
        num_str = num_to_word_tens_place(tens_place)
    else:
        tens_place = n // 10 % 10
        ones_place = n % 10
        num_str = num_to_word_tens_place(tens_place) + "-" + num_to_word_ones_place(ones_place)
    return(num_str)



def num_to_word_ones_place(n):
    if n == 1:
        return("one")
    elif n == 2:
        return("two")
    elif n == 3:
        return("three")
    elif n == 4:
        return("four")
    elif n == 5:
        return("five")
    elif n == 6:
        return("six")
    elif n == 7:
        return("seven")
    elif n == 8:
        return("eight")
    elif n == 9:
        return("nine")

def num_to_word_tens_place(n):
    if n == 2:
        return("twenty")
    elif n == 3:
        return("thirty")
    elif n == 4:
        return("forty")
    elif n == 5:
        return("fifty")
    elif n == 6:
        return("sixty")
    elif n == 7:
        return("seventy")
    elif n == 8:
        return("eighty")
    elif n == 9:
        return("ninety")


print(letter_count_including(1000))