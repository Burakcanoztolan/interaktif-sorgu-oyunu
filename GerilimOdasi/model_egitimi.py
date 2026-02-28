import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

# 1. EĞİTİM VERİ SETİ (Dataset)
# X: Oyuncunun sorabileceği olası cümleler (Özellikler)
# y: Bu cümlelerin ait olduğu kategoriler (Etiketler)

X_train = [
    # cinayet_ani kategorisi
    "O saatte tam olarak neredeydin?",
    "Sesleri nasıl duymadın?",
    "Kulaklık takıyordum deme bana.",
    "Cinayet işlenirken ne yapıyordun?",
    "Zamanı söyle bana, saat kaçtı?",
    "Olay anında stüdyoda mıydın?",

    # cinayet_silahi kategorisi
    "Kafasına neyle vurdun?",
    "Metronomu sen mi aldın?",
    "Silah nerede?",
    "Piyanonun üstündeki kan izleri ne?",
    "Parmak izini bulduk.",
    "Cinayet aletini nereye sakladın?",

    # kurbanla_iliski kategorisi
    "Aranız nasıldı?",
    "Neden kavga ettiniz?",
    "Telif hakları yüzünden mi tartışıyordunuz?",
    "Onu kıskanıyordun değil mi?",
    "Aranızdaki husumet ne zamandır var?",
    "Gruptan seni atacak mıydı?",

    # anlasilmadi kategorisi (Alakasız kelimeler veya sadece agresif çıkışlar)
    "Seni hapse attıracağım!",
    "Polisi arıyorum.",
    "Avukatımı istiyorum.",
    "Saçmalamayı kes.",
    "Yalan söylüyorsun!",
    "İtiraf et artık."
]

y_train = [
    "cinayet_ani", "cinayet_ani", "cinayet_ani", "cinayet_ani", "cinayet_ani", "cinayet_ani",
    "cinayet_silahi", "cinayet_silahi", "cinayet_silahi", "cinayet_silahi", "cinayet_silahi", "cinayet_silahi",
    "kurbanla_iliski", "kurbanla_iliski", "kurbanla_iliski", "kurbanla_iliski", "kurbanla_iliski", "kurbanla_iliski",
    "anlasilmadi", "anlasilmadi", "anlasilmadi", "anlasilmadi", "anlasilmadi", "anlasilmadi"
]

# 2. VEKTÖRİZASYON (Kelimeleri Matematiksel Matrislere Çevirme)
# Cümleleri modelin anlayabileceği sayılara dönüştürüyoruz
vectorizer = TfidfVectorizer()
X_train_vektor = vectorizer.fit_transform(X_train)

# 3. MODELİ EĞİTME
# Metin sınıflandırmada çok başarılı olan Support Vector Machine (SVM) algoritmasını kullanıyoruz
model = LinearSVC()
model.fit(X_train_vektor, y_train)

# 4. KAYDETME (Export)
# Eğittiğimiz modeli ve vektörizeri daha sonra oyunumuzda kullanmak üzere paketliyoruz
joblib.dump(model, 'intent_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Makine Öğrenmesi Modeli başarıyla eğitildi ve paketlendi!")