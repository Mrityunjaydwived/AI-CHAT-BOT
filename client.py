import google.generativeai as genai
genai.configure(api_key="AIzaSyBAUP2S02i_aqJ9dJyqvGT1QJzu_XTu0nw")
model = genai.GenerativeModel("gemini-1.5-flash")
command = '''
Copied Text: Functions and recursion
Basic math operations
2. Mathematics
Number Theory:
Prime numbers and primality tests
Sieve of Eratosthenes
Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
Modular arithmetic (modulo properties)
Modular exponentiation
Chinese Remainder Theorem
Combinatorics:
Permutations and combinations
Factorials and binomial coefficients
Geometry:
Points, lines, and ci…
'''
response = model.generate_content(f"you are a person named harry who speaks hindi as well as english . He is from India and is a coder. you analyze chat history and respond like harry. {command} ")
print(response.text)