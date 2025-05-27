from nltk.sem import Expression
from nltk.logic import LogicParser

# Define a logic parser
parser = LogicParser()

# Sample logical expressions in FOPC
expressions = [
    "all x.(dog(x) -> animal(x))",  # ∀x (Dog(x) → Animal(x))
    "exists x.(cat(x) & black(x))"  # ∃x (Cat(x) ∧ Black(x))
]

# Parse and display results
print("Parsed Logical Expressions:")
for expr in expressions:
    parsed_expr = parser.parse(expr)
    print(f"{expr}  →  {parsed_expr}")
