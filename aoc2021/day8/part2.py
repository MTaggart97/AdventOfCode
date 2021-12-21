#  aaaa   
# b    c  
# b    c  
#  dddd   
# e    f  
# e    f  
#  gggg  

numbers = {
    'abcefg' : 0,
    'cf'     : 1,
    'acdeg'  : 2,
    'acdfg'  : 3,
    'bcdf'   : 4,
    'abdfg'  : 5,
    'abdefg' : 6,
    'acf'    : 7,
    'abcdefg': 8,
    'abcdfg' : 9
    }

def remove_all(st: str, ch: str) -> str:
    modified_string = st
    for c in ch:
        modified_string = modified_string.replace(c, '')
    return modified_string

def inter(st1: str, st2: str) -> int:
    set1 = set(st1)
    set2 = set(st2)
    return len(set1.intersection(set2))

def decode_line(line: str) -> dict:
    segments = [''.join(sorted(seg)) for seg in remove_all(line,'|\n').split(' ')]
    segments = [seg for seg in segments if len(seg) > 0]
    key = {}
    known_numbers = {}
    for seg in segments:
        if (len(seg) == 2):
            known_numbers[1] = seg
        elif (len(seg) == 4):
            known_numbers[4] = seg
        elif (len(seg) == 3):
            known_numbers[7] = seg
        elif (len(seg) == 7):
            known_numbers[8] = seg
    # Find segment 'a' by looking for segment that's not in 1 but is in 7  
    a = remove_all(known_numbers[7], known_numbers[1])
    key[a] = 'a'    # Found 'a'!
    # Find 9 by adding the 'a' segment to 4 and searching for element that is one away from it
    four = ''.join(sorted(known_numbers[4] + a))
    for seg in segments:
        if (inter(seg, four) == 5 and seg not in known_numbers.values()):
            known_numbers[9] = seg
            break
    # Find 'e' by subtracting 9 from 8
    e = remove_all(known_numbers[8], known_numbers[9])
    key[e] = 'e'    # Found 'e'!
    # Can find 5 by adding 1 to each element and checking if it is 9
    one = known_numbers[1]
    for seg in segments:
        if (seg == known_numbers[9]):
            continue
        five_canidate = ''.join(sorted(list(set(seg + one))))
        if (five_canidate == known_numbers[9]):
            known_numbers[5] = seg
            c = remove_all(one, seg)
            key[c] = 'c'    # Also found 'c'!
    # Can find 6 by looking for element with no 'c'
    for seg in segments:
        if (c not in seg and seg not in known_numbers.values()):
            known_numbers[6] = seg
            break
    # 0 is only number left with length 6
    for seg in segments:
        if (len(seg) == 6):
            if (seg not in known_numbers.values()):
                known_numbers[0] = seg
                break
    # 2 is the only number of lenth 5 left that doesn't overlap fully with 1
    for seg in segments:
        if (len(seg) == 5 and seg not in known_numbers.values()):
            removed_length = len(remove_all(seg, one))
            if (removed_length == len(seg) - 1):
                known_numbers[2] = seg
            else:
                known_numbers[3] = seg

    return {v: k for k, v in known_numbers.items()}

def decode_segement(segment: str, key: dict) -> int:
    decoded = ''.join(key[i] for i in segment)
    return numbers[decoded]

output_summed = 0
with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        decoded_key = decode_line(line)
        output = line.strip('\n').split('|')[1]
        output_segments =[seg for seg in output.split(' ') if len(seg) > 0]
        # Sort elements to make look ups in the `numbers` dictionary eaiser
        output_segments = [''.join(sorted(seg)) for seg in output_segments]
        output_summed += sum(decoded_key[seg]*(10**(3-i)) for i, seg in enumerate(output_segments))

print(output_summed)
