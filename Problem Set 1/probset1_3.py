s = 'azcbobobegghakl'

start = 0
end = 0
length = 1

max_start = 0
max_end = 0
max_length = 1

for index in range(1,len(s)):
    if s[index] >= s[index-1]:
        end = index
        length += 1
    else:
        if length > max_length:
            max_length = length
            max_start = start
            max_end = end
        start = index
        end = index
        length = 1

if length > max_length:
    max_length = length
    max_start = start
    max_end = end

print 'Longest substring in alphabetical order is:',
print s[max_start: max_end + 1]
