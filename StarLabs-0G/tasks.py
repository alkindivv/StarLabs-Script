# 🚀 StarLabs 0G - Contoh Konfigurasi Task Optimal
# Copy salah satu konfigurasi di bawah ke file tasks.py

# ========================================
# 🔰 PEMULA - Task Dasar dan Aman
# ========================================

# Konfigurasi untuk pemula - fokus pada faucet dan deploy sederhana
TASKS_BEGINNER = ["BASIC_FARMING"]

BASIC_FARMING = [
    "faucet",                    # Dapatkan token A0GI
    "faucet_tokens",            # Dapatkan ETH/BTC/USDT
    "storagescan_deploy",       # Deploy kontrak sederhana
]

# ========================================
# 🚀 INTERMEDIATE - Task Menengah
# ========================================

# Konfigurasi untuk user menengah - tambah NFT dan swap
TASKS_INTERMEDIATE = ["MEDIUM_FARMING"]

MEDIUM_FARMING = [
    "faucet",                           # Faucet token
    ("faucet_tokens", "storagescan_deploy"),  # Jalankan keduanya secara acak
    ["conft_mint", "omnihub"],         # Pilih salah satu NFT mint
    "zero_exchange_swaps",             # Swap token
]

# ========================================
# 💎 ADVANCED - Task Lengkap dan Optimal
# ========================================

# Konfigurasi untuk user advanced - semua fitur dengan optimasi
TASKS = ["FULL_FARMING"]

FULL_FARMING = [
    # Phase 1: Setup dan Faucet
    # "faucet",
    "faucet_tokens",

    # Phase 2: Deploy Contracts (acak)
    # ("storagescan_deploy", "mintair_deploy", "easynode_deploy"),

    # Phase 3: NFT Minting (pilih 1-2 secara acak)
    ["conft_mint", "omnihub", "morkie_og_mint"],
    ["mintaura_pandriel_mint", "omnihub"],

    # Phase 4: Trading
    "zero_exchange_swaps",
]

# ========================================
# 🌉 BRIDGE FOCUSED - Fokus Bridge dan Refuel
# ========================================

TASKS_BRIDGE = ["BRIDGE_FARMING"]

BRIDGE_FARMING = [
    "crusty_refuel",               # Refuel dari network lain
    "faucet_tokens",              # Dapatkan token untuk swap
    "zero_exchange_swaps",        # Swap untuk volume
    ["storagescan_deploy", "mintair_deploy"],  # Deploy kontrak
]

# ========================================
# 🎨 NFT FOCUSED - Fokus NFT Minting
# ========================================

TASKS_NFT = ["NFT_FARMING"]

NFT_FARMING = [
    "faucet",                     # Dapatkan token untuk gas
    "faucet_tokens",             # Dapatkan ETH

    # Mint semua NFT yang tersedia
    "conft_mint",
    "omnihub",
    "morkie_og_mint",
    "mintaura_pandriel_mint",

    # Deploy untuk aktivitas tambahan
    ["storagescan_deploy", "easynode_deploy"],
]

# ========================================
# 💰 PROFIT FOCUSED - Fokus Trading dan Volume
# ========================================

TASKS_PROFIT = ["PROFIT_FARMING"]

PROFIT_FARMING = [
    "faucet_tokens",                    # Dapatkan token untuk trading
    "zero_exchange_swaps",             # Swap untuk volume
    "zero_exchange_swaps",             # Swap lagi untuk lebih banyak volume
    ("storagescan_deploy", "conft_mint"),  # Aktivitas tambahan
]

# ========================================
# 🔄 DAILY ROUTINE - Rutinitas Harian
# ========================================

TASKS_DAILY = ["DAILY_ROUTINE"]

DAILY_ROUTINE = [
    "faucet",                          # Faucet harian
    ["zero_exchange_swaps", "conft_mint"],  # Aktivitas acak
    ["storagescan_deploy", "omnihub"],      # Deploy atau mint
]

# ========================================
# 🎯 SPECIFIC TASKS - Task Spesifik
# ========================================

