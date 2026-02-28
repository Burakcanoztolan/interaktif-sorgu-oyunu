# 🕵️‍♂️ Gerilim Odası (Thriller Room): NLP Destekli İnteraktif Sorgu Simülasyonu

**Gerilim Odası**, oyuncunun bir cinayet şüphelisini serbest metin (doğal dil) kullanarak sorguladığı ve yapay zeka destekli bir psikolojik gerilim simülasyonudur. Klasik çoktan seçmeli oyunların aksine, sistem oyuncunun girdiği cümleleri analiz eder, şüphelinin stres seviyesini dinamik olarak hesaplar ve mantıksal çelişkileri yakalayarak oyunu yönlendirir.

## 💡 Projenin Amacı ve Vizyonu
Bu proje, makine öğrenmesi algoritmalarının ve doğal dil işleme (NLP) tekniklerinin, durum makineleri (state machines) ile nasıl entegre edilebileceğini göstermek amacıyla geliştirilmiştir. Kullanıcı deneyimini merkeze alan, öngörülemez ve dinamik bir sorgu ortamı yaratmak hedeflenmiştir.

## ⚙️ Sistem Mimarisi ve Kullanılan Teknolojiler

Proje, temel olarak üç ana mühendislik bloğundan oluşmaktadır:

### 1. Makine Öğrenmesi ile Niyet Sınıflandırma (Intent Classification)
* Oyuncunun girdiği serbest metinler, **TF-IDF (Term Frequency-Inverse Document Frequency)** yöntemiyle vektörize edilerek sayısal matrislere dönüştürülür.
* Eğitilmiş bir **Support Vector Machine (LinearSVC)** modeli, bu vektörleri analiz ederek oyuncunun sorusunun hangi kategoriye (cinayet anı, silah, ilişkiler vb.) ait olduğunu yüksek bir doğrulukla tahmin eder.

### 2. Kural Tabanlı Stres ve Duygu Analizi
* Girdi metnindeki suçlayıcı ve agresif kelimelerin (örn: "katil", "kanıt", "polis") ağırlığı hesaplanarak, şüphelinin "Panik Seviyesi" (0, 1, 2) dinamik olarak artırılır. Şüpheli köşeye sıkıştıkça verdiği cevapların uzunluğu ve agresifliği değişir.

### 3. Hafıza ve Çelişki Yakalama Algoritması (State Management)
* Sistem, her soru kategorisini ve o sorunun sorulduğu andaki panik seviyesini geçici bir hafızada (Dictionary) tutar. 
* Eğer oyuncu, şüphelinin panik seviyesi düşükken sorduğu bir konuyu, panik seviyesi zirvedeyken tekrar sorarsa sistem mantıksal bir çelişki yakalar. Şüphelinin eski ifadesini unuttuğunu tespit edip "İtiraf Döngüsü"nü tetikleyerek oyunu sonlandırır.

## 🛠️ Teknoloji Yığını (Tech Stack)
* **Dil:** Python
* **Makine Öğrenmesi & NLP:** Scikit-Learn (`LinearSVC`, `TfidfVectorizer`), `joblib`
* **Veri Yönetimi:** JSON (Karakter zihin haritası ve diyalog ağaçları için)
* **Kullanıcı Arayüzü (UI) & Deployment:** Streamlit, Streamlit Community Cloud

## 💻 Nasıl Çalıştırılır?
Projeyi lokal bilgisayarınızda test etmek için aşağıdaki adımları izleyebilirsiniz:

**1. Repoyu bilgisayarınıza klonlayın:**
   ```bash
   git clone [https://github.com/Burakcanoztolan/interaktif-sorgu-oyunu.git](https://github.com/Burakcanoztolan/interaktif-sorgu-oyunu.git)
```
**2. Gerekli kütüphaneleri kurun:**

```Bash

pip install -r requirements.txt
```
**3. Streamlit arayüzünü başlatın:**

```Bash

streamlit run main.py
```
