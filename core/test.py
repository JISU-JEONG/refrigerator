import json


cook = {
    #지수
    '100.png' : '감자',
    '101.png' : '감자,양파',
    '102.png' : '감자,양파',
    '00000.jpg' : '스팸,고추,감자,양파',
    '01000.jpg' : '감자,양파',
    '01001.jpeg' : '감자,양파',

    '07000.jpg' : '스팸',
    '07001.jpg' : '스팸',
    '07002.jpg' : '스팸',
    '07003.jpg' : '스팸',
    '07004.jpg' : '스팸',
    '07005.jpg' : '스팸',
    '07006.jpg' : '스팸',
    '07007.jpg' : '스팸',
    '07008.jpg' : '스팸',
    '07009.jpg' : '스팸',
    '07010.jpg' : '스팸',
    '07011.jpg' : '스팸',
    '07012.jpg' : '스팸',
    '07013.jpg' : '스팸',
    '07014.jpg' : '스팸',
    '07015.jpg' : '스팸',
    '07016.jpg' : '스팸',
    '07017.jpg' : '스팸',
    '07018.jpg' : '스팸',
    
    '08000.jpg' : '감자',
    '08001.jpg' : '감자',
    '08002.jpg' : '감자',
    '08003.jpg' : '감자',
    '08004.jpg' : '감자',
    '08005.jpg' : '감자',
    '08006.jpg' : '감자',
    '08007.jpg' : '감자',
    '08008.jpg' : '감자',
    '08009.jpg' : '감자',
    '08010.jpg' : '감자',
    '08020.jpg' : '감자',
    '08011.jpg' : '감자',
    '08012.jpg' : '감자',
    '08013.jpg' : '감자',
    '08014.jpg' : '감자',
    '08015.jpg' : '감자',
    '08016.jpg' : '감자',
    '08017.jpg' : '감자',
    '08018.jpg' : '감자',
    '08019.jpg' : '감자',
    '08021.jpg' : '감자',
    '08022.jpg' : '감자',
    '08023.jpg' : '감자',
    '08024.jpg' : '감자',
    '08025.jpg' : '감자',
    '08026.jpg' : '감자',
    '08027.jpg' : '감자',

    '09000.jpg' : '양파',
    '09001.jpg' : '양파',
    '09002.jpg' : '양파',
    '09003.jpg' : '양파',
    '09004.jpg' : '양파',
    '09005.jpg' : '양파',
    '09006.jpg' : '양파',
    '09007.jpg' : '양파',
    '09008.jpg' : '양파',

    '10100.jpg' : '스팸',
    '10101.jpg' : '스팸',
    '10102.jpg' : '스팸',
    '10103.jpg' : '스팸',
    '10104.jpg' : '스팸',
    '10105.jpg' : '스팸',
    '10106.jpg' : '스팸',
    '10107.jpg' : '스팸',
    '10108.jpg' : '스팸',
    '10109.jpg' : '스팸',
    '10110.jpg' : '스팸',
    '10201.jpg' : '감자',
    '10202.jpg' : '감자',
    '10203.jpg' : '감자',
    '10204.jpg' : '감자',
    '10205.png' : '감자',
    '10206.jpg' : '감자',
    '10206.jpg' : '감자',
    '10207.jpg' : '감자',
    '10208.jpg' : '감자',
    '10209.jpg' : '감자',
    '10210.jpg' : '감자',
    '10211.jpg' : '감자',
    '10212.jpg' : '감자',
    '10213.jpg' : '감자',
    '10214.jpg' : '감자',
    '10215.jpg' : '감자',
    '10216.jpg' : '감자',
    '10217.jpg' : '감자',
    '10218.jpg' : '감자',
    '10219.jpg' : '감자',
    '10220.jpg' : '감자',
    '10221.jpg' : '감자',
    '10222.jpg' : '감자',
    '10223.jpg' : '감자',
    '10224.jpg' : '감자',
    '10225.jpg' : '감자',
    '10226.jpg' : '감자',
    '10227.jpg' : '감자',
    '10228.jpg' : '감자',
    '10229.jpg' : '감자',
    '10230.jpg' : '감자',
    '10231.jpg' : '감자',
    '10232.jpg' : '감자',
    '10233.jpg' : '감자',
    '10234.jpg' : '감자',
    '10235.jpg' : '감자',
    '10236.jpg' : '감자',
    '10237.jpg' : '감자',
    '10238.jpg' : '감자',
    '10239.jpg' : '감자',
    '10240.jpg' : '감자',
    '10241.jpg' : '감자',
    '10242.jpg' : '감자',
    '10243.jpg' : '감자',
    '10244.jpg' : '감자',
    '10245.jpg' : '감자',
    '10246.jpg' : '감자',
    '10247.jpg' : '감자',
    '10248.jpg' : '감자',
    '10249.jpg' : '감자',
    '10250.jpeg' : '감자',
    '10251.jpg' : '감자',
    '10252.jpg' : '감자',
    '10301.jpg' : '스팸',
    '10302.jpg' : '스팸',
    '10303.jpg' : '스팸',
    '10304.jpg' : '스팸',
    '10305.jpg' : '스팸',
    '10306.jpg' : '스팸',
    '10307.jpg' : '스팸',
    '10308.jpg' : '스팸',
    '10309.jpg' : '스팸',
    '10310.jpg' : '스팸',
    '10311.jpg' : '스팸',
    '10312.jpg' : '스팸',
    '10313.jpg' : '스팸',
    '10314.jpg' : '스팸',
    '10315.jpg' : '스팸',
    '10316.jpg' : '스팸',
    '10317.jpg' : '스팸',
    '10318.jpg' : '스팸',
    '10319.jpg' : '스팸',
    '10320.jpg' : '스팸',
    '10321.jpg' : '스팸',
    '10322.jpg' : '스팸',
    '10323.jpg' : '스팸',
    '10324.jpg' : '스팸',
    '10325.jpg' : '스팸',
    '10326.jpg' : '스팸',
    '10327.jpg' : '스팸',
    '10328.jpg' : '스팸',
    '10329.jpg' : '스팸',
    '10330.jpg' : '스팸',
    '10331.jpg' : '스팸',
    '10332.jpg' : '스팸',
    '10333.jpg' : '스팸',
    '10334.jpg' : '스팸',
    '10335.jpg' : '스팸',
    '10336.jpg' : '스팸',
    '10337.jpg' : '스팸',
    '10338.jpg' : '스팸',
    '10339.jpg' : '스팸',
    '10340.jpg' : '스팸',
    '10341.jpg' : '스팸',
    '10342.jpg' : '스팸',
    '10343.jpg' : '스팸',
    '10344.jpg' : '스팸',
    '10345.jpg' : '스팸',
    '10346.jpg' : '스팸',
    '10347.jpg' : '스팸',
    '10348.jpg' : '스팸',
    '10349.jpg' : '스팸',
    '10350.jpg' : '스팸',
    '10351.jpg' : '스팸',
    # '10352.jpg' : '스팸',

    '11000.jpg' : '고추',
    '11001.jpg' : '고추',
    '11002.jpg' : '고추',
    '11003.jpg' : '고추',
    '11004.jpg' : '고추',
    '11005.jpg' : '고추',
    '11006.jpg' : '고추',
    '11007.jpg' : '고추',
    '11008.jpg' : '고추',
    '11009.jpg' : '고추',
    '11010.jpg' : '고추',
    '11011.jpg' : '고추',
    '11012.jpg' : '고추',
    '11013.jpg' : '고추',
    '11014.jpg' : '고추',
    '11015.jpg' : '고추',
    '11016.jpg' : '고추',
    '11017.jpg' : '고추',
    '11018.jpg' : '고추',
    '11019.jpg' : '고추',
    '11020.jpg' : '고추',
    '11021.jpg' : '고추',
    # '11022.jpg' : '마늘,고추',
    '11023.jpg' : '고추',
    '11024.jpg' : '고추',
    '11025.jpg' : '고추',
    '11026.jpg' : '고추',
    '11027.jpg' : '고추',
    '11028.jpg' : '고추',
    '11029.jpg' : '고추',
    '11030.jpg' : '고추',
    '11031.jpg' : '고추',
    '11032.png' : '고추',
    '11033.jpg' : '고추',
    '11034.jpg' : '고추',
    '11035.jpg' : '고추',
    '11036.jpg' : '고추',
    '11037.jpg' : '고추',
    '11038.jpg' : '고추',
    '11039.jpg' : '고추',
    '11040.jpg' : '고추',
    '11041.jpg' : '고추',
    '11042.jpg' : '고추',
    '11043.jpg' : '고추',
    '11044.jpg' : '고추',
    '11045.jpg' : '고추',
    '11046.jpg' : '고추',
    '11047.jpg' : '고추',
    '11048.jpg' : '고추',
    '11049.jpg' : '고추',
    '11050.jpg' : '고추',
    '11051.jpg' : '고추',
    '11052.jpg' : '고추',
    '11053.jpg' : '고추',
    '11054.jpg' : '고추',
    '11055.jpg' : '고추',
    '11056.jpg' : '고추',
    '11057.jpg' : '고추',
    '11058.jpg' : '고추',
    '11059.jpg' : '고추',
    '11060.jpg' : '고추',
    '11061.jpg' : '고추',
    '11062.jpg' : '고추',
    '11063.jpg' : '고추',
    '11064.jpg' : '고추',
    '11065.jpg' : '고추',
    '11066.jpg' : '고추',
    '11067.jpg' : '고추',
    '11068.jpg' : '고추',
    '11069.jpg' : '고추',
    '11070.jpg' : '고추',
    '11071.jpg' : '고추',
    '11072.jpg' : '고추',
    '11073.jpg' : '고추',

    '12000.jpg' : '감자,사과',
    '12001.jpg' : '감자,사과',
    '12002.jpg' : '감자,사과',
    '12003.jpg' : '감자,사과',
    '12004.jpg' : '감자,사과',
    '12005.jpg' : '감자,사과',
    '12006.jpg' : '감자,사과',
    '12007.jpg' : '감자,사과',
    '12008.jpg' : '감자,사과',
    '12009.jpg' : '감자,사과',
    '12010.jpg' : '감자,사과',
    '12011.jpg' : '감자,사과',
    # '12012.jpg' : '감자,사과',
    "13000.jpg": "고추,양파",
    "13001.jpg": "고추,양파",
    "13002.jpg": "고추,양파",
    "13003.jpg": "양파",
    "13004.jpg": "양파",
    "13005.jpg": "양파",
    "13006.jpg": "양파",
    "13007.jpg": "양파",
    "13008.jpg": "고추,양파",
    "13009.jpg": "고추,양파",
    "13010.jpg": "고추,양파",
    "13011.jpg": "고추,양파",
    "13012.jpg": "고추,양파",
    "13013.jpg": "고추,양파",
    "13014.jpg": "고추,양파",
    "13015.jpg": "고추,양파",
    "13016.jpg": "고추,양파",
    "13017.jpg": "고추,양파",
    "13018.jpg": "양파",
    "13019.jpg": "양파",
    "13020.jpg": "양파",
    "13021.jpg": "양파",
    "13022.jpg": "양파",
    "14000.jpg": "양파,스팸,고추,감자",
    "14001.jpg": "양파,스팸,고추,감자",
    "14002.jpg": "양파,스팸,고추,감자",
    "14003.jpg": "양파,스팸,고추,감자",
    "14004.jpg": "양파,스팸,고추,감자",
    "14005.jpg": "양파,스팸,고추,감자",
    "14006.jpg": "양파,스팸,고추,감자",
    "14007.jpg": "양파,스팸,고추,감자",
    "14008.jpg": "양파,스팸,고추,감자",
    "14009.jpg": "양파,스팸,고추,감자",
    "14010.jpg": "양파,스팸,고추,감자",
    "14011.jpg": "양파,스팸,고추,감자",
    "14012.jpg": "양파,스팸,고추,감자",
    "14013.jpg": "양파,스팸,고추,감자",
    "14014.jpg": "양파,스팸,고추,감자",
    "14015.jpg": "양파,스팸,고추,감자",
    "14016.jpg": "양파,스팸,감자",
    "14017.jpg": "양파,스팸,감자",
    "14018.jpg": "스팸,감자",
    "14019.jpg": "스팸,감자",
    "14020.jpg": "스팸,감자",
    "14021.jpg": "스팸,감자",
    "14022.jpg": "스팸",
    "14023.jpg": "스팸",
    "14024.jpg": "스팸",
    "14025.jpg": "스팸",
    "14026.jpg": "스팸",
    "14027.jpg": "스팸",
    "14028.jpg": "스팸",
    "14029.jpg": "스팸",
    "14030.jpg": "스팸",
    "14031.jpg": "스팸,감자,고추",
    "14032.jpg": "스팸,감자,고추",
    "14033.jpg": "감자,고추",
    "14034.jpg": "감자,고추",
    "14035.jpg": "감자,고추",
    "14036.jpg": "감자,고추",
    "14037.jpg": "감자,고추",
    "14038.jpg": "감자",
    "14039.jpg": "감자",
    "14040.jpg": "감자",
    "14041.jpg": "감자",
    "14042.jpg": "감자",
    "14043.jpg": "감자",
    "14044.jpg": "감자",
    "14045.jpg": "감자",
    "14046.jpg": "감자",
    "14047.jpg": "감자",
    "14048.jpg": "감자",
    "14049.jpg": "감자",
    "14050.jpg": "감자,스팸",
    "14051.jpg": "감자,스팸",
    "14052.jpg": "감자,스팸",
    "14053.jpg": "감자,스팸",
    "14054.jpg": "감자,스팸",
    "14055.jpg": "감자,스팸",
    "14056.jpg": "감자,스팸,고추",
    "14057.jpg": "감자,스팸,고추",
    "14058.jpg": "감자,스팸,고추",
    "14059.jpg": "감자,스팸,고추",
    "14060.jpg": "감자,스팸,고추",
    "14061.jpg": "감자,스팸,고추",
    "14062.jpg": "감자,스팸,고추",
    "14063.jpg": "감자,스팸,고추",
    "14064.jpg": "감자,스팸,고추",
    "14065.jpg": "양파,감자,스팸,고추",
    "14066.jpg": "양파,감자,스팸,고추",
    "14067.jpg": "양파,감자,스팸,고추",
    "14068.jpg": "양파,감자,스팸,고추",
    "14069.jpg": "양파,감자,스팸,고추",
    "14070.jpg": "양파,감자,스팸,고추",
    "14071.jpg": "양파,감자,스팸,고추",
    "14072.jpg": "양파,감자,스팸,고추",
    "14073.jpg": "양파,감자,스팸,고추",
    "14074.jpg": "양파,감자,스팸,고추",
    "14075.jpg": "양파,감자,스팸,고추",
    "15000.jpg": "감자",
    "15001.jpg": "감자",
    "15002.jpg": "감자",
    "15003.jpg": "감자",
    "15004.jpg": "감자",
    "15005.jpg": "감자",
    "15006.jpg": "감자",
    "15007.jpg": "감자",
    "15008.jpg": "감자",
    "15009.jpg": "감자",
    "15020.jpg": "감자",
    "15021.jpg": "감자",
    "15022.jpg": "감자",
    "15023.jpg": "감자",
    "15024.jpg": "감자",
    "15025.jpg": "감자",
    "15026.jpg": "감자",
    # "15027.jpg": "감자",
    "15010.jpg": "감자",
    "15011.jpg": "감자",
    "15012.jpg": "감자",
    "15013.jpg": "감자",
    "15014.jpg": "감자",
    "15015.jpg": "감자",
    "15016.jpg": "감자",
    "15017.jpg": "감자",
    "15018.jpg": "감자",
    "15019.jpg": "감자",
    "15200.jpg": "감자,계란",
    "15201.jpg": "감자,계란",
    "15202.jpg": "감자,계란",
    "15203.jpg": "감자,계란",
    "15204.jpg": "감자,계란",
    "15205.jpg": "감자,계란",
    "15206.jpg": "감자,계란",
    "15207.jpg": "감자,계란",
    "15208.jpg": "감자,계란",
    "15209.jpg": "감자,계란",
    "15210.jpg": "감자,계란",
    "15211.jpg": "감자,계란",
    "15212.jpg": "감자,계란",
    "15213.jpg": "감자,계란",
    "15214.jpg": "감자,계란",
    "15215.jpg": "감자,계란",
    "15216.jpg": "감자,계란",

    "18000.jpg": "계란",
    "18001.jpg": "계란",
    "18002.jpg": "계란",
    "18003.jpg": "계란",
    "18004.jpg": "계란",
    "18005.jpg": "계란",
    "18006.jpg": "계란",
    "18007.jpg": "계란",
    "18008.jpg": "계란",
    "18009.jpg": "계란",
    "18020.jpg": "계란",
    "18021.jpg": "계란",
    "18022.jpg": "계란",
    "18023.jpg": "계란",
    "18024.jpg": "계란",
    "18025.jpg": "계란",
    "18026.jpg": "계란",
    "18027.jpg": "계란",
    "18028.jpg": "계란",
    "18029.jpg": "계란",
    "18010.jpg": "계란",
    "18011.jpg": "계란",
    "18012.jpg": "계란",
    "18013.jpg": "계란",
    "18014.jpg": "계란",
    "18015.jpg": "계란",
    "18016.jpg": "계란",
    "18017.jpg": "계란",
    "18018.jpg": "계란",
    "18019.jpg": "계란",
    "18030.jpg": "계란",
    "18031.jpg": "계란",
    "18032.jpg": "계란",
    "18033.jpg": "계란",
    "18034.jpg": "계란",
    "18035.jpg": "계란",
    "18036.jpg": "계란",
    "18037.jpg": "계란",
    "18038.jpg": "계란",
    "18039.jpg": "계란",
    "18040.jpg": "계란",
    "18041.jpg": "계란",
    "18042.jpg": "계란",
    "18043.jpg": "계란",
    "18044.jpg": "계란",
    "18045.jpg": "계란",
    "18046.jpg": "계란",
    "18047.jpg": "계란",
    "18048.jpg": "계란",
    "18049.jpg": "계란",
    "18050.jpg": "계란",
    "18051.jpg": "계란",
    "18052.jpg": "계란",
    "18053.jpg": "계란",
    "18054.jpg": "계란",
    "18055.jpg": "계란",
    "18056.jpg": "계란",
    "18057.jpg": "계란",
    "18058.jpg": "계란",
    "18059.jpg": "계란",
    "18060.jpg": "계란",
    "18061.jpg": "계란",
    "18062.jpg": "계란",
    "18063.jpg": "계란",
    "18064.jpg": "계란",
    "18065.jpg": "계란",
    "18066.jpg": "계란",
    "18067.jpg": "계란",
    "18068.jpg": "계란",
    "18069.jpg": "계란",
    "18070.jpg": "계란",
    "18071.jpg": "계란",
    "18072.jpg": "계란",
    "18073.jpg": "계란",
    "18074.jpg": "계란",
    "18075.jpg": "계란",
    "18076.jpg": "계란",
    "18077.jpg": "계란",
    "18078.jpg": "계란",
    "18079.jpg": "계란",
    "18080.jpg": "계란",
    "18081.jpg": "계란",
    "18082.jpg": "계란",
    "18083.jpg": "계란",
    "18084.jpg": "계란",
    "18085.jpg": "계란",
    "18086.jpg": "계란",
    "18087.jpg": "계란",
    "18088.jpg": "계란",
    "18089.jpg": "계란",
    "18090.jpg": "계란",
    "18091.jpg": "계란",
    "18092.jpg": "계란",
    "18093.jpg": "계란",
    "18094.jpg": "계란",


    "19000.jpg": "계란",
    "19001.jpg": "계란",
    "19002.jpg": "계란",
    "19003.jpg": "계란",
    "19004.jpg": "계란",
    "19005.jpg": "계란",
    "19006.jpg": "계란",
    "19007.jpg": "계란",
    "19008.jpg": "계란",
    "19009.jpg": "계란",
    "19020.jpg": "계란",
    "19021.jpg": "계란",
    "19022.jpg": "계란",
    "19023.jpg": "계란",
    "19024.jpg": "계란",
    "19025.jpg": "계란",
    "19026.jpg": "계란",
    "19027.jpg": "계란",
    "19028.jpg": "계란",
    "19029.jpg": "계란",
    "19010.jpg": "계란",
    "19011.jpg": "계란",
    "19012.jpg": "계란",
    "19013.jpg": "계란",
    "19014.jpg": "계란",
    "19015.jpg": "계란",
    "19016.jpg": "계란",
    "19017.jpg": "계란",
    "19018.jpg": "계란",
    "19019.jpg": "계란",
    "19030.jpg": "계란",
    "19031.jpg": "계란",
    "19032.jpg": "계란",
    "19033.jpg": "계란",
    # "19034.jpg": "계란",
    "19035.jpg": "계란",


    '10500.jpg' : '감자,양파',
    '10501.jpg' : '감자,양파',
    '10502.jpeg' : '감자,양파',
    '10503.jpeg' : '감자,양파',
    '10504.jpg' : '감자,양파',
    '10505.jpg' : '감자,양파',
    '00001.jpg' : '사과',
    # '00002.jpg' : '딸기',
    '00004.jpg' : '사과',
    # '00008.jpg' : '딸기',
    # '00010.jpg' : '바나나',
    '00012.jpg' : '사과',
    # '00013.jpg' : '오렌지',
    # '00014.jpg' : '포도',
  #   '30000.jpg': '소세지',
  # '30001.jpg': '소세지',
  # '30002.jpg': '소세지',
  # '30003.jpg': '소세지',
  # '30004.jpg': '소세지',
  # '30005.jpg': '소세지',
  # '30006.jpg': '소세지',
  # '30007.jpg': '소세지',
  # '30008.jpg': '소세지',
  # '30009.jpg': '소세지',
  # '30010.jpg': '소세지',
  # '30011.jpg': '소세지',
  # '30012.jpg': '소세지',
  # '30013.jpg': '소세지',
  # '30014.jpg': '소세지',
  '31000.jpg': '스팸',
  '31001.jpg': '스팸',
  '31002.jpg': '스팸',
  '31003.jpg': '스팸',
  '31004.jpg': '스팸',
  '31005.jpg': '스팸',
  '31006.jpg': '스팸',
  '31007.jpg': '스팸',
  '31008.jpg': '스팸',
  '31009.jpg': '스팸',
  '31010.jpg': '스팸',
  '31011.jpg': '스팸',
  '31012.jpg': '스팸',
  '31013.jpg': '스팸',
  '31014.jpg': '스팸',
  # '32000.jpg': '햄',
  # '32001.jpg': '햄',
  # '32002.jpg': '햄',
  # '32003.jpg': '햄',
  # '32004.jpg': '햄',
  # '32005.jpg': '햄',
  # '32006.jpg': '햄',
  # '32007.jpg': '햄',
  # '32008.jpg': '햄',
  # '32009.jpg': '햄',
  # '32010.jpg': '햄',
  # '32011.jpg': '햄',
  # '32012.jpg': '햄',

  #영훈
#   '60000.jpg' : '우유',
# '60001.jpg' : '우유',
# '60002.jpg' : '우유',
# '60003.jpg' : '우유',
# '60004.jpg' : '우유',
# '60005.jpg' : '우유',
# '60006.jpg' : '우유',
# '60007.jpg' : '우유',
# '60008.jpg' : '우유',
# '60009.jpg' : '우유',
# '60010.jpg' : '콩',
# '60011.jpg' : '콩',
# '60012.jpg' : '콩',
# '60013.jpg' : '콩',
# '60014.jpg' : '콩',
# '60015.jpg' : '콩',
# '60016.jpg' : '콩',
# '60017.jpg' : '콩',
# '60018.jpg' : '콩',
# '60019.jpg' : '콩',
# '60020.jpg' : '두부',
# '60021.jpg' : '두부',
# '60022.jpg' : '두부',
# '60023.jpg' : '두부',
# '60024.jpg' : '두부',
# '60025.jpg' : '두부',
# '60026.jpg' : '두부',
# '60027.jpg' : '두부',
# '60028.jpg' : '두부',
# '60029.jpg' : '두부',
# '60030.jpg' : '대파',
# '60031.jpg' : '대파',
# '60032.jpg' : '대파',
# '60033.jpg' : '대파',
# '60034.jpg' : '대파',
# '60035.jpg' : '대파',
# '60036.jpg' : '대파',
# '60037.jpg' : '대파',
# '60038.jpg' : '대파',
# '60039.jpg' : '대파',
# '60040.jpg' : '마늘',
# '60041.jpg' : '마늘',
# '60042.jpg' : '마늘',
# '60043.jpg' : '마늘',
# '60044.jpg' : '마늘',
# '60045.jpg' : '마늘',
# '60046.jpg' : '마늘',
# '60047.jpg' : '마늘',
# '60048.jpg' : '마늘',
# '60049.jpg' : '마늘',
# '60050.jpg' : '다진마늘',
# '60051.jpg' : '다진마늘',
# '60052.jpg' : '다진마늘',
# '60053.jpg' : '다진마늘',
# '60054.jpg' : '다진마늘',
# '60055.jpg' : '다진마늘',
# '60056.jpg' : '다진마늘',
# '60057.jpg' : '다진마늘',
# '60058.jpg' : '다진마늘',
# '60059.jpg' : '다진마늘',
# '60060.jpg' : '오렌지',
# '60061.jpg' : '오렌지',
# '60062.jpg' : '오렌지',
# '60063.jpg' : '오렌지',
# '60064.jpg' : '오렌지',
# '60065.jpg' : '오렌지',
# '60066.jpg' : '오렌지',
# '60067.jpg' : '오렌지',
# '60068.jpg' : '오렌지',
# '60069.jpg' : '오렌지',
# '60070.jpg' : '배',
# '60071.jpg' : '배',
# '60072.jpg' : '배',
# '60073.jpg' : '배',
# '60074.jpg' : '배',
# '60075.jpg' : '배',
# '60076.jpg' : '배',
# '60077.jpg' : '배',
# '60078.jpg' : '배',
# '60079.jpg' : '배',
# '60080.jpg' : '우유',
# '60081.jpg' : '우유',
# '60082.jpg' : '우유',
# '60083.jpg' : '우유',
# '60084.jpg' : '우유',
# '60085.jpg' : '우유',
# '60086.jpg' : '우유',
# '60087.jpg' : '우유',
# '60088.jpg' : '우유',
# '60089.jpg' : '우유',
# '60090.jpg' : '콩',
# '60091.jpg' : '콩',
# '60092.jpg' : '콩',
# '60093.jpg' : '콩',
# '60094.jpg' : '콩',
# '60095.jpg' : '콩',
# '60096.jpg' : '콩',
# '60097.jpg' : '콩',
# '60098.jpg' : '콩',
# '60099.jpg' : '콩',
# '60100.jpg' : '두부',
# '60101.jpg' : '두부',
# '60102.jpg' : '두부',
# '60103.jpg' : '두부',
# '60104.jpg' : '두부',
# '60105.jpg' : '두부',
# '60106.jpg' : '두부',
# '60107.jpg' : '두부',
# '60108.jpg' : '두부',
# '60109.jpg' : '두부',
# '60110.jpg' : '대파',
# '60111.jpg' : '대파',
# '60112.jpg' : '대파',
# '60113.jpg' : '대파',
# '60114.jpg' : '대파',
# '60115.jpg' : '대파',
# '60116.jpg' : '대파',
# '60117.jpg' : '대파',
# '60118.jpg' : '대파',
# '60119.jpg' : '대파',
# '60120.jpg' : '마늘',
# '60121.jpg' : '마늘',
# '60122.jpg' : '마늘',
# '60123.jpg' : '마늘',
# '60124.jpg' : '마늘',
# '60125.jpg' : '마늘',
# '60126.jpg' : '마늘',
# '60127.jpg' : '마늘',
# '60128.jpg' : '마늘',
# '60129.jpg' : '마늘',
# '60130.jpg' : '다진마늘',
# '60131.jpg' : '다진마늘',
# '60132.jpg' : '다진마늘',
# '60133.jpg' : '다진마늘',
# '60134.jpg' : '다진마늘',
# '60135.jpg' : '다진마늘',
# '60136.jpg' : '다진마늘',
# '60137.jpg' : '다진마늘',
# '60138.jpg' : '다진마늘',
# '60139.jpg' : '다진마늘',
# '60140.jpg' : '오렌지',
# '60141.jpg' : '오렌지',
# '60142.jpg' : '오렌지',
# '60143.jpg' : '오렌지',
# '60144.jpg' : '오렌지',
# '60145.jpg' : '오렌지',
# '60146.jpg' : '오렌지',
# '60147.jpg' : '오렌지',
# '60148.jpg' : '오렌지',
# '60149.jpg' : '오렌지',
# '60150.jpg' : '배',
# '60151.jpg' : '배',
# '60152.jpg' : '배',
# '60153.jpg' : '배',
# '60154.jpg' : '배',
# '60155.jpg' : '배',
# '60156.jpg' : '배',
# '60157.jpg' : '배',
# '60158.jpg' : '배',
# '60159.jpg' : '배',
'60200.jpg' : '양파',
'60201.jpg' : '양파',
'60202.jpg' : '양파',
'60203.jpg' : '양파',
'60204.jpg' : '양파',
'60205.jpg' : '양파',
'60206.jpg' : '양파',
'60207.jpg' : '양파',
'60208.jpg' : '양파',
'60209.jpg' : '양파',
'60210.jpg' : '양파',
'60211.jpg' : '양파',
'60212.jpg' : '양파',
'60213.jpg' : '양파',
'60214.jpg' : '양파',
'60215.jpg' : '양파',
'60216.jpg' : '양파',
'60217.jpg' : '양파',
'60218.jpg' : '양파',
'60219.jpg' : '양파',
'60220.jpg' : '양파',
'60221.jpg' : '양파',
'60222.jpg' : '양파',
'60223.jpg' : '양파',
'60224.jpg' : '양파',
'60225.jpg' : '양파',
'60226.jpg' : '양파',
'60227.jpg' : '양파',
'60228.jpg' : '양파',
'60229.jpg' : '양파',
'60230.jpg' : '양파',
'60231.jpg' : '양파',
'60232.jpg' : '양파',
'60233.jpg' : '양파',
'60234.jpg' : '양파',
'60235.jpg' : '양파',
'60236.jpg' : '양파',
'60237.jpg' : '양파',
'60238.jpg' : '양파',
'60239.jpg' : '양파',
'60240.jpg' : '양파',
'60241.jpg' : '양파',
'60242.jpg' : '양파',
'60243.jpg' : '양파',
'60244.jpg' : '양파',
'60245.jpg' : '양파',
'60246.jpg' : '양파',
'60247.jpg' : '양파',
'60248.jpg' : '양파',
'60249.jpg' : '양파',
'60250.jpg' : '양파',
'60251.jpg' : '양파',
'60252.jpg' : '양파',
'60253.jpg' : '양파',
'60254.jpg' : '양파',
'60255.jpg' : '양파',
'60256.jpg' : '양파',
'60257.jpg' : '양파',
'60258.jpg' : '양파',
'60259.jpg' : '양파',
'60260.jpg' : '양파',
'60261.jpg' : '양파',
'60262.jpg' : '양파',
'60263.jpg' : '양파',
'60264.jpg' : '양파',
'60265.jpg' : '양파',
'60266.jpg' : '양파',
'60267.jpg' : '양파',
'60268.jpg' : '양파',
'60269.jpg' : '양파',
'60270.jpg' : '양파',
'60271.jpg' : '양파',
'60272.jpg' : '양파',
'60273.jpg' : '양파',
'60274.jpg' : '양파',
'60275.jpg' : '양파',
'60276.jpg' : '양파',
'60277.jpg' : '양파',
'60278.jpg' : '양파',
'60279.jpg' : '양파',
'60280.jpg' : '양파',
'60281.jpg' : '양파',
'60282.jpg' : '양파',
'60283.jpg' : '양파',
'60284.jpg' : '양파',
'60285.jpg' : '양파',
'60286.jpg' : '양파',
'60287.jpg' : '양파',
'60288.jpg' : '양파',
'60289.jpg' : '양파',
'60290.jpg' : '양파',
'60291.jpg' : '양파',
'60292.jpg' : '양파',
'60293.jpg' : '양파',
'60294.jpg' : '양파',
'60295.jpg' : '양파',
'60296.jpg' : '양파',
'60297.jpg' : '양파',
'60298.jpg' : '양파',
'60299.jpg' : '양파',
'60300.jpg' : '스팸',
'60301.jpg' : '스팸',
'60302.jpg' : '스팸',
'60303.jpg' : '스팸',
'60304.jpg' : '스팸',
'60305.jpg' : '스팸',
'60306.jpg' : '스팸',
'60307.jpg' : '스팸',
'60308.jpg' : '스팸',
'60309.jpg' : '스팸',
'60310.jpg' : '스팸',
'60311.jpg' : '스팸',
'60312.jpg' : '스팸',
'60313.jpg' : '스팸',
'60314.jpg' : '스팸',
'60315.jpg' : '스팸',
# '60316.jpg' : '스팸',
# '60317.jpg' : '스팸',
'60318.jpg' : '스팸',
'60319.jpg' : '스팸',
'60320.jpg' : '스팸',
'60321.jpg' : '스팸',
'60322.jpg' : '스팸',
'60323.jpg' : '스팸',
'60324.jpg' : '스팸',
'60325.jpg' : '스팸',
'60326.jpg' : '스팸',
# '60327.jpg' : '스팸',
# '60328.jpg' : '스팸',
'60329.jpg' : '스팸',
'60330.jpg' : '스팸',
'60331.jpg' : '스팸',
'60332.jpg' : '스팸',
'60333.jpg' : '스팸',
'60334.jpg' : '스팸',
'60335.jpg' : '스팸',
'60336.jpg' : '스팸',
'60337.jpg' : '스팸',
'60338.jpg' : '스팸',
'60339.jpg' : '스팸',
'60340.jpg' : '스팸',
'60341.jpg' : '스팸',
'60342.jpg' : '스팸',
# '60343.jpg' : '스팸',
# '60344.jpg' : '스팸',
'60345.jpg' : '스팸',
# '60346.jpg' : '스팸',
'60347.jpg' : '스팸',
'60348.jpg' : '스팸',
'60349.jpg' : '스팸',
'60350.jpg' : '스팸',
'60351.jpg' : '스팸',
'60352.jpg' : '스팸',
'60353.jpg' : '스팸',
'60354.jpg' : '스팸',
'60355.jpg' : '스팸',
'60356.jpg' : '스팸',
'60357.jpg' : '스팸',
'60358.jpg' : '스팸',
'60359.jpg' : '스팸',
'60360.jpg' : '스팸',
'60361.jpg' : '스팸',
'60362.jpg' : '스팸',
'60363.jpg' : '스팸',
'60364.jpg' : '스팸',
'60365.jpg' : '스팸',


# 기은
	# "40000.jpg": "딸기",
	# "40001.jpg": "딸기",
	# "40002.jpg": "딸기",
	# "40003.jpg": "딸기",
	# "40004.jpg": "딸기",
	# "40005.jpg": "딸기",
	# "40006.jpg": "딸기",
	# "40007.jpg": "딸기",
	# "40008.jpg": "딸기",
	# "40009.jpg": "딸기",
	"40010.jpg": "사과",
	"40011.jpg": "사과",
	"40012.jpg": "사과",
	"40013.jpg": "사과",
	"40014.jpg": "사과",
	"40015.jpg": "사과",
	"40016.jpg": "사과",
	"40017.jpg": "사과",
	"40018.jpg": "사과",
	"40019.jpg": "사과",
	# "40020.jpg": "칼국수면",
	# "40021.jpg": "칼국수면",
	# "40022.jpg": "칼국수면",
	# "40023.jpg": "칼국수면",
	# "40024.jpg": "칼국수면",
	# "40025.jpg": "칼국수면",
	# "40026.jpg": "칼국수면",
	# "40027.jpg": "칼국수면",
	# "40028.jpg": "칼국수면",
	# "40029.jpg": "칼국수면",
	# "40030.jpg": "팥",
	# "40031.jpg": "팥",
	# "40032.jpg": "팥",
	# "40033.jpg": "팥",
	# "40034.jpg": "팥",
	# "40035.jpg": "팥",
	# "40036.jpg": "팥",
	# "40037.jpg": "팥",
	# "40038.jpg": "팥",
	# "40039.jpg": "팥",
  '41001.jpg' : '고추',
'41002.jpg' : '고추',
'41003.jpg' : '고추',
'41004.jpg' : '고추',
'41005.jpg' : '고추',
'41006.jpg' : '고추',
'41007.jpg' : '고추',
'41008.jpg' : '고추',
'41009.jpg' : '고추',
'41010.jpg' : '고추',
'41011.jpg' : '고추',
'41012.jpg' : '고추',
'41013.jpg' : '고추',
'41014.jpg' : '고추',
'41015.jpg' : '고추',
'41016.jpg' : '고추',
'41017.jpg' : '고추',
'41018.jpg' : '고추',
'41019.jpg' : '고추',
'41020.jpg' : '고추',
'41021.jpg' : '고추',
'41022.jpg' : '고추',
'41023.jpg' : '고추',
'41024.jpg' : '고추',
'41025.jpg' : '고추',
'41026.jpg' : '고추',
'41027.jpg' : '고추',
'41028.jpg' : '고추',
'41029.jpg' : '고추',
'41030.jpg' : '고추',
'41031.jpg' : '고추',
'41032.jpg' : '고추',
'41033.jpg' : '고추',
'41034.jpg' : '고추',
'41035.jpg' : '고추',
'41036.jpg' : '고추',
'41037.jpg' : '고추',
'41038.jpg' : '고추',
'41039.jpg' : '고추',
'41040.jpg' : '고추',
'41041.jpg' : '고추',
'41042.jpg' : '고추',
'41043.jpg' : '고추',
'41044.jpg' : '고추',
'41045.jpg' : '고추',
'41046.jpg' : '고추',
'41047.jpg' : '고추',
'41048.jpg' : '고추',
'41049.jpg' : '고추',
'41050.jpg' : '고추',
'41051.jpg' : '고추',
'41052.jpg' : '고추',
'41053.jpg' : '고추',
'41054.jpg' : '고추',
'41055.jpg' : '고추',
'41056.jpg' : '고추',
'41057.jpg' : '고추',
'41058.jpg' : '고추',
'41059.jpg' : '고추',
'41060.jpg' : '고추',
'41061.jpg' : '고추',
'41062.jpg' : '고추',
'41063.jpg' : '고추',
'41064.jpg' : '고추',
'41065.jpg' : '고추',
'41066.jpg' : '고추',
'41067.jpg' : '고추',
'41068.jpg' : '고추',
'41069.jpg' : '고추',
'41070.jpg' : '고추',
'41071.jpg' : '고추',
'41072.jpg' : '고추',
'41073.jpg' : '고추',
'41074.jpg' : '고추',
'41075.jpg' : '고추',
'41076.jpg' : '고추',
'41077.jpg' : '고추',
'41078.jpg' : '고추',
'41079.jpg' : '고추',
'41080.jpg' : '고추',


# '21000.jpg' : '사과,오렌지',
# '21001.jpg' : '사과,오렌지,바나나',
# '21003.jpg' : '사과,오렌지',
# '21007.jpg' : '사과,오렌지',
# '21009.jpg' : '사과,오렌지',
# '21010.jpg' : '사과,오렌지',
# '21011.jpg' : '사과,오렌지',
# '21012.jpg' : '사과,오렌지',
# '21013.jpg' : '사과,바나나',
# '21014.jpeg' : '사과,바나나',
# '21015.jpg' : '사과,바나나',
# '21016.jpg' : '사과,바나나',
# '21017.jpg' : '사과,바나나',
# '21018.jpg' : '사과,바나나',
# '21019.jpg' : '사과,바나나',
# '21020.jpg' : '사과,바나나',
# '21021.jpg' : '사과,바나나',
# '21022.jpg' : '사과,바나나',
# '21024.jpg' : '사과,바나나',
# '21025.jpg' : '사과,바나나',
# '21026.jpg' : '사과,포도',
# '21027.jpg' : '사과,포도',
# '21028.jpg' : '사과,포도',
# '21029.jpg' : '사과,포도',
# '21030.jpg' : '사과,포도',
'21031.jpg' : '사과,감자',
'21032.jpg' : '사과,감자',
'21033.jpg' : '사과,감자',
'21034.jpg' : '사과,감자',
# '21035.jpg' : '사과,딸기',
# '21036.jpg' : '사과,딸기',

# 영길
'50000.jpg': '계란',
  '50001.jpg': '계란',
  '50002.jpg': '계란',
  # '50003.jpg': '계란',
  # '50004.jpg': '계란',
  '50005.jpg': '계란',
  # '50006.jpg': '계란',
  # '50007.jpg': '계란',
  '50008.jpg': '계란',
  # '50009.jpg': '계란',
  # '50010.jpg': '계란',
  # '50011.jpg': '계란',
  # '50012.jpg': '계란',
  # '50013.jpg': '계란',
  # '50014.jpg': '계란',
  '50015.jpg': '계란',
  # '50016.jpg': '계란',
  '50017.jpg': '계란',
  '50018.jpg': '계란',
  # '50019.jpg': '계란',
  # '50020.jpg': '계란',
  '50021.jpg': '계란',
  '50022.jpg': '계란',
  # '50023.jpg': '계란',
  # '50024.jpg': '계란',
  '50025.jpg': '계란',
  # '50026.jpg': '계란',
  '50027.jpg': '계란',
  # '50028.jpg': '계란',
  # '50029.jpg': '계란',
  # '50030.jpg': '계란',
  # '50031.jpg': '계란',
  # '50032.jpg': '계란',
  # '50033.jpg': '계란',
  '50034.jpg': '계란',
  '50035.jpg': '계란',
  '50036.jpg': '계란',
  # '50037.jpg': '계란',
  # '50038.jpg': '계란',
  # '50039.jpg': '계란',
  # '50040.jpg': '계란',
  # '50041.jpg': '계란',
  # '50042.jpg': '계란',
  # '50043.jpg': '계란',
  # '50044.jpg': '계란',
  # '50045.jpg': '계란',
  # '50046.jpg': '계란',
  '50047.jpg': '계란',
  # '50048.jpg': '계란',
  # '50049.jpg': '계란',
  # '50050.jpg': '계란',
  '50051.jpg': '계란',
  # '50052.jpg': '계란',
  # '50053.jpg': '계란',
  '50054.jpg': '계란',
  # '50055.jpg': '계란',
  '50056.jpg': '계란',
  # '50057.jpg': '계란',
  # '50058.jpg': '계란',
  # '50059.jpg': '계란',
  '50060.jpg': '계란',
  # '50061.jpg': '계란',
  # '50062.jpg': '계란',
  # '50063.jpg': '계란',
  # '50064.jpg': '계란',
  # '50065.jpg': '계란',
  # '50066.jpg': '계란',
  # '50067.jpg': '계란',
  # '50068.jpg': '계란',
  # '50069.jpg': '계란',
  '50070.jpg': '계란',
  # '50071.jpg': '계란',
  '50072.jpg': '계란',

  '51001.jpg': '양파',
  # '51002.jpg': '양파',
  '51003.jpg': '양파',
  '51004.jpg': '양파',
  '51005.jpg': '양파',
  '51006.jpg': '양파',
  # '51007.jpg': '양파',
  '51008.jpg': '양파',
  # '51009.jpg': '양파',
  '51010.jpg': '양파',
  '51011.jpg': '양파',
  '51012.jpg': '양파',
  '51013.jpg': '양파',
  '51014.jpg': '양파',
  # '51015.jpg': '양파',
  # '51016.jpg': '양파',
  # '51017.jpg': '양파',
  # '51018.jpg': '양파',
  # '51019.jpg': '양파',
  # '51020.jpg': '양파',
  # '51021.jpg': '양파',
  '51022.jpg': '양파',
  '51023.jpg': '양파',
  # '51024.jpg': '양파',
  # '51025.jpg': '양파',
  # '51026.jpg': '양파',
  # '51027.jpg': '양파',
  # '51028.jpg': '양파',
  # '51029.jpg': '양파',
  '51030.jpg': '양파',
  # '51031.jpg': '양파',
  # '51032.jpg': '양파',
  # '51033.jpg': '양파',
  '51034.jpg': '양파',
  '51035.jpg': '양파',
  # '51036.jpg': '양파',
  # '51037.jpg': '양파',
  # '51038.jpg': '양파',
  '51039.jpg': '양파',
  '51040.jpg': '양파',
  # '51041.jpg': '양파',
  # '51042.jpg': '양파',
  # '51043.jpg': '양파',
  # '51044.jpg': '양파',
  '51045.jpg': '양파',
  # '51046.jpg': '양파',
  # '51047.jpg': '양파',
  '51048.jpg': '양파',
  # '51049.jpg': '양파',
  '51050.jpg': '양파',
  '51051.jpg': '양파',
  '51052.jpg': '양파',
  '51053.jpg': '양파',
  '51054.jpg': '양파',
  '51055.jpg': '양파',
  # '52000.jpg': '땅콩',
  # '52001.jpg': '땅콩',
  # '52002.jpg': '땅콩',
  # '52003.jpg': '땅콩',
  # '52004.jpg': '땅콩',
  # '52005.jpg': '땅콩',
  # '52006.jpg': '땅콩',
  # '52007.jpg': '땅콩',
  # '52008.jpg': '땅콩',
  # '52009.jpg': '땅콩',
  # '52010.jpg': '땅콩',
  # '52011.jpg': '땅콩',
  # '52012.jpg': '땅콩',
  # '52013.jpg': '땅콩',
  # '52014.jpg': '땅콩',
  # '52015.jpg': '땅콩',
  # '52016.jpg': '땅콩',
  # '52017.jpg': '땅콩',
  # '52018.jpg': '땅콩',
  # '52019.jpg': '땅콩',
  # '52020.jpg': '땅콩',
  # '52021.jpg': '땅콩',
  # '52022.jpg': '땅콩',
  # '52023.jpg': '땅콩',
  # '52024.jpg': '땅콩',
  # '52025.jpg': '땅콩',
  # '52026.jpg': '땅콩',
  # '52027.jpg': '땅콩',
  # '52028.jpg': '땅콩',
  # '52029.jpg': '땅콩',
  # '52030.jpg': '땅콩',
  # '52031.jpg': '땅콩',
  # '52032.jpg': '땅콩',
  # '52033.jpg': '땅콩',
  # '52034.jpg': '땅콩',
  # '52035.jpg': '땅콩',
  # '52036.jpg': '땅콩',
  # '52037.jpg': '땅콩',
  # '52038.jpg': '땅콩',
  # '52039.jpg': '땅콩',
  # '52040.jpg': '땅콩',
  # '52041.jpg': '땅콩',
  # '52042.jpg': '땅콩',
  # '52043.jpg': '땅콩',
  # '52044.jpg': '땅콩',
  # '52045.jpg': '땅콩',
  # '52046.jpg': '땅콩',
  # '52047.jpg': '땅콩',
  # '52048.jpg': '땅콩',
  # '52049.jpg': '땅콩',
  # '52050.jpg': '땅콩',
  # '52051.jpg': '땅콩',
  # '52052.jpg': '땅콩',
  # '52053.jpg': '땅콩',
  # '52054.jpg': '땅콩',
  # '52055.jpg': '땅콩',
  # '52056.jpg': '땅콩',
  # '52057.jpg': '땅콩',
  # '52058.jpg': '땅콩',
  # '52059.jpg': '땅콩',
  # '52060.jpg': '땅콩',
  # '52061.jpg': '땅콩',
  # '52062.jpg': '땅콩',
  # '52063.jpg': '땅콩',
  # '52064.jpg': '땅콩',
  # '52065.jpg': '땅콩',
  # '52066.jpg': '땅콩',
  # '52067.jpg': '땅콩',
  # '52068.jpg': '땅콩',
  # '53000.jpg': '날콩가루',
  # '53001.jpg': '날콩가루',
  # '53002.jpg': '날콩가루',
  # '53003.jpg': '날콩가루',
  # '53004.jpg': '날콩가루',
  # '53005.jpg': '날콩가루',
  # '53006.jpg': '날콩가루',
  # '53007.jpg': '날콩가루',
  # '53008.jpg': '날콩가루',
  # '53009.jpg': '날콩가루',
  # '53010.jpg': '날콩가루',
  # '53011.jpg': '날콩가루',
  # '53012.jpg': '날콩가루',
  # '53013.jpg': '날콩가루',
  # '53014.jpg': '날콩가루',
  # '53015.jpg': '날콩가루',
  # '53016.jpg': '날콩가루',
  # '53017.jpg': '날콩가루',
  # '53018.jpg': '날콩가루',
  # '53019.jpg': '날콩가루',
  # '53020.jpg': '날콩가루',
  # '53021.jpg': '날콩가루',
  # '53022.jpg': '날콩가루',
  # '53023.jpg': '날콩가루',
  # '53024.jpg': '날콩가루',
  # '53025.jpg': '날콩가루',
  # '53026.jpg': '날콩가루',
  # '53027.jpg': '날콩가루',
  # '53028.jpg': '날콩가루',
  # '53029.jpg': '날콩가루',
  # '53030.jpg': '날콩가루',
  # '53031.jpg': '날콩가루',
  # '53032.jpg': '날콩가루',
  # '53033.jpg': '날콩가루',
  # '53034.jpg': '날콩가루',
  # '53035.jpg': '날콩가루',
  # '53036.jpg': '날콩가루',
  # '53037.jpg': '날콩가루',
  # '53038.jpg': '날콩가루',
  # '53039.jpg': '날콩가루',
  # '53040.jpg': '날콩가루',
  # '53041.jpg': '날콩가루',
  # '53042.jpg': '날콩가루',
  # '53043.jpg': '날콩가루',
  # '53044.jpg': '날콩가루',
  # '53045.jpg': '날콩가루',
  # '53046.jpg': '날콩가루',
  # '53047.jpg': '날콩가루',
  # '53048.jpg': '날콩가루',
  # '53049.jpg': '날콩가루',
  # '53050.jpg': '날콩가루',
  # '53051.jpg': '날콩가루',
  # '53052.jpg': '날콩가루',
  # '53053.jpg': '날콩가루',
  # '53054.jpg': '날콩가루',
  # '53055.jpg': '날콩가루',
  # '53056.jpg': '날콩가루',
  # '53057.jpg': '날콩가루',
  # '53058.jpg': '날콩가루',
  # '53059.jpg': '날콩가루',
  # '53060.jpg': '날콩가루',
  # '53061.jpg': '날콩가루',
  # '53062.jpg': '날콩가루',
  # '53063.jpg': '날콩가루',
  # '53064.jpg': '날콩가루',
  # '53065.jpg': '날콩가루',
  # '53066.jpg': '날콩가루',
  # '53067.jpg': '날콩가루',
  # '53068.jpg': '날콩가루',
  # '53069.jpg': '날콩가루',
  # '53070.jpg': '날콩가루',
  # '53071.jpg': '날콩가루',
  # '53072.jpg': '날콩가루',
  # '53073.jpg': '날콩가루',
  # '53074.jpg': '날콩가루',
  # '53075.jpg': '날콩가루',
  # '53076.jpg': '날콩가루',
  # '53077.jpg': '날콩가루',
  # '53078.jpg': '날콩가루',
  # '53079.jpg': '날콩가루',
  # '53080.jpg': '날콩가루',
  # '53081.jpg': '날콩가루',
  # '53082.jpg': '날콩가루',
  # '53083.jpg': '날콩가루',
  # '53084.jpg': '날콩가루',
  # '53085.jpg': '날콩가루',
  # '53086.jpg': '날콩가루',
  # '53087.jpg': '날콩가루',
  # '53088.jpg': '날콩가루',
  # '53089.jpg': '날콩가루',
  # '53090.jpg': '날콩가루',
  # '53091.jpg': '날콩가루',
  # '53092.jpg': '날콩가루',
  # '53093.jpg': '날콩가루',
  # '53094.jpg': '날콩가루',
  # '53095.jpg': '날콩가루',
  # '53096.jpg': '날콩가루',
  # '53097.jpg': '날콩가루',
  
}

with open('test.json', 'w',encoding="utf-8") as make_file:
    json.dump(cook, make_file, ensure_ascii=False,indent="\t")

with open('test.json', 'r',encoding="utf-8") as f:
    json_data = json.load(f)
print(json_data)
print(type(json_data))