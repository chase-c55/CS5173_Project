import secrets
import numpy as np

def calculate_bits_entropy(numOptions, length):
    """Calculates the entropy of a password
    
    Args:
        num_options: the number of possible word options
        length: the number of words
    
    Return:
        float: the entropy of the password
    """

    return length * np.log2(numOptions)

def calc_num_years_from_bits_entropy(bits_entropy, checks_per_second):
    """Calculates the number of years to bruteforce a password with bits_entropy on classical and quantum computers

    Args:
        bits_entropy: the bits of entropy in the password

    Return:
        float: number of years on classical
        float: number of years on quantum
    """
    
    # Calculate years on classical
    classical_entropy = 2 ** bits_entropy
    class_seconds = classical_entropy / checks_per_second
    class_minutes = class_seconds / 60
    class_hours = class_minutes / 60
    class_days = class_hours / 24
    class_years = class_days / 365

    # Calculate years on quantum
    quantum_entropy = int(classical_entropy ** (1 / 2))
    quant_seconds = quantum_entropy / checks_per_second
    quant_minutes = quant_seconds / 60
    quant_hours = quant_minutes / 60
    quant_days = quant_hours / 24
    quant_years = quant_days / 365

    return class_years, quant_years


if __name__ == "__main__":
    MIN_ENTROPY = 256
    CHECKS_PER_SECOND = 10e18 # A quintillion checks per second (Fastest classical supercomputer) - Frontier

    # Get the word list from a file
    dictionary_file = "/usr/share/dict/words"
    with open(dictionary_file) as file:
        words = [word.strip() for word in file]
        num_options = len(words)
        print(f"The number of options is {num_options}")

    num_words = 0
    bits_entropy = 0
    password = ''

    # Find a sufficiently complex password
    while bits_entropy < MIN_ENTROPY:
        password += secrets.choice(words) + " "
        num_words += 1
        bits_entropy = calculate_bits_entropy(num_options, num_words)

    # Strip extra whitespace
    password.strip()

    # Convert to an integer for clarity
    bits_entropy = int(bits_entropy)

    # Calculate the years
    classical_years, quantum_years = calc_num_years_from_bits_entropy(bits_entropy, CHECKS_PER_SECOND)
    print(f"Bits of entropy: {bits_entropy}")
    print(f"Years on classical computer: {classical_years}")
    print(f"Years on quantum computer: {quantum_years}")
    
    # Print the number of words and the generated password
    print(f"The number of words is {num_words}")
    print("#" * 30)
    print(f"The password is:\n{password}")
    print("#" * 30)
