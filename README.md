# 🔧 Python Utilities Collection

This repository contains a collection of simple yet practical Python programs for beginners and learners.  
Each program is self-contained, demonstrates core Python concepts, and solves a real-world problem — from inventory management to secure password generation.

---

## 📦 1. EOQ Model Calculator (Using Function)

**Filename:** `EOQ Model Calculator (using function).py`  
**Description:** A command-line based Python program to calculate the **Economic Order Quantity (EOQ)** using three different models in inventory management.

**Key Features:**
- Accepts inputs:
  - Annual Demand (A)
  - Demand Rate (λ)
  - Inventory Carrying Cost (Ic)
  - Production Rate (Xi)
  - Shortage Cost (Pi)
- Calculates EOQ for:
  - **Model 1**: Basic EOQ without production or shortages  
    `EOQ1 = √((2 × A × λ) / Ic)`
  - **Model 2**: EOQ with finite production rate (gradual replenishment)  
    `EOQ2 = √(((2 × A × λ) / Ic) × (Xi / (Xi - λ)))`
  - **Model 3**: EOQ with shortages allowed (backordering)  
    `EOQ3 = √(((2 × A × λ) / Ic) × ((Ic + Pi) / Pi))`
- Returns EOQ rounded to 2 decimal places.
- User-friendly interface and input validation.

---

## 📦 2. EOQ Model Calculator (Using match-case)

**Filename:** `EOQ Model Calculator (using match).py`  
**Description:** A command-line Python tool for calculating EOQ using `match-case`, introduced in Python 3.10+, for cleaner control flow.

**Key Features:**
- Interactive selection of EOQ models using `match-case`.
- EOQ formulas:
  - **Model 1**: Basic EOQ  
    `EOQ1 = √((2 × A × λ) / Ic)`
  - **Model 2**: EOQ with production  
    `EOQ2 = √(((2 × A × λ) / Ic) × (Xi / (Xi - λ)))`
  - **Model 3**: EOQ with shortages  
    `EOQ3 = √(((2 × A × λ) / Ic) × ((Ic + Pi) / Pi))`
- Validates that production rate > demand rate.
- Shows how EOQ varies with input values.

---

## 🔐 3. Password Generator

**Filename:** `Password Generator.py`  
**Description:** A secure password generator that creates random passwords based on user-defined length and complexity preferences.

**Key Features:**
- Prompts user for:
  - Minimum password length
  - Inclusion of numbers and/or special characters
- Generates strong, random passwords using:
  - Uppercase letters
  - Lowercase letters
  - Digits (optional)
  - Special characters (optional)
- Ensures the generated password meets selected criteria.
- Uses only built-in libraries: `random` and `string`.

---

## ➕ 4. Simple Calculator

**Filename:** `Simple Calculator.py`  
**Description:** A basic calculator for performing standard arithmetic operations interactively.

**Key Features:**
- Supported operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
  - Power (^)
  - Factorial (!)
- Validates inputs (e.g., prevents division by zero and negative factorials).
- Good exercise in `if-else` control flow and user input handling.
- Uses Python's built-in `math` module for advanced operations.
