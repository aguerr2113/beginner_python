# User Input Handling: Understanding how to prompt users for input and retrieve their responses using the input function.

# Function Definition: Learning how to define and call a function (get_input) that takes parameters and returns values.

# String Interpolation: Using f-strings to dynamically insert variables into a string, a feature introduced in Python 3.6, which makes string formatting more concise and readable.

# Type Annotations: Utilizing type hints to specify the expected data type of function parameters and local variables. This can improve code readability and potentially assist in error detection, especially in larger code bases.

# Reuse and Modularity: Applying the principle of "Don't Repeat Yourself" (DRY) by creating a reusable function to avoid duplicating code.

# Multiline String Literals: Creating multiline string literals with triple quotes to represent larger text blocks. This is a useful feature for working with large strings in Python.

# Variable Naming and Scope: Understanding variable naming, scope, and how function parameters and return values are used to pass information between different parts of the code.

def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}:")
    return user_input
noun1 = get_input('Noun ')
verb1 = get_input('Verb ')
noun2 = get_input('Noun ')
verb2 = get_input('Verb ')

story = f"""
Once upon a time, there was a {noun1} who loved {verb1} all day.
One day, {noun2} walked into the room and caught the {noun1} in the act.
{noun2}: "What are you doing?"
{noun1}: "I'm just {verb1}ing, whats the big deal?"
{noun2}: "Well its not every day that you see a {noun1} {verb1}ing in the middle of the day."
{noun1}: "I guess your right "
{noun2}: "Thats probably a good idea . Why dont we go {verb2} instead?"
{noun1}: " Sure"

And so, {noun2} and the {noun1} went off to {verb2} and had a greate time.
 """

print(story)