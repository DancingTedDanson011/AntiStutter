# Contributing to AntiStutter 🤝

First off, thank you for considering contributing to AntiStutter! It's people like you who make this tool better for the stuttering community.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Scientific Contributions](#scientific-contributions)

---

## 📜 Code of Conduct

This project follows a simple principle: **Be respectful and constructive**.

- Be welcoming to newcomers
- Respect differing viewpoints
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards other contributors

---

## 🎯 How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title** and description
- **Steps to reproduce** the problem
- **Expected vs. actual behavior**
- **Screenshots** (if applicable)
- **System information**:
  - OS version
  - Python version
  - Audio hardware
  - Log files from `%USERPROFILE%\.antistutter\logs\`

Use the [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md)

### 💡 Suggesting Features

Feature suggestions are welcome! Please:

- **Check existing feature requests** first
- **Explain the problem** you're trying to solve
- **Describe your proposed solution**
- **Consider alternatives** you've thought about
- **Include research** if suggesting new DSP techniques

Use the [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md)

### 📖 Improving Documentation

Documentation improvements are always welcome:

- Fix typos or clarify explanations
- Add examples or usage scenarios
- Translate documentation (e.g., Spanish, French, Chinese)
- Improve code comments

### 💻 Code Contributions

#### Good First Issues

Look for issues labeled `good first issue` or `help wanted`

#### Areas for Contribution

- **DSP Algorithms**: Improve delay, pitch shifting, or binaural beats
- **GUI Enhancements**: Better widgets, dark mode, accessibility
- **Cross-Platform**: Linux/macOS support
- **Performance**: Reduce latency, CPU usage
- **Testing**: Unit tests, integration tests, user testing
- **Localization**: Multi-language support

---

## 🛠️ Development Setup

### Prerequisites

- Python 3.10+
- Git
- Windows 10/11 (for testing)
- Audio interface (microphone + headphones)

### Setup

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/antistutter.git
cd antistutter

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install development dependencies (optional)
pip install pytest black flake8 mypy

# 5. Run tests
python tests/test_audio.py

# 6. Run application
python src/main.py
```

### Project Structure

```
src/
├── main.py              # Entry point
├── audio_engine.py      # Audio processing core
├── dsp/                 # DSP algorithms
│   ├── delay.py
│   ├── pitch_shift.py
│   ├── metronome.py
│   └── binaural.py
├── gui/                 # GUI components
│   ├── main_window.py
│   ├── widgets.py
│   └── presets.py
└── utils/               # Utilities
    ├── config.py
    └── logger.py
```

---

## 📝 Coding Standards

### Python Style

- Follow **PEP 8** style guide
- Use **type hints** where appropriate
- Write **docstrings** for all public functions/classes
- Keep functions **small and focused**

```python
def process_audio(audio: np.ndarray, delay_ms: int) -> np.ndarray:
    """
    Process audio with delayed feedback.

    Args:
        audio: Input audio samples
        delay_ms: Delay time in milliseconds

    Returns:
        Processed audio samples
    """
    # Implementation
    pass
```

### Code Formatting

```bash
# Format code
black src/

# Check style
flake8 src/

# Type checking
mypy src/
```

### Testing

- Write tests for new features
- Ensure existing tests pass
- Aim for >80% code coverage (DSP modules)

```bash
# Run tests
python tests/test_audio.py
```

---

## 📤 Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding/updating tests
- `chore`: Maintenance tasks

#### Examples

```
feat(dsp): Add adaptive delay algorithm

Implements dynamic delay adjustment based on speech rate.
Reduces stuttering by additional 10% in tests.

Closes #42
```

```
fix(gui): Fix level meter overflow

Level meter was clipping at high input volumes.
Now properly normalizes to 0-1 range.

Fixes #38
```

---

## 🔄 Pull Request Process

### Before Submitting

1. **Update documentation** if needed
2. **Add tests** for new features
3. **Run all tests** locally
4. **Format code** (black, flake8)
5. **Update CHANGELOG.md** (if significant change)

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Self-reviewed code
- [ ] Commented complex code
- [ ] Updated documentation
- [ ] Added tests (if applicable)
- [ ] All tests pass
- [ ] No merge conflicts

### PR Title Format

```
[Type] Brief description

Example:
[Feature] Add Spanish language support
[Fix] Resolve audio feedback loop
[Docs] Update installation guide
```

### Review Process

1. **Automated checks** run (if CI/CD set up)
2. **Maintainer review** (1-3 days typically)
3. **Address feedback** if requested
4. **Approval & merge**

---

## 🎓 Scientific Contributions

### Adding Research

If contributing new DSP techniques or parameters:

1. **Cite peer-reviewed research**
2. **Include PDF** in repository (if permissible)
3. **Document parameters** thoroughly
4. **Provide evidence** of effectiveness

#### Research Contribution Template

```markdown
## New Technique: [Name]

### Research Basis
- **Paper**: Author et al. (Year). "Title". Journal, Volume(Issue), Pages.
- **DOI**: https://doi.org/...

### Effectiveness
- Stuttering reduction: X%
- Optimal parameters: [details]
- Tested on: N participants

### Implementation
[Technical details]

### References
[Full citations]
```

### Clinical Data

If sharing clinical results:

- **Anonymize all data**
- **Obtain proper consent**
- **Follow ethical guidelines**
- **Include IRB approval** (if applicable)

---

## 🌐 Translation Contributions

Help make AntiStutter accessible worldwide!

### Adding a New Language

1. Copy `README.md` → `README_XX.md` (XX = language code)
2. Translate all text
3. Update GUI strings in `src/gui/` (create i18n system if needed)
4. Update language selector in main README

### Translation Guidelines

- Maintain technical accuracy
- Keep formatting consistent
- Preserve links and badges
- Translate code comments (optional)

---

## 🐛 Bug Triage

Help wanted for:

- Reproducing reported bugs
- Adding debug information
- Testing fixes
- Closing resolved issues

---

## 💬 Community

- **GitHub Discussions**: Ask questions, share ideas
- **Issues**: Bug reports and feature requests
- **Pull Requests**: Code contributions

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.

This means:
- Your contributions can be used freely for non-commercial purposes
- Commercial use requires separate licensing
- You retain copyright of your original contributions
- By contributing, you grant the project perpetual rights to use your code under CC BY-NC 4.0

---

## 🙏 Recognition

All contributors will be:

- Listed in **CONTRIBUTORS.md**
- Mentioned in **release notes**
- Credited in **CITATION.cff**

---

## ❓ Questions?

Not sure how to start? Feel free to:

- Open a **Discussion** thread
- Comment on an existing **Issue**
- Reach out to maintainers

**Thank you for making AntiStutter better!** 🎤✨

---

*Happy Contributing!*
