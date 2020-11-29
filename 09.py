import re

garbage_with_cancel = re.compile(r'<.*!..*>')
cancel = re.compile(r'!.')
garbage = re.compile(r'<.*>')

def excl_in_garbage(input):
    return len(re.findall(garbage_with_cancel,input)) > 0

def get_rid_of_exclamations(input):
    test = input[input.find('<'):input.find('>')+1]
    input_1 = input[0:input.find('<')]
    input_2 = input[input.find('>')+1:]
    test1 = re.sub(cancel,"",test)
    return(input_1 + test1 + input_2)


def get_rid_of_garbage(input):
    test = input[input.find('<'):input.find('>')+1]
    input_1 = input[0:input.find('<')]
    input_2 = input[input.find('>')+1:]
    return(input_1 + input_2)



with open('./inputs/09') as f:
    input = f.readlines()[0]

print(len(input))

#giinput = "!234"

while "!" in input:
    input = input[:input.find('!')] + input[input.find('!')+2:]
#input = re.sub(cancel,"",input)

print(input)

while re.findall(garbage,input):
    input = get_rid_of_garbage(input)
    print(len(input))

print(input)


#while excl_in_garbage(input):
#        input = get_rid_of_exclamations(input)
        #print(input)

#while '<' in input:
 #   input = get_rid_of_garbage(input)
    #print(input)
#print(input)

#solution_1 = count_groups(input)
#   - keep cleaning it up until we don't have any