
def two_digit_canceling_frac():
    non_trivial_fractions = []
    num_dig=1
    denom_dig=1
    same_dig=1
    while num_dig<10:
        denom_dig = 1
        while denom_dig<10:
            same_dig =1
            while same_dig<10:
                fracs = [int(str(num_dig)+str(same_dig))/int(str(denom_dig)+str(same_dig))]
                fracs.append(int(str(same_dig)+str(num_dig))/int(str(denom_dig)+str(same_dig)))
                fracs.append(int(str(same_dig)+str(num_dig))/int(str(same_dig)+str(denom_dig)))
                fracs.append(int(str(num_dig)+str(same_dig))/int(str(same_dig)+str(denom_dig)))
                for i in range(len(fracs)):
                    if fracs[i]<1 and fracs[i]==(num_dig/denom_dig):
                        non_trivial_fractions.append(f"{str(num_dig)}/{str(denom_dig)} , {same_dig}")
                same_dig+=1
            denom_dig+=1
        num_dig+=1
    return(non_trivial_fractions)


            
print(two_digit_canceling_frac())



