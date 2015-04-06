s = 'azcbobobegghakl'

count = 0
num = 0
while num <= (len(s)-3):
    if (s[num] == 'b' and s[num+1] == 'o' and s[num+2] == 'b'):
        count += 1
    num += 1
print 'Number of times bob occurs is:',
print count
