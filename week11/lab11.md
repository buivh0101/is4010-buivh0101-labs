# Lab 11: Structs, enums, and methods

**Due**: Sunday at 11:59 PM &nbsp; **Points:** 10

Open `src/student.rs` and implement every `todo!()`. The types (`Student`, `Grade`, `CourseGrade`, `StudentDatabase`) are already defined — do not change them. The test suite is pre-written — make it pass. Do not modify the test module.

When implementing a method, rename parameters by dropping the leading `_` (e.g., `_id` → `id`).

## What to implement

**`Student`**

| Method | Description |
|--------|-------------|
| `new(id, name, email)` | `credits_earned` starts at 0, `grades` starts empty |
| `class_standing()` | `"Freshman"` 0–29 cr, `"Sophomore"` 30–59, `"Junior"` 60–89, `"Senior"` 90+ |
| `add_credits(credits)` | Add to `credits_earned` |
| `can_graduate()` | `true` if `credits_earned >= 120` |
| `add_grade(course_grade)` | Append to `grades` |
| `calculate_gpa()` | Weighted GPA = total quality points / total credit hours; `0.0` if no grades |

**`Grade`**

| Method | Description |
|--------|-------------|
| `to_gpa_points()` | `A→4.0`, `B→3.0`, `C→2.0`, `D→1.0`, `F→0.0` |
| `from_string(s)` | Parse `"A"`–`"F"` (case-insensitive); `None` for anything else |
| `is_passing()` | `true` for A, B, C |

**`CourseGrade`**

| Method | Description |
|--------|-------------|
| `new(course_code, course_name, credits, grade)` | Construct a `CourseGrade` |
| `quality_points()` | `credits as f32 × grade.to_gpa_points()` |

**`StudentDatabase`**

| Method | Description |
|--------|-------------|
| `new()` | Empty database (uses `HashMap`) |
| `add_student(student)` | Add by id; return `Err(String)` if id already exists |
| `find_student(id)` | `Option<&Student>` |
| `find_student_mut(id)` | `Option<&mut Student>` |
| `student_count()` | Number of students |
| `average_gpa()` | Mean GPA across all students; `0.0` if empty |
| `list_students()` | `Vec<&Student>` of all students |

## Commands

```bash
cargo test
cargo fmt
cargo clippy -- -D warnings
```

## Submit

```bash
git add week11/
git commit -m "Complete lab 11"
git push origin main
```

Verify a green checkmark on the **Actions** tab of your GitHub fork.
