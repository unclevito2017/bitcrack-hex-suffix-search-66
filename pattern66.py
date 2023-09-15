import subprocess
import random
import time

def generate_hex():
    # Generate a random 7-digit hex string
    hex_string = ''.join(random.choices('0123456789ABCDEF', k=7))
    return hex_string

def insert_hex(pattern, hex_string):
    # Replace 'xxxxxxx' characters in the pattern with the hex string
    result = pattern.replace('xxxxxxx', hex_string)
    return result

def check_match(pattern):
    # Run the bitcrack program and check if there is a successful match
    command = ['./cuBitCrack', '-b', '128', '-t', '256', '-p', '1280', '--stride', '100000000',
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
        time.sleep(33)  # Wait for 33 seconds before restarting
        # input("Press Enter to continue...")
        # Add additional conditions to check for success or exit the loop if desired

# Example usage
pattern = "xxxxxxx"  # Replace 'xxxxxxx' with the generated hex string
generate_and_check(pattern)