# Hanya Faucet
FAUCET_ONLY = ["faucet"]
# FAUCET_ONLY = ["faucet", "faucet_tokens"]

# Hanya Deploy
DEPLOY_ONLY = ["storagescan_deploy", "mintair_deploy", "easynode_deploy"]

# Hanya NFT
NFT_ONLY = ["conft_mint", "omnihub", "morkie_og_mint", "mintaura_pandriel_mint"]

# Hanya Swap
SWAP_ONLY = ["zero_exchange_swaps"]

# Hanya Bridge
BRIDGE_ONLY = ["crusty_refuel"]

# ========================================
# 🔧 CUSTOM TASK BUILDER
# ========================================

# Template untuk membuat task custom
CUSTOM_TASK_TEMPLATE = [
    # 1. Pilih faucet (opsional)
    # "faucet",
    # "faucet_tokens",

    # 2. Pilih deploy (gunakan () untuk semua, [] untuk acak)
    # ("storagescan_deploy", "mintair_deploy"),
    # ["storagescan_deploy", "easynode_deploy"],

    # 3. Pilih NFT minting
    # "conft_mint",
    # ["omnihub", "morkie_og_mint"],

    # 4. Pilih trading
    # "zero_exchange_swaps",

    # 5. Pilih bridge (jika diperlukan)
    # "crusty_refuel",
]

# ========================================
# 📊 TASK RECOMMENDATIONS BERDASARKAN GOAL
# ========================================

"""
🎯 PILIH BERDASARKAN TUJUAN:

1. 🔰 PEMULA (Belajar dan Aman):
   TASKS = ["BASIC_FARMING"]

2. 💰 MAKSIMAL PROFIT:
   TASKS = ["PROFIT_FARMING"]

3. 🎨 KOLEKSI NFT:
   TASKS = ["NFT_FARMING"]

4. 🌉 BRIDGE ACTIVITY:
   TASKS = ["BRIDGE_FARMING"]

5. 🔄 RUTINITAS HARIAN:
   TASKS = ["DAILY_ROUTINE"]

6. 💎 SEMUA FITUR:
   TASKS = ["FULL_FARMING"]

7. 🎯 SPESIFIK:
   TASKS = ["FAUCET_ONLY"]  # atau yang lain

8. 🔧 CUSTOM:
   Buat sendiri menggunakan CUSTOM_TASK_TEMPLATE
"""

# ========================================
# ⚡ QUICK START CONFIGURATIONS
# ========================================

# Untuk testing cepat (1-2 task saja)
QUICK_TEST = ["faucet"]

# Untuk farming harian ringan
LIGHT_FARMING = ["faucet", "storagescan_deploy"]

# Untuk farming intensif
INTENSIVE_FARMING = [
    "faucet",
    "faucet_tokens",
    ("storagescan_deploy", "mintair_deploy"),
    ["conft_mint", "omnihub"],
    "zero_exchange_swaps",
    "zero_exchange_swaps",  # Double swap untuk volume
]

# ========================================
# 📝 CARA PENGGUNAAN:
# ========================================
"""
1. Pilih salah satu konfigurasi di atas
2. Copy ke file tasks.py
3. Ganti nama variabel menjadi TASKS
4. Jalankan bot

Contoh:
TASKS = ["FULL_FARMING"]  # Ganti dengan pilihan Anda

FULL_FARMING = [
    "faucet",
    "storagescan_deploy",
    "conft_mint",
]
"""

# ========================================
# ⚠️ TIPS OPTIMASI:
# ========================================
"""
1. 🔄 Gunakan () untuk menjalankan semua task dalam grup
2. 🎲 Gunakan [] untuk memilih 1 task secara acak dari grup
3. ⏱️ Atur delay di config.yaml untuk menghindari rate limit
4. 🔒 Gunakan proxy untuk keamanan
5. 📊 Monitor logs untuk tracking progress
6. 💾 Backup konfigurasi sebelum mengubah
7. 🧪 Test dengan 1-2 akun dulu sebelum full farming
"""