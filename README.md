
# **Practice Repository: Adding Numbers**

Welcome to your practice repository! This project is a simple coding exercise to help you get familiar with GitHub Classroom, working with functions, and using autograding to receive immediate feedback.

---

## **Project Overview**

The goal of this project is to implement a function that adds two numbers together and returns the result. This will help you understand how to work with functions, write testable code, and use GitHub Actions for autograding.

---

## **Task Description**

1. Open the `main.py` file in the repository.
2. Complete the `add_numbers(a, b)` function. It should:
   - Take two integers, `a` and `b`, as input.
   - Return the sum of the two integers.
3. Test your implementation using the examples provided in `main.py`.

---

## **How Autograding Works**

This repository is set up with autograding using GitHub Actions and `pytest`. Here’s how it works:

1. When you **push your code** to your GitHub repository or create a pull request, the autograder will automatically run the tests in the `test_main.py` file.
2. The autograder will check whether your implementation of `add_numbers(a, b)` passes all the test cases.
3. You can see the test results by going to the **Actions** tab of your GitHub repository.

---

## **Steps to Complete the Task**

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   ```
2. **Edit `main.py`:**
   Complete the `add_numbers` function as described.
3. **Test Locally:**
   Run the file locally to test your implementation:
   ```bash
   python main.py
   ```
4. **Push Your Code:**
   After implementing and testing your code, push your changes to the repository:
   ```bash
   git add .
   git commit -m "Completed add_numbers function"
   git push
   ```
5. **Check Autograding Results:**
   - Go to the **Actions** tab in your repository.
   - View the test results to see if your code passed all the test cases.

---

## **Example Input and Output**

Here’s what your function should do:

### **Example 1**
Input:
```python
add_numbers(1, 2)
```
Output:
```
3
```

### **Example 2**
Input:
```python
add_numbers(-1, 1)
```
Output:
```
0
```

---

## **Notes**
- Make sure your function passes all the test cases in `test_main.py`.
- You can modify and re-push your code as many times as needed until all tests pass.

Happy coding!
