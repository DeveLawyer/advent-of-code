import os

def sum_calibration_values(input):
    values = get_calibration_values(input)
    return sum(values)

def get_calibration_values(input):
    '''Retorna el listado numérico'''
    lines = input.split('\n')
    cleaned_lines = map(clean_line, lines)
    return list(cleaned_lines)

def clean_line(line):
    '''Limpia las líneas para dejar solo los dígitos inicial y final'''
    cleaned_line = ''
    for char in line:
        if char.isdigit():
            cleaned_line += char
    return int(cleaned_line[0] + cleaned_line[-1])

def main():
    __location__ = os.path.dirname(__file__)
    f = open(os.path.join(__location__, '01-trebuchet.txt'), 'r')
    input = f.read()
    sum = sum_calibration_values(input)
    print(sum)
    return sum

if __name__ == "__main__":
    main()