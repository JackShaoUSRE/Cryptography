import CryptLib
import gmpy2

# test script of gcd.py and gcd_ext.py

test_a_1 = 7
test_b_1 = 5
test_a_2 = 31
test_b_2 = -13
test_a_3 = 24
test_b_3 = 36
test_a_4 = 2461502723515673086658704256944912426065172925575
test_b_4 = 1720876577542770214811199308823476528929542231719
test_a_5 = 13709616469144948883512229123502305176385931810284088906755090238431898972708904439178898468021710798401875986657125211084472621499595371254346390738382042
test_b_5 = 19235039994987625167590963480899777255933775238312044097122773255647530276806317636026727679800825370459321617724871515442147432420951257037823141069640181
test_a_6 = 96557807278640299121519463045206377934978887298086994211590515571717325955785923783159432436307870512742354877476790046891802153053719263845602618422474671707896136814707875793300040916757228826108499490311295942553478010913043680523612655400526255290702983490382191419067057726624348815391509161304477322782
test_b_6 = 146116799305702219220540123503890666704710410600856387071776221592477256752759997798169931809156426471243799795374072510423645363680537337813774268658907130969994146783451692837222772144941434909050652825715582967684984814095461041109999161468223272534833391335036612863782740784573110824091866969655931097032

result_1 = gmpy2.gcd(test_a_1, test_b_1)
result_2 = gmpy2.gcd(test_a_2, test_b_2)
result_3 = gmpy2.gcd(test_a_3, test_b_3)
result_4 = gmpy2.gcd(test_a_4, test_b_4)
result_5 = gmpy2.gcd(test_a_5, test_b_5)
result_6 = gmpy2.gcd(test_a_6, test_b_6)
result_1_t = CryptLib.gcd.gcd(test_a_1, test_b_1)
result_2_t = CryptLib.gcd.gcd(test_a_2, test_b_2)
result_3_t = CryptLib.gcd.gcd(test_a_3, test_b_3)
result_4_t = CryptLib.gcd.gcd(test_a_4, test_b_4)
result_5_t = CryptLib.gcd.gcd(test_a_5, test_b_5)
result_6_t = CryptLib.gcd.gcd(test_a_6, test_b_6)

print("T1 >> Max Common Divisor of")
print("     ", test_a_1)
print("     and")
print("     ", test_b_1)
print("     is :")
print("     ", result_1)
if result_1 == result_1_t:
    print("     Passed.  <<")
else:
    print("     Failed. The result your program got is:")
    print("     ", result_1_t)

print("T2 >> Max Common Divisor of")
print("     ", test_a_2)
print("     and")
print("     ", test_b_2)
print("     is :")
print("     ", result_2)
if result_2 == result_2_t:
    print("     Passed.  <<")
else:
    print("     Failed. The result your program got is:")
    print("     ", result_2_t)

print("T3 >> Max Common Divisor of")
print("     ", test_a_3)
print("     and")
print("     ", test_b_3)
print("     is :")
print("     ", result_3)
if result_3 == result_3_t:
    print("     Passed.  <<")
else:
    print("     Failed. The result your program got is:")
    print("     ", result_3_t)

print("T4 >> Max Common Divisor of")
print("     ", test_a_4)
print("     and")
print("     ", test_b_4)
print("     is :")
print("     ", result_4)
if result_4 == result_4_t:
    print("     Passed.  <<")
else:
    print("     Failed. The result your program got is:")
    print("     ", result_4_t)

print("T5 >> Max Common Divisor of")
print("     ", test_a_5)
print("     and")
print("     ", test_b_5)
print("     is :")
print("     ", result_5)
if result_5 == result_5_t:
    print("     Passed.  <<")
else:
    print("     Failed. The result your program got is:")
    print("     ", result_5_t)

print("T6 >> Max Common Divisor of")
print("     ", test_a_6)
print("     and")
print("     ", test_b_6)
print("     is :")
print("     ", result_6)
if result_6 == result_6_t:
    print("     Passed.  <<")
else:
    print("     Failed. The result your program got is:")
    print("     ", result_6_t)
