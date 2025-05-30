# 🚀 StarLabs-MegaETH Task Configuration Guide

## 📋 Daftar Task yang Tersedia

### 🎯 **FULL_MEGAETH_AUTOMATION** (Default)

Task komprehensif yang mencakup semua aktivitas MegaETH testnet dalam urutan optimal:

**Fase 1: Setup & Funding**

- `crusty_refuel` - Refuel MEGAETH tokens
- `cex_withdrawal` - Withdraw dari exchange (opsional)

**Fase 2: Faucet & Token Acquisition**

- `faucet` - Dapatkan MEGAETH tokens (perlu captcha)
- `teko_faucet` - Token tambahan dari Teko

**Fase 3: DeFi & Staking**

- `teko_finance` - Stake tokens di Teko Finance
- `cap_app` - Mint cUSD tokens

**Fase 4: Trading & Swapping**

- `bebop` + `gte_swaps` - Trading di kedua platform (random order)

**Fase 5: NFT & Minting**

- `onchain_gm` + `omnihub` + `rarible` - Mint NFT dari berbagai platform
- `conft_app` - Mint NFT dan domain (biaya 0.0013 ETH)

**Fase 6: Meme Token Trading**

- `xl_meme` atau `rainmakr` - Beli meme tokens (pilihan random)

**Fase 7: Contract Deployment**

- `mintair` + `easynode` + `zkcodex` - Deploy berbagai kontrak
- `owlto` - Deploy basic contract

**Fase 8: Platform Khusus**

- `nerzo_megaeth` - Mint di Nerzo MegaETH
- `morkie_mega` - Mint di Morkie
- `nerzo_fluffle` - Mint Fluffle tokens

**Fase 9: Quest & Campaign**

- `superboard` - Complete quests
- `hopnetwork` - Join waitlist

---

## 🎮 Task Alternatif Berdasarkan Fokus

### 🌱 **BASIC_STARTER** (Untuk Pemula)

```python
TASKS = ["BASIC_STARTER"]
```

- Aktivitas dasar dengan risiko rendah
- Cocok untuk wallet baru atau testing

### 💹 **TRADING_FOCUSED** (Fokus Trading)

```python
TASKS = ["TRADING_FOCUSED"]
```

- Fokus pada aktivitas trading dan swap
- Maksimalkan volume trading

### 🖼️ **NFT_FOCUSED** (Fokus NFT)

```python
TASKS = ["NFT_FOCUSED"]
```

- Fokus pada minting NFT dari berbagai platform
- Cocok untuk collectors

### 🏦 **DEFI_FOCUSED** (Fokus DeFi)

```python
TASKS = ["DEFI_FOCUSED"]
```

- Fokus pada staking dan DeFi activities
- Maksimalkan yield farming

### ⚙️ **DEPLOYMENT_FOCUSED** (Fokus Contract)

```python
TASKS = ["DEPLOYMENT_FOCUSED"]
```

- Fokus pada deployment kontrak
- Cocok untuk developers

### 🛡️ **CONSERVATIVE** (Konservatif)

```python
TASKS = ["CONSERVATIVE"]
```

- Risiko rendah, biaya minimal
- Aktivitas gratis atau murah

### 🔥 **AGGRESSIVE** (Agresif)

```python
TASKS = ["AGGRESSIVE"]
```

- Aktivitas maksimal untuk rewards tinggi
- Biaya lebih tinggi tapi potensi reward besar

---

## 🔧 Cara Menggunakan

### 1. Edit File tasks.py

Ganti nilai `TASKS` dengan task yang diinginkan:

```python
# Untuk full automation
TASKS = ["FULL_MEGAETH_AUTOMATION"]

# Untuk pemula
TASKS = ["BASIC_STARTER"]

# Untuk trading focus
TASKS = ["TRADING_FOCUSED"]

# Atau kombinasi multiple tasks
TASKS = ["BASIC_STARTER", "TRADING_FOCUSED"]
```

