import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

fobidden_fishing = [
    {"location": " 수성못 ", "lattitude": 35.8276358 , "longtitude": 128.6177221 },
    {"location": " 도원지 ", "lattitude": 35.8016376 , "longtitude": 128.5476739 },
    {"location": " 옥연지 ", "lattitude": 35.7760839 , "longtitude": 128.4836806 },
    {"location": " 금봉지 ", "lattitude": 35.7778512 , "longtitude": 128.4312361 },
    {"location": " 용흥지 ", "lattitude": 35.6675 , "longtitude": 128.4313889 },
    {"location": " 군위댐 ", "lattitude": 36.1193552 , "longtitude": 128.7952878 },
    {"location": " 창평호 ", "lattitude": 36.0917697 , "longtitude": 128.678327 },
    {"location": " 선암호 ", "lattitude": 35.5168527 , "longtitude": 129.3262754 },
    {"location": " 대암댐 ", "lattitude": 35.5394583 , "longtitude": 129.179594 },
    {"location": " 사연댐 ", "lattitude": 35.6002307 , "longtitude": 129.1879907 },
    {"location": " 태화호 ", "lattitude": 35.5780104 , "longtitude": 129.2353933 },
    {"location": " 반월호 ", "lattitude": 37.3218125 , "longtitude": 126.891706 },
    {"location": " 갈치호 ", "lattitude": 37.335557 , "longtitude": 126.907564 },
    {"location": " 대왕호 ", "lattitude": 37.4317754 , "longtitude": 127.0854906 },
    {"location": " 운중호 ", "lattitude": 37.3932239 , "longtitude": 127.0493008 },
    {"location": " 서현호 ", "lattitude": 37.3844444 , "longtitude": 127.1413889 },
    {"location": " 낙생호(성남) ", "lattitude": 37.354023 , "longtitude": 127.077175 },
    {"location": " 낙생호(용인) ", "lattitude": 37.3527571 , "longtitude": 127.0745772 },
    {"location": " 기흥호 ", "lattitude": 37.2403311 , "longtitude": 127.0998829 },
    {"location": " 공릉호 ", "lattitude": 37.7549814 , "longtitude": 126.8329506 },
    {"location": " 애룡호 ", "lattitude": 37.825862 , "longtitude": 126.8590849 },
    {"location": " 마장호 ", "lattitude": 37.776036 , "longtitude": 126.9267464 },
    {"location": " 금파호 ", "lattitude": 37.9284323 , "longtitude": 126.8363342 },
    {"location": " 초리호 ", "lattitude": 37.9712993 , "longtitude": 126.7975655 },
    {"location": " 봉암호 ", "lattitude": 37.9197419 , "longtitude": 126.9973465 },
    {"location": " 남양호평택) ", "lattitude": 37.013766 , "longtitude": 126.8145563 },
    {"location": " 남양호(화성) ", "lattitude": 37.0138492 , "longtitude": 126.8059183 },
    {"location": " 보통리호 ", "lattitude": 37.1932748 , "longtitude": 126.9748136 },
    {"location": " 삼화리농수로 ", "lattitude": 37.2503229 , "longtitude": 126.8590868 },
    {"location": " 문호리농수로 ", "lattitude": 37.60421 , "longtitude": 127.358647 },
    {"location": " 대벽저류지 ", "lattitude": 37.6168897 , "longtitude": 126.5763905 },
    {"location": " 백운호수 ", "lattitude": 37.3804191 , "longtitude": 127.0028335 },
    {"location": " 오전호 ", "lattitude": 37.3497797 , "longtitude": 126.9770682 },
    {"location": " 왕송호수 ", "lattitude": 37.3067049 , "longtitude": 126.9473965 },
    {"location": " 일왕호 ", "lattitude": 37.2997345 , "longtitude": 127.000697 },
    {"location": " 일월호 ", "lattitude": 37.2880409 , "longtitude": 126.9725612 },
    {"location": " 원천호 ", "lattitude": 37.2814878 , "longtitude": 127.0622471 },
    {"location": " 서호호 ", "lattitude": 37.2779722 , "longtitude": 126.9884368 },
    {"location": " 신대호 ", "lattitude": 37.2868927 , "longtitude": 127.0754639 },
    {"location": " 고모호 ", "lattitude": 37.7977778 , "longtitude": 127.1630556 },
    {"location": " 서랑호 ", "lattitude": 37.1725 , "longtitude": 127.0138889 },
    {"location": " 기산호 ", "lattitude": 37.7779529 , "longtitude": 126.9544381 },
    {"location": " 산정호 ", "lattitude": 38.0705903 , "longtitude": 127.3203937 },
    {"location": " 물왕호 ", "lattitude": 37.3821937 , "longtitude": 126.835738 },
    {"location": " 경포호 ", "lattitude": 37.7966983 , "longtitude": 128.9020548 },
    {"location": " 영랑호 ", "lattitude": 38.2184017 , "longtitude": 128.5812382 },
    {"location": " 학호 ", "lattitude": 38.2337353 , "longtitude": 127.2290923 },
    {"location": " 송지호 ", "lattitude": 38.3360804 , "longtitude": 128.5153243 },
    {"location": " 광포호 ", "lattitude": 38.24039 , "longtitude": 128.5656 },
    {"location": " 천진호 ", "lattitude": 38.25345 , "longtitude": 128.5557 },
    {"location": " 봉포호 ", "lattitude": 38.250871 , "longtitude": 128.560849 },
    {"location": " 매호 ", "lattitude": 37.95068 , "longtitude": 128.7695 },
    {"location": " 명암호 ", "lattitude": 36.64001 , "longtitude": 127.5117 },
    {"location": " 연제호 ", "lattitude": 36.627594 , "longtitude": 127.323325 },
    {"location": " 오창호 ", "lattitude": 36.75143 , "longtitude": 127.4139 },
    {"location": " 호암호 ", "lattitude": 36.96171 , "longtitude": 127.9223 },
    {"location": " 미암소류지 ", "lattitude": 36.817902 , "longtitude": 127.585779 },
    {"location": " 가장골 ", "lattitude": 36.773597 , "longtitude": 127.579869 },
    {"location": " 정안 ", "lattitude": 36.76722 , "longtitude": 127.57899 },
    {"location": " 내성동 ", "lattitude": 36.769615 , "longtitude": 127.588662 },
    {"location": " 서동 ", "lattitude": 36.752355 , "longtitude": 127.598886 },
    {"location": " 탄티 ", "lattitude": 36.8372798 , "longtitude": 127.5943304 },
    {"location": " 송정 ", "lattitude": 36.838591 , "longtitude": 127.5943304 },
    {"location": " 바윗골 ", "lattitude": 36.02317 , "longtitude": 128.8493 },
    {"location": " 영수호 ", "lattitude": 36.8350322 , "longtitude": 127.5945922 },
    {"location": " 영천소류지 ", "lattitude": 36.803633 , "longtitude": 127.562855 },
    {"location": " 연탄 ", "lattitude": 36.803508 , "longtitude": 127.560938 },
    {"location": " 송오리 ", "lattitude": 37.40042 , "longtitude": 128.679 },
    {"location": " 송티 ", "lattitude": 36.803508 , "longtitude": 127.560938 },
    {"location": " 뇌실 ", "lattitude": 36.82644 , "longtitude": 127.5957 },
    {"location": " 백암 ", "lattitude": 37.14362 , "longtitude": 127.3797 },
    {"location": " 원남호(증평) ", "lattitude": 36.852558 , "longtitude": 127.579393 },
    {"location": " 원남호(음성) ", "lattitude": 36.8684921 , "longtitude": 127.5999844 },
    {"location": " 삼기호 ", "lattitude": 36.7225735 , "longtitude": 127.6218874 },
    {"location": " 신항호 ", "lattitude": 36.8512196 , "longtitude": 127.7780789 },
    {"location": " 백마호 ", "lattitude": 37.17133 , "longtitude": 128.0181 },
    {"location": " 금정호 ", "lattitude": 37.026194 , "longtitude": 127.573746 },
    {"location": " 오창호 ", "lattitude": 36.7408114 , "longtitude": 127.4059787 },
    {"location": " 업성호 ", "lattitude": 36.8488889 , "longtitude": 127.1361111 },
    {"location": " 보령호 ", "lattitude": 36.24481 , "longtitude": 126.662 },
    {"location": " 마산호 ", "lattitude": 36.7705556 , "longtitude": 126.9752778 },
    {"location": " 잠홍호 ", "lattitude": 36.7938149 , "longtitude": 126.4921491 },
    {"location": " 탑정호 ", "lattitude": 36.18063 , "longtitude": 127.1602 },
    {"location": " 왕암호 ", "lattitude": 36.10267 , "longtitude": 127.1624 },
    {"location": " 입암호 ", "lattitude": 35.49132 , "longtitude": 126.7911 },
    {"location": " 동부호 ", "lattitude": 36.1214845 , "longtitude": 126.776806 },
    {"location": " 종천수원지 ", "lattitude": 36.11351 , "longtitude": 126.6576 },
    {"location": " 천장호 ", "lattitude": 36.41512 , "longtitude": 126.919 },
    {"location": " 칠갑호 ", "lattitude": 36.4412 , "longtitude": 126.8418 },
    {"location": " 옥계호 ", "lattitude": 36.19324 , "longtitude": 127.8208 },
    {"location": " 상가호 ", "lattitude": 36.7162432 , "longtitude": 126.619861 },
    {"location": " 기지제 ", "lattitude": 35.84502 , "longtitude": 127.0677 },
    {"location": " 인교제 ", "lattitude": 35.821944 , "longtitude": 127.1770811 },
    {"location": " 백석제 ", "lattitude": 35.93358 , "longtitude": 126.7176 },
    {"location": " 오송제 ", "lattitude": 35.86056 , "longtitude": 127.137 },
    {"location": " 지시제 ", "lattitude": 35.7855556 , "longtitude": 127.13 },
    {"location": " 맛내제 ", "lattitude": 35.787726 , "longtitude": 127.139484 },
    {"location": " 서은제 ", "lattitude": 35.8332745 , "longtitude": 127.0935888 },
    {"location": " 군산호수 ", "lattitude": 35.93159 , "longtitude": 126.7507 },
    {"location": " 은파호수 ", "lattitude": 35.95085 , "longtitude": 126.6948 },
    {"location": " 당하호 ", "lattitude": 36.1074621 , "longtitude": 126.9923135 },
    {"location": " 왕궁호 ", "lattitude": 35.99977 , "longtitude": 127.1024 },
    {"location": " 금마호 ", "lattitude": 36.00484 , "longtitude": 127.054 },
    {"location": " 도순호 ", "lattitude": 35.8219604 , "longtitude": 127.1773776 },
    {"location": " 옥정호(정읍) ", "lattitude": 35.6277944 , "longtitude": 127.1470884 },
    {"location": " 옥정호(임실) ", "lattitude": 35.6330495 , "longtitude": 127.1517551 },
    {"location": " 선암호 ", "lattitude": 35.7655736 , "longtitude": 127.0201121 },
    {"location": " 상관호 ", "lattitude": 35.78225 , "longtitude": 127.2217 },
    {"location": " 용담댐 ", "lattitude": 35.87824 , "longtitude": 127.4736 },
    {"location": " 동산호 ", "lattitude": 35.4525116 , "longtitude": 126.9238647 },
    {"location": " 운곡호 ", "lattitude": 35.4650609 , "longtitude": 126.6411691 },
    {"location": " 동림호 ", "lattitude": 36.49343 , "longtitude": 129.4442 },
    {"location": " 원당호 ", "lattitude": 37.9181863 , "longtitude": 126.9875975 },
    {"location": " 상암호 ", "lattitude": 34.98842 , "longtitude": 127.2295 },
    {"location": " 신운천 ", "lattitude": 36.891825 , "longtitude": 127.075043 },
    {"location": " 동천 ", "lattitude": 36.8409289 , "longtitude": 126.9843779 },
    {"location": " 수어호 ", "lattitude": 35.04298 , "longtitude": 127.7105 },
    {"location": " 해평호 ", "lattitude": 34.7378371 , "longtitude": 127.1885078 },
    {"location": " 보문호 ", "lattitude": 35.8443406 , "longtitude": 129.2757152 },
    {"location": " 부항호 ", "lattitude": 35.9819024 , "longtitude": 127.9998692 },
    {"location": " 순흥호 ", "lattitude": 36.93102 , "longtitude": 128.5595 },
    {"location": " 금계호 ", "lattitude": 36.9050048 , "longtitude": 128.5254501 },
    {"location": " 성곡호 ", "lattitude": 36.97112 , "longtitude": 128.6046 },
    {"location": " 영주호 ", "lattitude": 36.7362128 , "longtitude": 128.6748278 },
    {"location": " 보현호 ", "lattitude": 36.126129 , "longtitude": 128.9489827 },
    {"location": " 풍락지 ", "lattitude": 35.95372 , "longtitude": 128.8613 },
    {"location": " 우로지 ", "lattitude": 35.98512 , "longtitude": 128.9555 },
    {"location": " 적제지 ", "lattitude": 35.8067 , "longtitude": 128.8385 },
    {"location": " 대풍지 ", "lattitude": 35.81882 , "longtitude": 128.77 },
    {"location": " 신지 ", "lattitude": 36.3382424 , "longtitude": 128.6707582 },
    {"location": " 반곡지 ", "lattitude": 35.78061 , "longtitude": 128.8068 },
    {"location": " 성덕댐 ", "lattitude": 36.26175 , "longtitude": 128.9602 },
    {"location": " 호촌늪 ", "lattitude": 35.8281547 , "longtitude": 128.4562216 },
    {"location": " 동명지 ", "lattitude": 35.98072 , "longtitude": 128.5671 },
    {"location": " 연호지 ", "lattitude": 35.84028 , "longtitude": 128.6859 },
    {"location": " 주남.동판호 ", "lattitude": 35.314705 , "longtitude": 128.6726824 },
    {"location": " 산남호 ", "lattitude": 35.3501846 , "longtitude": 128.1746102 },
    {"location": " 구천호 ", "lattitude": 34.825255 , "longtitude": 128.6372753 },
    {"location": " 소동호 ", "lattitude": 34.8384487 , "longtitude": 128.6807709 },
    {"location": " 노단이호 ", "lattitude": 35.528912 , "longtitude": 128.569637 },
    {"location": " 대가호 ", "lattitude": 35.00403 , "longtitude": 128.30586 },
    {"location": " 발랑지 ", "lattitude": 37.80456 , "longtitude": 126.9094 },
    {"location": " 마지지 ", "lattitude": 37.9549028 , "longtitude": 126.9195753 },
    {"location": " 청천지 ", "lattitude": 35.22743 , "longtitude": 127.4986 },
    {"location": " 탑정호 ", "lattitude": 36.18009 , "longtitude": 127.1719 },
    {"location": " 서부지 ", "lattitude": 36.12134 , "longtitude": 126.6917 },
    {"location": " 종천지 ", "lattitude": 36.13706 , "longtitude": 126.6515 }]