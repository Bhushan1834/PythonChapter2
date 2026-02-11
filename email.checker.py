# Gmail Validation Program

email = input("Enter your email: ").strip().lower()

# basic checks
if not email:
    print("❌ Email cannot be empty")

elif "@" not in email:
    print("❌ Invalid email: '@' missing")

elif not email.endswith("@gmail.com"):
    print("❌ Only Gmail addresses are allowed")

elif email.startswith("@"):
    print("❌ Invalid email format")

else:
    print(f"✅ Valid Gmail: {email}")



import traceback

def execute_code(code):
    try:
        exec(code)
        return {
            "status": "success",
            "output": "Code executed successfully"
        }
    except Exception as e:
        return {
            "status": "error",
            "error_type": type(e).__name__,
            "error_message": str(e),
            "traceback": traceback.format_exc()
        }
def explain_error(error_type):
    errors = {
        "SyntaxError": "Syntax mistake in code.",
        "NameError": "Variable not defined.",
        "TypeError": "Wrong data type used.",
        "ZeroDivisionError": "Division by zero.",
        "IndentationError": "Indentation issue."
    }
    return errors.get(error_type, "Unknown error.")

    import openai
    from config import OPENAI_API_KEY

    openai.api_key = OPENAI_API_KEY

def fix_code_with_ai(code, error_message):
    prompt = f"""
You are a Python expert.
The following code has an error.

CODE:
{code}

ERROR:
{error_message}

Explain the error briefly and provide corrected code.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

    from executor import execute_code
    from error_analyzer import explain_error
    from ai_fixer import fix_code_with_ai

print("🔹 Enter Python code (type END to finish):")

user_code = ""
while True:
    line = input()
    if line == "END":
        break
    user_code += line + "\n"

result = execute_code(user_code)

if result["status"] == "success":
    print("\n✅ Code executed successfully")

else:
    print("\n❌ ERROR DETECTED")
    print("Error Type:", result["error_type"])
    print("Error Message:", result["error_message"])

    print("\n🧠 Explanation:")
    print(explain_error(result["error_type"]))

    print("\n🤖 AI Suggested Fix:")
    ai_response = fix_code_with_ai(user_code, result["error_message"])
    print(ai_response)
