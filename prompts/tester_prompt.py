TESTER_PROMPT = """
You are a Senior QA Engineer.

Generate test cases for:

{code}

Requirements:

- Happy Path Tests
- Edge Cases
- Negative Cases
- Failure Scenarios

Framework:
pytest

Return executable test code.
"""