import os
import sys

def create_problem(problem_name, difficulty):
    difficulty = difficulty.lower()
    if difficulty not in ["easy", "medium", "hard"]:
        print("Difficulty must be: easy, medium, or hard")
        sys.exit(1)

    problem_name = problem_name.lower().replace(" ", "-")
    base_path = os.path.join(difficulty, problem_name)

    if os.path.exists(base_path):
        print(f"Problem '{problem_name}' already exists under '{difficulty}/'")
        sys.exit(1)

    # --- README ---
    readme_content = f"""# {problem_name.replace("-", " ").title()}

**Difficulty:** {difficulty.capitalize()}  
**Link:** https://leetcode.com/problems/{problem_name}/

## Problem

<!-- Paste the problem description here -->

## Constraints

<!-- Paste the constraints here -->

## Examples

<!-- Paste the examples here -->

## Notes

<!-- Your approach, time/space complexity, what tripped you up -->
"""

    # --- Java ---
    class_name = "Solution"
    java_content = f"""class {class_name} {{

    public static void main(String[] args) {{
        {class_name} solution = new {class_name}();
        // TODO: add test cases
    }}
}}
"""

    # --- Python ---
    python_content = f"""class Solution(object):
    pass

if __name__ == '__main__':
    solution = Solution()
    # TODO: add test cases
"""

    files = {
        os.path.join(base_path, "README.md"): readme_content,
        os.path.join(base_path, "java", "solution.java"): java_content,
        os.path.join(base_path, "python", "solution.py"): python_content,
    }

    for path, content in files.items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)

    print(f"Created '{problem_name}' under '{difficulty}/'")
    print(f"  {base_path}/")
    print(f"  ├── README.md")
    print(f"  ├── java/solution.java")
    print(f"  ├── python/solution.py")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python new_problem.py <problem-name> <difficulty>")
        print("Example: python new_problem.py two-sum easy")
        sys.exit(1)

    create_problem(sys.argv[1], sys.argv[2])
