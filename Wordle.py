# cook your dish here
for _ in range(int(input())):
    s = input()
    t = input()
    string = ''
    for i in range(len(s)):
        if s[i] == t[i]:
            string+='G'
        else:
            string+='B'
    print(string)
