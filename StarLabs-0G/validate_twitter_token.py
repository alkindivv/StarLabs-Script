#!/usr/bin/env python3
"""
Script untuk memvalidasi Twitter token sebelum menjalankan aplikasi utama
"""
import asyncio
from noble_tls import Session, Client
import secrets
from loguru import logger

async def validate_twitter_token(auth_token: str) -> bool:
    """Validate Twitter token by making a test request"""
    try:
        logger.info("🔍 Validating Twitter token...")

        # Create Twitter client
        session = Session(client=Client.CHROME_131)
        session.random_tls_extension_order = True
        session.timeout_seconds = 30

        generated_csrf_token = secrets.token_hex(16)

        cookies = {"ct0": generated_csrf_token, "auth_token": auth_token}
        headers = {"x-csrf-token": generated_csrf_token}

        session.headers.update(headers)
        session.cookies.update(cookies)

        # Test request to Twitter API
        headers = {
            "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
            "referer": "https://x.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "x-csrf-token": generated_csrf_token,
            "x-twitter-auth-type": "OAuth2Session",
            "x-twitter-active-user": "yes",
            "x-twitter-client-language": "en",
        }

        session.headers.update(headers)

        # Make a simple request to verify token
        response = await session.get("https://api.x.com/1.1/account/verify_credentials.json")

        if response.status_code == 200:
            logger.success("✅ Twitter token is valid!")
            return True
        elif response.status_code == 401:
            logger.error("❌ Twitter token is invalid or expired")
            return False
        else:
            logger.warning(f"⚠️ Unexpected response: {response.status_code}")
            return False

    except Exception as e:
        logger.error(f"❌ Error validating token: {e}")
        return False

def check_token_format(token: str) -> bool:
    """Check if token has the correct format"""
    if not token or len(token.strip()) < 20:
        logger.error("❌ Token is too short")
        return False

    # Support both old format (with user ID) and new format (hex string)
    if "-" in token:
        # Old format: 1234567890123456789-AbCdEfGhIjKlMnOpQrStUvWxYz1234567890AbCdEf
        parts = token.split("-")
        if len(parts) != 2:
            logger.error("❌ Token should have exactly one '-' separator")
            return False

        user_id, token_part = parts

        if not user_id.isdigit():
            logger.error("❌ First part should be numeric user ID")
            return False

        if len(token_part) < 20:
            logger.error("❌ Token part is too short")
            return False
    else:
        # New format: hex string (like 6e1f2a66d3daabceeb205e1f3cd523cdd84ae7e8)
        if len(token) < 30:
            logger.error("❌ Token is too short for new format")
            return False

        # Check if it's a valid hex string
        try:
            int(token, 16)
        except ValueError:
            logger.error("❌ Token should be a valid hexadecimal string")
            return False

    logger.success("✅ Token format looks correct")
    return True

async def main():
    """Main validation function"""
    logger.info("🐦 Twitter Token Validator")
    logger.info("="*50)

    try:
        # Read token from file
        with open("data/twitter_tokens.txt", "r", encoding="utf-8") as f:
            token = f.read().strip()

        logger.info(f"📋 Token found: {token[:20]}...{token[-10:]}")

        # Check format first
        if not check_token_format(token):
            logger.error("❌ Token format is invalid")
            logger.info("📖 Please check TWITTER_TOKEN_GUIDE.md for instructions")
            return False

        # Validate with Twitter API
        is_valid = await validate_twitter_token(token)

        if is_valid:
            logger.success("🎉 Token validation successful!")
            logger.info("✅ You can now run the main application")
            return True
        else:
            logger.error("❌ Token validation failed")
            logger.info("📖 Please check TWITTER_TOKEN_GUIDE.md for instructions")
            return False

    except FileNotFoundError:
        logger.error("❌ File data/twitter_tokens.txt not found")
        return False
    except Exception as e:
        logger.error(f"❌ Error reading token file: {e}")
        return False

if __name__ == "__main__":
    result = asyncio.run(main())
    if not result:
        exit(1)