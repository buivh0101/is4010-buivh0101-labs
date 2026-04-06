# Lab 13: Idiomatic Rust

**Due**: Sunday at 11:59 PM &nbsp; **Points:** 10

Open `src/main.rs` and implement every `todo!()`. The test suite is pre-written — make it pass. Do not modify the test module.

When implementing a function, rename parameters by dropping the leading `_`.

## What to implement

**Part 1 — Iterators and closures**

| Function | Description |
|----------|-------------|
| `analyze_text(text)` | Return `(word_count, avg_word_length, longest_word)`; use iterator adaptors |
| `process_numbers(numbers)` | Sum of squares of all even numbers: `[1,2,3,4]` → `4+16 = 20` |
| `make_counter()` | Return a closure (`impl FnMut() -> i32`) that increments on each call |

For `make_counter`: the closure wrapper is already in place — rename `_count` → `count`, increment it, and return the new value.

**Part 2 — Error handling with `Result`**

| Function / type | Description |
|-----------------|-------------|
| `divide(a, b)` | `Ok(a / b)` or `Err("division by zero")` when `b == 0.0` |
| `Display for ParseError` | Both variants must produce a non-empty message |
| `parse_positive_number(input)` | Parse `input` as `i32 > 0`; return `ParseError::NotANumber` or `ParseError::NotPositive` on failure |

## Commands

```bash
cargo test
cargo fmt
cargo clippy -- -D warnings
```

## Submit

```bash
git add week13/
git commit -m "Complete lab 13"
git push origin main
```

Verify a green checkmark on the **Actions** tab of your GitHub fork.
