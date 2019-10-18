"""(a) Write a function to print the first N numbers of the Fibonacci sequence.
(b) Write a function to print the Nth number of the sequence."""

def fibonacci_sequence(n_series):
    term_1 , term_2 = 1, 1
    n_term = 0
    count = n_series
    while count >= 0:

        n_term = term_1 + term_2
        term_2 = term_1

        term_1 = n_term
        print(n_term, 'yes')
        count -=1

def recursive_fibonacci(n_seiries):
    if n_seiries == 0 or n_seiries == 1:
        return n_seiries
    else:
        return recursive_fibonacci(n_seiries - 1) + recursive_fibonacci(n_seiries - 2)


def main():
    n_series = int(input("Enter a series "))

    # fibonacci_sequence(n_series)
    nth_term = recursive_fibonacci(n_series)
    print(nth_term)

if __name__ == '__main__':
    main()


