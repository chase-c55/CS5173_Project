import secrets
import numpy as np

def calculate_entropy(numOptions, length):
    """Calculates the entropy of a password
    
    Args:
        num_options: the number of possible word options
        length: the number of words
    
    Return:
        float: the entropy of the password
    """

    return length * np.log2(numOptions)

def calc_num_years_from_bits_entropy(bits_entropy):
    """Calculates the number of years to bruteforce a password with bits_entropy on classical and quantum computers

    Args:
        bits_entropy: the bits of entropy in the password

    Return:
        float: number of years on classical
        float: number of years on quantum
    """
    
    CHECKS_PER_SEC = 10e18 # A quintillion checks per second (Fastest classical supercomputer) - Frontier
    classical_entropy = 2 ** bits_entropy
    class_seconds = classical_entropy / CHECKS_PER_SEC
    class_minutes = class_seconds / 60
    class_hours = class_minutes / 60
    class_days = class_hours / 24
    class_years = class_days / 365

    quantum_entropy = int(classical_entropy ** (1 / 2))
    quant_seconds = quantum_entropy / CHECKS_PER_SEC
    quant_minutes = quant_seconds / 60
    quant_hours = quant_minutes / 60
    quant_days = quant_hours / 24
    quant_years = quant_days / 365

    return class_years, quant_years

if __name__ == "__main__":
    MIN_ENTROPY = 256

    with open('/usr/share/dict/words') as f:
        words = [word.strip() for word in f]
        num_options = len(words)
        print(f"The number of options is {num_options}")

        num_words = 0
        bits_entropy = 0
        password = ''
        while bits_entropy < MIN_ENTROPY:
            password += secrets.choice(words) + " "
            num_words += 1
            bits_entropy = calculate_entropy(num_options, num_words)

        password.strip()
        bits_entropy = int(bits_entropy)

        years = calc_num_years_from_bits_entropy(bits_entropy)
        print(f"Years at {bits_entropy} bits entropy on classical computer: ", years[0],"\n"
            "Years on quantum computer: ", years[1])
        
        print(f"The number of words is {num_words}")
        print("The password is:\n", password)
