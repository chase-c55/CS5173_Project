#!/usr/bin/env python3
import secrets
import numpy as np


def calculate_bits_entropy(numOptions: int, length: int) -> float:
    """Calculates the entropy of a password

    Args:
        num_options: the number of possible word options
        length: the number of words

    Return:
        float: the entropy of the password
    """

    return length * np.log2(numOptions)


def calc_num_years_from_bits_entropy(
    bits_entropy: int, checks_per_second: int
) -> tuple[float, float]:
    """Calculates the number of years to bruteforce a password with bits_entropy on classical and quantum computers

    Args:
        bits_entropy: the bits of entropy in the password
        checks_per_second: the number of checks per second

    Return:
        float: number of years on classical
        float: number of years on quantum
    """

    # Calculate years on classical
    classical_entropy = 2**bits_entropy
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
    COMPLEX_DICTIONARY = "/usr/share/dict/words"
    COMMON_DICTIONARY = "./30k.txt"

    min_entropy = 256  # Default to 256 bits of entropy
    checks_per_second = 10e18  # A quintillion checks per second (Fastest classical supercomputer) - Frontier
    dictionary_file = COMPLEX_DICTIONARY  # Default to complex dictionary

    match input("Would you like to use default settings (y/n)? "):
        case "y":
            pass
        case "n":
            try:
                in_bits = int(
                    input("Please enter the minimum entropy (bits) (default = 256): ")
                )
                min_entropy = in_bits
            except ValueError:
                print("Invalid input, using default")

            try:
                in_checks = int(
                    input(
                        "Please enter the number of checks per second (10^N) (default N = 18): "
                    )
                )
                checks_per_second = 10**in_checks
            except ValueError:
                print("Invalid input, using default")

            match input(
                "Please choose complexity of words (1 = common, 2 = complex (default)): "
            ):
                case "1":
                    dictionary_file = COMMON_DICTIONARY
                case "2":
                    dictionary_file = COMPLEX_DICTIONARY
                case default:
                    print("Invalid input, using default")
        case default:
            print("Invalid input, using default")

    # Get the word list from a file
    with open(dictionary_file) as file:
        words = [word.strip() for word in file]
        num_options = len(words)
        print(f"The number of possible words is {num_options}")

    num_words = 0
    bits_entropy = 0
    password = ""

    # Find a sufficiently complex password
    while bits_entropy < min_entropy:
        password += secrets.choice(words) + " "
        num_words += 1
        bits_entropy = calculate_bits_entropy(num_options, num_words)

    # Strip extra whitespace
    password = password.strip()

    # Convert to an integer for clarity
    bits_entropy = int(bits_entropy)
    qubits = int(np.ceil(np.log2(bits_entropy)))  # Assumption: log2(n) qubits required to solve, in reality much more complex

    # Calculate the years
    classical_years, quantum_years = calc_num_years_from_bits_entropy(
        bits_entropy, checks_per_second
    )

    # Print the stats
    print(f"Bits of entropy: {bits_entropy}")
    print(f"Qubits required: {qubits}")
    print(f"Years on classical computer: {classical_years}")
    print(f"Years on quantum computer: {quantum_years}")

    # Print the number of words and the generated password
    print(f"The number of words is {num_words}")
    print("#" * 30)
    print(f"The password is:\n{password}")
    print("#" * 30)

    # Verify the password
    num_verifications = 3
    while num_verifications > 0:
        if input("Please enter the password to verify:\n").strip().lower() == password.lower():
            num_verifications -= 1
            print("Password verified successfully. Remaining verifications:", num_verifications)
        else:
            print("Password verification failed. Remaining verifications:", num_verifications)
