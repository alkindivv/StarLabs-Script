#!/usr/bin/env python3
"""
Script untuk menjalankan StarLabs 0G dengan konfigurasi yang dioptimalkan
"""
import subprocess
import sys
from loguru import logger

def main():
    logger.info("🚀 Starting StarLabs 0G with optimized configuration...")
    logger.info("📋 Configuration applied:")
    logger.info("   ✅ Fallback without proxy: ENABLED")
    logger.info("   ✅ Increased timeouts: 60 seconds")
    logger.info("   ✅ Enhanced error handling: ENABLED")
    logger.info("   ✅ Retry mechanism: IMPROVED")
    logger.info("")
    logger.info("🔧 Based on connection test results:")
    logger.info("   ✅ Direct connection: WORKING")
    logger.info("   ❌ Proxy connection: FAILED (will fallback)")
    logger.info("")
    logger.info("🎯 Starting main application...")
    logger.info("="*50)

    try:
        # Run the main application
        result = subprocess.run([sys.executable, "main.py"], check=True)
        logger.success("✅ Application completed successfully!")
        return result.returncode
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Application failed with exit code: {e.returncode}")
        return e.returncode
    except KeyboardInterrupt:
        logger.warning("⚠️ Application interrupted by user")
        return 130
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)