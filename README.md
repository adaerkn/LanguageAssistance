### **Dil Asistanı Uygulaması**

Yapay zeka destekli dil asistanı uygulamamız, **Pupilica Yapay Zeka Hackathon**'u için  Filiz **Buzkıran** (@lizlavigne) , **Göknil Bilge** (@GoknilBilge) ve **Ada Erkan** (@adaerkn) tarafından geliştirilmiştir. 

Bu uygulama, dil öğrenimini interaktif ve eğlenceli hale getiren bir Streamlit arayüzüdür. Kullanıcıların İngilizce kelime bilgisini geliştirmesine ve yazdıkları cümlelerdeki dil bilgisi ve yazım hatalarını kontrol etmesine yardımcı olur.


### **Uygulamayı Canlı Deneyin!**

Uygulamayı indirmeden doğrudan tarayıcınızda denemek için aşağıdaki bağlantıyı ziyaret edebilirsiniz:

👉 **[Uygulamaya Gitmek İçin Tıklayın](https://languageassistance.streamlit.app/)**


### **Ana Özellikler**

* **Günlük Kelime Pratiği:** Rastgele seçilen bir kelime ve anlamı ile kullanıcıya örnek cümleler sunar.
* **Akıllı Cümle Kontrolü:** Kullanıcının yazdığı cümledeki yazım ve dil bilgisi hatalarını akıllı bir yapay zeka modeliyle (Hugging Face `prithivida/grammar_error_correcter_v1`) düzeltir.
* **Ayrıntılı Düzeltme Raporu:** Düzeltilen cümledeki hataları ayrıntılı olarak gösterir.
* **Mini Quiz:** Öğrenilen kelimenin anlam testini sunar.
* **Profil Yönetimi:** Kullanıcılar dil, seviye ve hedeflerini kaydedebilir.

---

### **Kurulum ve Kullanım**

Uygulamayı yerel bilgisayarınızda kurmak ve çalıştırmak için aşağıdaki adımları sırasıyla izleyin.

#### **1. Depoyu Klonlayın**

Uygulamanın tüm dosyalarını bilgisayarınıza indirmek için terminalinizde aşağıdaki komutu çalıştırın:

```bash
git clone [https://github.com/adaerkn/Language_Assistance.git](https://github.com/adaerkn/Language_Assistance.git)
```
#### **2. Proje Klasörüne Gidin**

```bash
cd Language_Assistance
```
#### **3. Gerekli Kütüphane kurulumu**
Bu uygulamamızın ihtiyacı olan kütüphaneleri yüklenilen requirements.txt dosyamızdan kütüphaneleri otomatik olarak indirecektir.

```bash
pip install -r requirements.txt
```

#### **4. Uygulamayı Başlatın**
Streamlit arayüzü ile birleştirdiğimiz uygulamamız bu komut yarıdımıyla açılacaktır. 

```bash
streamlit run arayuz.py
```





