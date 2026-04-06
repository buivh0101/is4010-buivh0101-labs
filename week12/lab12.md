# Lab 12: Generics and traits

**Due**: Sunday at 11:59 PM &nbsp; **Points:** 10

Open `src/main.rs` and implement every `todo!()`. The `Stack<T>` struct and trait impl skeletons are already defined — make the pre-written tests pass. Do not modify the test module.

When implementing a method, rename parameters by dropping the leading `_`.

## What to implement

**`Stack<T>` methods**

| Method | Description |
|--------|-------------|
| `new()` | Return an empty stack backed by `Vec<T>` |
| `push(item)` | Append `item` to the top |
| `pop()` | Remove and return `Some(T)` from the top, or `None` if empty |
| `peek()` | Return `Some(&T)` to the top item without removing it, or `None` |
| `is_empty()` | `true` if the stack has no items |
| `len()` | Number of items |

**Trait impls**

| Impl | Description |
|------|-------------|
| `Display for Stack<T>` | Format as `[bottom, ..., top]`; empty stack as `[]` |

## Commands

```bash
cargo test
cargo fmt
cargo clippy -- -D warnings
```

## Submit

```bash
git add week12/
git commit -m "Complete lab 12"
git push origin main
```

Verify a green checkmark on the **Actions** tab of your GitHub fork.
