# 🐦 Panduan Mendapatkan Twitter Token untuk StarLabs 0G

## 🚨 **MASALAH YANG TERIDENTIFIKASI**

Twitter token Anda saat ini tidak valid atau tidak lengkap:

```
1835257202581651456-qdGpqIahTY9kyCv2Z2Thp8gNMCBMPe
```

## 📋 **CARA MENDAPATKAN TWITTER TOKEN YANG VALID**

### **Metode 1: Menggunakan Browser Developer Tools**

1. **Buka Twitter/X di browser** dan login ke akun Anda
2. **Tekan F12** untuk membuka Developer Tools
3. **Pergi ke tab Network**
4. **Refresh halaman** (Ctrl+R atau F5)
5. **Cari request yang mengandung "auth_token"** di cookies
6. **Copy nilai auth_token** yang lengkap

### **Metode 2: Menggunakan Browser Cookies**

1. **Login ke Twitter/X**
2. **Buka Developer Tools** (F12)
3. **Pergi ke tab Application/Storage**
4. **Pilih Cookies → https://x.com**
5. **Cari cookie bernama "auth_token"**
6. **Copy nilai lengkapnya**

### **Metode 3: Menggunakan Extension Browser**

1. **Install extension "Cookie Editor"** atau sejenisnya
2. **Login ke Twitter/X**
3. **Buka extension dan cari "auth_token"**
4. **Copy nilai lengkapnya**

## ✅ **FORMAT TOKEN YANG BENAR**

Token Twitter yang valid biasanya terlihat seperti ini:

```
1234567890123456789-AbCdEfGhIjKlMnOpQrStUvWxYz1234567890AbCdEf
```

**Karakteristik token yang valid:**

- Panjang sekitar 50-70 karakter
- Dimulai dengan angka panjang (user ID)
- Diikuti tanda "-"
- Diikuti string alfanumerik panjang

## 🔧 **CARA UPDATE TOKEN**

1. **Edit file `data/twitter_tokens.txt`**
2. **Ganti token lama dengan token baru**
3. **Simpan file**
4. **Jalankan aplikasi lagi**

## 🚨 **TROUBLESHOOTING**

### **Jika masih error "invalid token":**

1. Pastikan Anda login ke Twitter/X
2. Pastikan token di-copy lengkap tanpa spasi
3. Coba logout dan login ulang ke Twitter
4. Dapatkan token baru

### **Jika mendapat "HTML response":**

- Token sudah expired atau tidak valid
- Perlu mendapatkan token baru

## 📝 **CONTOH TOKEN YANG BENAR**

```
# File: data/twitter_tokens.txt
1835257202581651456-qdGpqIahTY9kyCv2Z2Thp8gNMCBMPeXYZ123456789AbCdEf
```

## ⚠️ **KEAMANAN**

- **JANGAN SHARE** token Twitter Anda
- Token ini memberikan akses ke akun Twitter Anda
- Ganti token secara berkala untuk keamanan

---

**Setelah mendapatkan token yang valid, aplikasi akan berjalan dengan lancar!**
