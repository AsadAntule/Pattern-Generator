import os

# Size validation for Decor
def size_limit(func):
    def wrapper(self, n):
        if n < 1 or n > 20:
            raise ValueError("Size must be between 1 and 20!")
        return func(self, n)
    return wrapper

class PatternGenerator:
    def __init__(self):
        self.save_file = "Saved_Patterns.txt"
        if not os.path.exists("Patterns"):
            os.makedirs("Patterns")

    # Pyramid Pattern
    @size_limit
    def generate_pyramid(self, n):
        pattern = []
        for i in range(1, n + 1):
            line = " " * (n - i) + " ".join([str(j) for j in range(1, i + 1)])
            pattern.append(line)
        return "\n".join(pattern)

    # Reverse Pyramid pattern
    @size_limit
    def generate_reverse_pyramid(self, n):
        pattern = []
        for i in range(n, 0, -1):
            line = " " * (n - i) + " ".join([str(j) for j in range(1, i + 1)])
            pattern.append(line)
        return "\n".join(pattern)

    # Floyds Triangle pattern
    @size_limit
    def generate_floyd(self, n):
        pattern = []
        num = 1
        for i in range(1, n + 1):
            row = []
            for _ in range(i):
                row.append(str(num))
                num += 1
            pattern.append(" ".join(row))
        return "\n".join(pattern)

    # Pascal Triangle Pattern
    @size_limit
    def generate_pascal(self, n):
        triangle = [[1]]
        for i in range(1, n):
            row = [1] + [
                triangle[i - 1][j] + triangle[i - 1][j + 1]
                for j in range(len(triangle[i - 1]) - 1)
            ] + [1]
            triangle.append(row)

        return "\n".join(" ".join(str(x) for x in row) for row in triangle)

    # Fibonacci pattern
    @size_limit
    def generate_fibonacci(self, n):
        f = [0, 1]
        add = lambda a, b: a + b

        for _ in range(2, n):
            f.append(add(f[-1], f[-2]))

        return "".join(str(x) for x in f[:n])

    # Saving Patterns
    def save_pattern(self, name, pattern):
        file_path = os.path.join("Patterns", f"{name}.txt")
        with open(file_path, "w") as f:
            f.write(pattern)

        with open(self.save_file, "a") as f:
            f.write(f"\n === {name} ===\n{pattern}\n")

        return f"saved in {file_path}"