### 2. Custom Task

Anda juga bisa membuat task custom:

```python
TASKS = ["MY_CUSTOM_TASK"]

MY_CUSTOM_TASK = [
    "crusty_refuel",
    "faucet",
    ("bebop", "gte_swaps"),  # Kedua akan dijalankan random order
    ["xl_meme", "rainmakr"], # Hanya satu yang dipilih random
    "onchain_gm",
]
```

---

## 📊 Detail Setiap Modul

| Modul           | Platform     | Biaya      | Deskripsi                     |
| --------------- | ------------ | ---------- | ----------------------------- |
| `crusty_refuel` | CrustySwap   | Gas fee    | Refuel MEGAETH tokens         |
| `faucet`        | MegaETH      | Gratis     | Faucet tokens (perlu captcha) |
| `teko_faucet`   | Teko         | Gratis     | Faucet dari Teko              |
| `cap_app`       | Cap.app      | Gas fee    | Mint cUSD                     |
| `bebop`         | Bebop        | Gas fee    | Trading tokens                |
| `gte_swaps`     | GTE          | Gas fee    | Trading tokens                |
| `teko_finance`  | Teko Finance | Gas fee    | Staking                       |
| `onchain_gm`    | OnChain GM   | Gas fee    | Mint GM NFT                   |
| `xl_meme`       | XL Meme      | ETH + Gas  | Buy meme tokens               |
| `omnihub`       | OmniHub      | ETH + Gas  | Mint NFT                      |
| `mintair`       | Mintair      | Gas fee    | Deploy timer contract         |
| `easynode`      | EasyNode     | Gas fee    | Deploy counter contract       |
| `hopnetwork`    | Hop Network  | Gratis     | Join waitlist                 |
| `owlto`         | Owlto        | Gas fee    | Deploy basic contract         |
| `rainmakr`      | Rainmakr     | ETH + Gas  | Buy meme token                |
| `rarible`       | Rarible      | Gas fee    | Mint NFT                      |
| `superboard`    | Superboard   | Varies     | Complete quests               |
| `conft_app`     | Conft        | 0.0013 ETH | Mint NFT & domain             |
| `zkcodex`       | ZKCodex      | Gas fee    | Deploy contracts              |
| `nerzo_megaeth` | Nerzo        | Gas fee    | Mint MegaETH                  |
| `morkie_mega`   | Morkie       | Gas fee    | Mint Mega                     |
| `nerzo_fluffle` | Nerzo        | Gas fee    | Mint Fluffle                  |

---

## ⚠️ Penting untuk Diingat

1. **Captcha**: Modul `faucet` memerlukan captcha solver (Solvium/Capsolver)
2. **Biaya**: Beberapa modul memerlukan ETH untuk mint/buy
3. **Proxy**: Disarankan menggunakan proxy untuk keamanan
4. **Balance**: Pastikan wallet memiliki ETH yang cukup
5. **Config**: Sesuaikan `config.yaml` sebelum menjalankan

---

## 🚀 Rekomendasi Penggunaan

### Untuk Pemula:

1. Mulai dengan `BASIC_STARTER`
2. Pastikan setup proxy dan captcha solver
3. Test dengan 1-2 wallet dulu

### Untuk Advanced:

1. Gunakan `FULL_MEGAETH_AUTOMATION` atau `AGGRESSIVE`
2. Setup multiple proxy
3. Gunakan range wallet yang lebih besar

### Untuk Specific Goals:

- **Airdrop Hunter**: `FULL_MEGAETH_AUTOMATION`
- **NFT Collector**: `NFT_FOCUSED`
- **DeFi Farmer**: `DEFI_FOCUSED`
- **Developer**: `DEPLOYMENT_FOCUSED`

---

## 📞 Support

Jika ada pertanyaan atau masalah:

- Baca dokumentasi di README.md
- Check konfigurasi di config.yaml
- Pastikan semua dependencies terinstall
- Gunakan proxy yang stabil
