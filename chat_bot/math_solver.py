import sympy as sp

def solve_math_expression(expression):
    try:
        result = sp.sympify(expression)
        return f"The result of the expression {expression} is: {result}"
    except (sp.SympifyError, SyntaxError):
        return "There was an error processing the math expression."
