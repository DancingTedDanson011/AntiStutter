"""
AntiStutter - Main Entry Point
Scientifically-based stuttering reduction through auditory stimulation

Based on research:
- Delayed Auditory Feedback (DAF): 30-70% reduction
- Frequency Altered Feedback (FAF): 30-60% reduction
- Rhythmic Stimulation: Up to 100% reduction
- Binaural Beats: ~25% reduction

Version: 1.0.0
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from gui.main_window import MainWindow
from utils.logger import logger
from utils.config import config


def main():
    """Main application entry point"""
    logger.info("=" * 60)
    logger.info("AntiStutter v1.0 starting...")
    logger.info("=" * 60)

    # Create Qt application
    app = QApplication(sys.argv)
    app.setApplicationName("AntiStutter")
    app.setOrganizationName("AntiStutter")

    # Enable high DPI scaling
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    # Apply dark theme (optional)
    app.setStyle("Fusion")

    # Create and show main window
    try:
        window = MainWindow()
        window.show()

        logger.info("Application started successfully")
        logger.info(f"Config directory: {config.config_dir}")

        # Run application
        exit_code = app.exec_()

        logger.info("Application exiting...")
        return exit_code

    except Exception as e:
        logger.critical(f"Fatal error: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
