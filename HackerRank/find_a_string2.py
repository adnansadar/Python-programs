string, substring = (input().strip(), input().strip())
print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)