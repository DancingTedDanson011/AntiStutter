# GitHub Repository Setup Guide

This guide helps you prepare AntiStutter for GitHub.

## 📋 Pre-Upload Checklist

### Required Actions

- [ ] **Update GitHub username** in files:
  - [ ] `README.md` (replace `DancingTedDanson011`)
  - [ ] `README_DE.md` (replace `DancingTedDanson011`)
  - [ ] `CITATION.cff` (replace `DancingTedDanson011` and `your-email@example.com`)
  - [ ] `SECURITY.md` (replace `your-security-email@example.com`)
  - [ ] `CODE_OF_CONDUCT.md` (replace `your-email@example.com`)
  - [ ] `.github/FUNDING.yml` (uncomment and add your sponsors info)

- [ ] **Test locally**:
  ```bash
  # Run installation
  install.bat

  # Run application
  start.bat

  # Run tests
  run_tests.bat
  ```

- [ ] **Clean up**:
  ```bash
  # Remove virtual environment (will be recreated by users)
  rmdir /s /q venv

  # Remove logs (if any)
  rmdir /s /q logs

  # Remove user configs (if any)
  del /q *.user.json
  ```

---

## 🚀 Creating the Repository

### 1. Create Repository on GitHub

1. Go to https://github.com/new
2. Name: `antistutter`
3. Description: "Real-time stuttering reduction via scientifically-validated auditory stimulation"
4. Visibility: **Public**
5. Do NOT initialize with README (we have our own)
6. Click "Create repository"

### 2. Initial Commit & Push

```bash
cd C:\Users\DancingTedDanson\Desktop\AntiStutter

# Initialize git (if not done)
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit: AntiStutter v1.0.0

- Delayed Auditory Feedback (DAF)
- Frequency Altered Feedback (FAF)
- Rhythmic Metronome
- Binaural Beats
- PyQt5 GUI
- Comprehensive documentation
- Research PDFs included"

# Add remote
git remote add origin https://github.com/DancingTedDanson011/antistutter.git

# Push to main
git branch -M main
git push -u origin main
```

---

## ⚙️ Repository Settings

### General

- **Description**: "Real-time stuttering reduction via scientifically-validated auditory stimulation"
- **Website**: (Optional: Documentation site)
- **Topics**: Add relevant tags:
  - `stuttering`
  - `speech-fluency`
  - `delayed-auditory-feedback`
  - `binaural-beats`
  - `dsp`
  - `python`
  - `pyqt5`
  - `speech-therapy`
  - `research`
  - `windows`

### Features

- ✅ Issues
- ✅ Discussions (enable for community Q&A)
- ✅ Projects (optional: for roadmap)
- ✅ Wiki (optional: for extended docs)

### Pull Requests

- ✅ Allow squash merging
- ✅ Automatically delete head branches

### Security

- ✅ Private vulnerability reporting (enable if available)

---

## 📜 Create Releases

### Tag v1.0.0

```bash
# Create annotated tag
git tag -a v1.0.0 -m "Release v1.0.0

Initial public release with:
- DAF/FAF/Metronome/Binaural Beats
- 3 presets (Light/Medium/Strong)
- Real-time processing (<30ms latency)
- PyQt5 GUI
- Comprehensive documentation
- Research-backed parameters"

# Push tag
git push origin v1.0.0
```

### Create Release on GitHub

1. Go to https://github.com/DancingTedDanson011/antistutter/releases/new
2. Choose tag: `v1.0.0`
3. Release title: `AntiStutter v1.0.0 - Initial Release`
4. Description: Copy from CHANGELOG.md
5. Attach: (Optional) Pre-built Windows .exe if you create one
6. Click "Publish release"

---

## 📊 Repository Insights

### Recommended Labels

Create these labels for better issue management:

**Type:**
- `bug` (🐛 red)
- `enhancement` (✨ light blue)
- `documentation` (📖 blue)
- `question` (❓ purple)

**Priority:**
- `priority: high` (🔴 red)
- `priority: medium` (🟡 yellow)
- `priority: low` (🟢 green)

**Status:**
- `good first issue` (💚 green)
- `help wanted` (🆘 blue)
- `wontfix` (⛔ grey)
- `duplicate` (grey)

**Area:**
- `dsp` (audio processing)
- `gui` (user interface)
- `research` (scientific)

---

## 🎨 Repository Branding

### Create Social Preview Image (Optional)

Dimensions: 1280 x 640 px

Content:
```
┌────────────────────────────────────────┐
│         AntiStutter 🎤                 │
│                                        │
│  Real-time Stuttering Reduction       │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      │
│                                        │
│  🔊 DAF   🎵 FAF   🥁 Metronome       │
│                                        │
│  30-80% Reduction                      │
│  Research-Backed                       │
└────────────────────────────────────────┘
```

Upload at: Settings → Social preview

---

## 🤖 Enable GitHub Actions (Optional)

Create `.github/workflows/tests.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: windows-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: python tests/test_audio.py
```

---

## 📣 Promotion

### After Upload

1. **GitHub Discussions**
   - Create "Welcome" thread
   - Pin "How to Get Started"

2. **Reddit**
   - r/stutter
   - r/Python
   - r/opensource

3. **Communities**
   - Speech pathology forums
   - Stuttering support groups
   - Research communities

4. **Social Media**
   - Tweet about release
   - LinkedIn post (if applicable)

---

## 🔄 Ongoing Maintenance

### Regular Tasks

- [ ] Respond to issues (within 48h)
- [ ] Review pull requests (within 1 week)
- [ ] Update documentation as needed
- [ ] Release updates (follow semantic versioning)
- [ ] Keep dependencies updated
- [ ] Monitor security alerts

### Versioning

Follow [Semantic Versioning](https://semver.org/):
- **Major** (2.0.0): Breaking changes
- **Minor** (1.1.0): New features (backward compatible)
- **Patch** (1.0.1): Bug fixes

---

## ✅ Post-Upload Checklist

- [ ] Repository is public
- [ ] README renders correctly
- [ ] All links work
- [ ] Issues are enabled
- [ ] First release is published
- [ ] Topics/tags are added
- [ ] License is visible
- [ ] Contributing guide is accessible
- [ ] Code of Conduct is in place
- [ ] Security policy is defined

---

## 🎉 You're Ready!

Your AntiStutter repository is now professionally set up for open source development!

Next: Share it with the world! 🌍
