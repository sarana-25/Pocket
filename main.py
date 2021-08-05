def count_substring(string, sub_string):
    a=0
    for i in range(len(string)):
        a+=string[i:i+len(sub_string)].count(sub_string)
    return(a)
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)