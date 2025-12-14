# create some tables we can pull from
ones = ["",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"]

teens = ["ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen"
]

tens = ["",
        "ten",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
]

ans = 0
for x in range(1,1001):
    s = ""
    # special case
    if x == 1000:
        s = "onethousand"
    else:
        
        # teens are special case
        if (x%100) >= 10 and (x%100) < 20:
            s += teens[x % 10]
        else:
            # easy to do the tens and ones
            if x >= 20:
                s += tens[(x%100) // 10]
            s += ones[x % 10]
        if x >= 100:
            # need to add "and" if there is already something
            if len(s) > 0:
                s = "and" + s
            s = ones[x//100] + "hundred" + s
        x = x % 100
    print(s)
    ans += len(s)
print(ans)