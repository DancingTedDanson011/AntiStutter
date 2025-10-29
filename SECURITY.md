# Security Policy

## 🔒 Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## 🐛 Reporting a Vulnerability

If you discover a security vulnerability in AntiStutter, please follow these steps:

### 1. DO NOT Create a Public Issue

Security vulnerabilities should be reported privately to protect users.

### 2. Report via Private Channel

- **Email**: your-security-email@example.com
- **Subject**: "[SECURITY] Brief description"

### 3. Include in Your Report

- **Type of vulnerability**
- **Affected component(s)**
- **Steps to reproduce**
- **Potential impact**
- **Suggested fix** (if you have one)

### 4. What to Expect

- **Acknowledgment**: Within 48 hours
- **Assessment**: Within 1 week
- **Fix**: Depends on severity
  - Critical: 24-48 hours
  - High: 1 week
  - Medium: 2 weeks
  - Low: Next release

### 5. Disclosure Policy

- We will work with you to understand and resolve the issue
- We will credit you (unless you prefer anonymity)
- We will disclose the issue publicly after a fix is released
- Coordinated disclosure: typically 90 days

## 🛡️ Security Considerations

### Audio Processing

- **Low Volume**: Start with low volume settings
- **Headphones Only**: Never use speakers (feedback risk)
- **Monitoring**: Discontinue if experiencing discomfort

### Data Privacy

- **Local Processing**: All audio processing happens locally
- **No Internet**: AntiStutter doesn't send data online
- **Config Files**: Stored locally in `%USERPROFILE%\.antistutter\`
- **Logs**: May contain system info, but no audio data

### Dependencies

We use well-maintained open-source libraries:

- numpy, scipy (numerical computing)
- sounddevice, soundfile (audio I/O)
- librosa (audio DSP)
- PyQt5 (GUI)

All dependencies are from PyPI and verified.

## 🔐 Best Practices for Users

1. **Download from Official Sources**
   - GitHub repository
   - Official releases only

2. **Verify Installation**
   ```bash
   # Check dependencies
   pip list

   # Run tests
   python tests/test_audio.py
   ```

3. **Review Permissions**
   - AntiStutter needs: Microphone, Audio Output
   - Does NOT need: Network, Filesystem (beyond config)

4. **Keep Updated**
   - Check for updates regularly
   - Read CHANGELOG.md for security fixes

## 🚨 Known Security Considerations

### 1. Audio Feedback Loop

**Risk**: Using speakers instead of headphones can create loud feedback

**Mitigation**:
- GUI warning displayed
- Documentation emphasizes headphones requirement
- Consider adding speaker detection (future)

### 2. System Audio Access

**Risk**: Application has access to system audio

**Mitigation**:
- Open source - code is auditable
- No network access
- Local processing only

### 3. Configuration Files

**Risk**: Config files could be modified by malware

**Mitigation**:
- Config files in user directory (sandboxed)
- JSON format (human readable, no code execution)
- Validation on load

## 🔍 Security Audits

- No formal security audits yet (volunteer project)
- Code reviews by maintainers
- Community code review welcome
- Static analysis: flake8, mypy

## 📞 Contact

For security concerns:
- **Email**: your-security-email@example.com
- **GPG Key**: [Optional: Add GPG key for encrypted communication]

For general issues:
- **GitHub Issues**: https://github.com/DancingTedDanson011/antistutter/issues

---

**Thank you for helping keep AntiStutter secure!** 🔒
