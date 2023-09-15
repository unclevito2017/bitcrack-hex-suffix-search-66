import subprocess
import random
import time

def generate_hex():
    # Generate a random 7-digit hex string with no more than 2 consecutive occurrences of the same digit
    hex_string = ''
    last_digit = ''
    while len(hex_string) < 7:
        digit = random.choice('0123456789ABCDEF')
        if digit != last_digit:
            hex_string += digit
            last_digit = digit
    return hex_string
    # 0123456789ABCDEF

def insert_hex(pattern, hex_string):
    # Replace 'xxxxxxx' characters in the pattern with the hex string
    result = pattern.replace('xxxxxxx', hex_string)
    return result

def check_match(pattern):
    # Run the bitcrack.exe program and check if there is a successful match 
    command = ['BitCrack.exe', '-b', '672', '-t', '256', '-p', '256', '--stride', '100000000',
               '--keyspace', '2000000000' + pattern + ':3ffffffffffffffff', '-o', 'FOUND.txt',
               '-c', '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so']
    subprocess.Popen(command, shell=True)

def save_tried_hex(hex_string):
    # Save the tried hex string to the 'tried.txt' file
    with open('tried.txt', 'a') as f:
        f.write(hex_string + '\n')

def load_tried_hex():
    # Load the tried hex strings from the 'tried.txt' file
    try:
        with open('tried.txt', 'r') as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        return set()

def generate_and_check(pattern):
    tried_hex_strings = load_tried_hex()

    while True:
        hex_string = generate_hex()
        if hex_string in tried_hex_strings:
            continue  # Skip already tried hex string
        tried_hex_strings.add(hex_string)

        save_tried_hex(hex_string)
        modified_pattern = insert_hex(pattern, hex_string)
        check_match(modified_pattern)
        print("Pattern:", modified_pattern)
        time.sleep(33)  # Wait for 30 seconds before restarting
        # input("Press Enter to continue...")
        # Add additional conditions to check for success or exit the loop if desired

# Example usage
pattern = "xxxxxxx"  # Replace 'xxxxxxx' with the generated hex string
generate_and_check(pattern)
