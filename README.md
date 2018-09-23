# zarkacgeldi
Zarın görüntüsünden kaç geldiğini algılama yapay zeka çalışmaları

OpenCV kullanımı
Python kodlama

1. Vektörel Resim
    
    Zarın vektörel resimlerinden zarın hangi yüzünün geldiğinin algılanması. 
    İzlenen yol :
    * Resmi oku ve gri tonlamaya çevir
    * Gri tonlama resmi Gaussian bulankılık uygula
    * Canny algoritması ile kenarları algıla 
    * Kapalı dış konturların tamamını oku
    * Okunan kontur sayısı zarın yüzündeki dairelerin sayısı, dolayısıyla zarın hangi yüzünün geldiği
    
2. JPEG Resim
    
    Zarın standart kamera ile çekilmiş JPEG fotoğraflarından zarın hangi yüzünün geldiğinin algılanması. 
    İzlenen yol :
    * Resmi oku ve eşik değer resmini al 
    * Eşik değer resme Gaussian bulankılık uygula
    * Canny algoritması ile kenarları algıla 
    * Kapalı dış konturların tamamını oku
    * Okunan kontur sayısı zarın yüzündeki dairelerin sayısı, dolayısıyla zarın hangi yüzünün geldiği
    

