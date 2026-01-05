# IS4010 Course

**Course**: IS4010 - AI-Enhanced Application Development
**Institution**: University of Cincinnati, Lindner College of Business
**Instructor**: Brandon M. Greenwell

---

## Overview

This repository is the template for all IS4010 lab assignments. You will fork this repository at the beginning of the course and complete all labs within your fork.

## Repository Structure

```
is4010-course/
├── module01/          # Week 1: Development Toolkit Setup
├── module02/          # Week 2: AI-Assisted Development
├── module03/          # Week 3: Python Basics + Testing
├── module04/          # Week 4: Data Structures
├── module05/          # Week 5: Functions and Error Handling
├── module06/          # Week 6: Object-Oriented Programming
├── module07/          # Week 7: Data and APIs
├── module08/          # Week 8: Python CLI Application
├── module09/          # Week 9: Rust Basics
├── module10/          # Week 10: Ownership and Borrowing
├── module11/          # Week 11: Structuring Code and Data
├── module12/          # Week 12: Generics and Traits
├── module13/          # Week 13: Idiomatic Rust
├── module14/          # Week 14: Rust CLI Application
├── resources/      # Setup guides and documentation
│   └── SETUP_GUIDE.md  # Comprehensive installation guide
├── .github/        # GitHub Actions CI/CD workflows
├── requirements.txt    # Python dependencies
└── README.md       # This file
```

## Getting Started

### 1. Fork This Repository

1. Click the "Fork" button in the top-right corner of this repository
2. Choose your personal GitHub account as the destination
3. Ensure the repository is **private**
4. Name your fork: `is4010-[your-username]-course` (e.g., `is4010-jdoe-course`)

### 2. Add Instructor as Collaborator

1. Go to your forked repository settings
2. Navigate to "Collaborators and teams"
3. Add `bgreenwell` (or your instructor's GitHub username) as a collaborator
4. This allows the instructor to view your private repository for grading

### 3. Clone Your Fork Locally

```bash
git clone https://github.com/YOUR-USERNAME/is4010-YOUR-USERNAME-course.git
cd is4010-YOUR-USERNAME-course
```

### 4. Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows (Git Bash):
source venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt
```

### 5. Verify Rust Installation

```bash
# Check Rust toolchain
rustc --version
cargo --version

# Should show Rust 1.70+ and Cargo
```

## Weekly Workflow

Each week, you'll complete a lab assignment:

1. **Read the lab README** in the corresponding `labXX/` folder
2. **Write your code** following the lab instructions
3. **Run tests locally** to verify your solution
4. **Commit and push** your changes to GitHub
5. **Verify CI/CD** - Check that GitHub Actions shows a green checkmark

### Example: Completing Lab 03

```bash
# Navigate to lab folder
cd module03/

# Write your code
# - Create module03.py with your solution
# - Create tests/test_module03.py with tests

# Run tests locally
pytest tests/ -v

# Commit your work
git add module03/
git commit -m "Complete Lab 03: Python Basics"
git push origin main

# Check GitHub Actions
# - Go to your repository on GitHub
# - Click "Actions" tab
# - Verify "Lab 03 - Python Basics" workflow shows green checkmark ✓
```

## CI/CD and Grading

Each lab has an automated GitHub Actions workflow that runs when you push code:

- **Python labs (3-8)**: Run `pytest` to verify your tests pass
- **Rust labs (9-14)**: Run `cargo test`, `cargo fmt --check`, and `cargo clippy`

**Grading is based on CI/CD status**:
- ✅ **Green checkmark** = Lab passes (full credit)
- ❌ **Red X** = Lab fails (no credit until fixed)

**You must verify your CI/CD passes before the lab deadline.**

## Lab Descriptions

### Python Track (Weeks 1-8)

| Lab | Chapter | Topic |
|-----|---------|-------|
| 01 | Ch 1 | Development Toolkit Setup |
| 02 | Ch 2 | AI-Assisted Development |
| 03 | Ch 3 | Python Basics + Testing Infrastructure |
| 04 | Ch 4 | Data Structures |
| 05 | Ch 5 | Functions and Error Handling |
| 06 | Ch 6 | Object-Oriented Programming |
| 07 | Ch 7 | Data and APIs |
| 08 | Ch 8 | Python CLI Application (Integrative) |

### Rust Track (Weeks 9-14)

| Lab | Chapter | Topic |
|-----|---------|-------|
| 09 | Ch 9 | Rust Basics |
| 10 | Ch 10 | Ownership and Borrowing |
| 11 | Ch 11 | Structuring Code and Data |
| 12 | Ch 12 | Generics and Traits |
| 13 | Ch 13 | Idiomatic Rust |
| 14 | Ch 14 | Rust CLI Application (Integrative) |

## Important Notes

### Independent Labs
Each lab is **self-contained** and **independent**:
- You don't copy code from previous labs
- Each lab starts fresh with new exercises
- Failing one lab doesn't affect the next lab
- You can redo/skip labs without cascade failures

### AI Assistance Policy
You are **encouraged** to use AI coding assistants:
- **GitHub Copilot** (in-editor suggestions)
- **Gemini CLI** (terminal assistance)
- **ChatGPT, Claude, etc.** (conversational help)

**Academic Integrity Requirements**:
- You must **understand** all code you submit
- Document AI assistance in `module02/` and throughout
- The goal is **learning**, not just completion

### Testing Requirements
Starting with Lab 03, all labs require automated tests:
- **Python**: Use `pytest` framework
- **Rust**: Use built-in `cargo test`
- Tests must pass locally **and** in GitHub Actions
- Aim for comprehensive test coverage

## Troubleshooting

### Python Issues

**Virtual environment not activating:**
```bash
# Ensure you're in the repository root
pwd  # Should show .../is4010-YOUR-USERNAME-course

# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate  # macOS/Linux
source venv/Scripts/activate  # Windows Git Bash
```

**pytest not found:**
```bash
# Activate virtual environment first
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Rust Issues

**cargo command not found:**
```bash
# Install Rust toolchain
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Restart terminal, then verify
rustc --version
cargo --version
```

**Cargo.lock errors:**
- Cargo.lock is in .gitignore - don't commit it
- Run `cargo clean` if you see lock file errors

### GitHub Actions Failing

**Check the workflow log:**
1. Go to your repository on GitHub
2. Click "Actions" tab
3. Click the failing workflow run
4. Read the error messages
5. Fix the issue locally
6. Commit and push again

**Common issues:**
- Tests failing locally → Fix tests first
- Import errors → Check file names and paths
- Syntax errors → Run code locally before pushing

## Resources

- **Course Materials**: `is4010-course-template/` repository
- **Textbook**: *From Script to System* (aiappdev book)
- **Setup Guide**: See `is4010-course-template/resources/SETUP_GUIDE.md`
- **Lecture Notes**: See `is4010-course-template/resources/lecture-notes/`

## Getting Help

1. **Read the lab README** thoroughly
2. **Check the textbook chapter** corresponding to the lab
3. **Use AI assistants** for coding help (with understanding)
4. **Check CI/CD logs** for specific error messages
5. **Ask on course discussion board** (Microsoft Teams)
6. **Attend office hours** for instructor help

## License

Course materials © 2025 Brandon M. Greenwell, University of Cincinnati
