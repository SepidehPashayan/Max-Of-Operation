# 🔢 Maximum Expression Finder

> A Python utility that takes three integers and finds the maximum possible result  
> by trying every combination of `+` and `×` operators — including grouped expressions.

![Python](https://img.shields.io/badge/Language-Python-blue)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 🧠 How It Works

Given three integers `a`, `b`, `c` (entered as `a?b?c`), the program evaluates all possible arithmetic combinations:

| Expression | Example (2, 3, 4) |
|---|---|
| `a × b × c` | 2 × 3 × 4 = **24** |
| `a × b + c` | 2 × 3 + 4 = 10 |
| `a + b × c` | 2 + 3 × 4 = 14 |
| `a × (b + c)` | 2 × (3 + 4) = 14 |
| `(a + b) × c` | (2 + 3) × 4 = 20 |
| `a + b + c` | 2 + 3 + 4 = 9 |

Then returns the **maximum** result among all six.

---

## 🖥️ Usage

### Run

```bash
python company.py
```

### Input format

Enter exactly **three integers** separated by `?`:

```
2?3?4
```

### Output

```
24
```

---

## ✅ Input Validation

| Error | Message |
|---|---|
| Wrong number of values | `the number of character is not correct` |
| Non-integer input | `please just enter numbers` |

The program keeps prompting until valid input is received.

---

## 📁 Project Structure

```
max-expression/
└── company.py     # Input handler + expression evaluator
```

---

## 👩‍💻 Author

**Sepideh Pashayan** 
