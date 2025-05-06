import streamlit as st

st.title("TCK 32 Rapor Oluşturucu")

kurum = st.text_input("Kurumu")
ust_yazi_tarihi = st.date_input("Üst Yazı Tarihi")
ust_yazi_sayisi = st.text_input("Üst Yazı Sayısı")
suc_tarihi = st.date_input("Suç Tarihi")
tc_kimlik_no = st.text_input("TC Kimlik No")
ad_soyad = st.text_input("Ad Soyad")
muayene_tarihi = st.date_input("Muayene Tarihi")
anamnez = st.text_area("Anamnez")
tani = st.text_input("Tanı")
ehliyet_durumu = st.selectbox("Ceza Ehliyeti Durumu", ["tam", "sınırlı"])

if ehliyet_durumu == "sınırlı":
    algilama = st.text_input("Algılama Durumu")
    davranis = st.text_input("Davranış Yönlendirme")
    madde = st.text_input("Madde (32/1 veya 32/2)")

if st.button("Raporu Oluştur"):
    base = f"""
TCK 32

{kurum}un {ust_yazi_tarihi} tarih ve {ust_yazi_sayisi} sayılı yazısı ile 
suç tarihi olan {suc_tarihi} tarihi itibariyle TCK'nın 32. maddesi 
kapsamında değerlendirilip değerlendirilemeyeceği hususunda rapor 
düzenlenmesi için yönlendirilen {tc_kimlik_no} T.C. kimlik nolu 
{ad_soyad}, {muayene_tarihi} tarihinde Hitit Üniversitesi Erol Olçok 
Eğitim ve Araştırma Hastanesi Psikiyatri Polikliniğinde muayene 
edilmiştir.
İlgilinin kendisinden ve ilgili tıbbi/adli evraktan edinilen bilgilere 
göre {anamnez} anlaşılmıştır.
İlgilinin ruhsal durum muayenesinde giyiminin sosyoekonomik düzeyi ile 
uyumlu olduğu, konuşma miktarının ve hızının normal olduğu, duygudurumunun 
ötimik, duygulanımının uygun olduğu, çağrışımlarının düzenli olduğu, sanrı 
ve algı bozukluğunun olmadığı, soyutlama ve muhakeme yetilerinin normal 
olduğu tespit edilmiştir.
"""

    if ehliyet_durumu == 'tam':
        result = f"""
Sonuç: Alınan öykü, incelenen evrak ve yapılan muayene sonucunda 
{ad_soyad}’na {tani} tanısının koyulduğu, bu tanının ilgilinin işlediği 
suçun tarihi olan {suc_tarihi} tarihi itibariyle TCK'nın 32. maddesi 
kapsamında değerlendirilmesine neden olmayacağı, ilgilinin işlediği fiilin 
hukuki anlam ve sonuçlarını algılamasına veya işlediği fiille ilgili 
davranışlarını yönlendirme yeteneğinin etkilenmesine neden olabilecek 
nitelikte bir psikiyatrik bozukluğunun bulunmadığı kanaatini bildirir 
sağlık kurulu raporudur.
"""
    else:
        result = f"""
Sonuç: Alınan öykü, incelenen evrak ve yapılan muayene sonucunda 
{ad_soyad}’na {tani} tanısının koyulduğu, ilgilinin işlediği suçun tarihi 
olan {suc_tarihi} tarihi itibariyle ve hâlihazırda işlediği fiilin hukuki 
anlam ve sonuçlarını {algilama}, işlediği fiille ilgili davranışlarını 
yönlendirme yeteneğinin {davranis}, psikiyatrik hastalığının TCK’nın 
{madde} maddesi kapsamında değerlendirilebileceği kanaatini bildirir 
sağlık kurulu raporudur.
"""
    st.text_area("Oluşturulan Rapor", base + result, height=400)

