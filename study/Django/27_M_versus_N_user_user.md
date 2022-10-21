User 자기 자신과의 M:N 관계 설정을 통하여 팔로우 기능을 구현해보자.

#### **목차**

1.  Profile
2.  Follow

---

### **1. Profile**

-   url 및 view 함수 작성

![](https://blog.kakaocdn.net/dn/41vPp/btrOs3G3ZiI/EUpLPqFcXyzb3fOpLE8K1k/img.png)

-   profile 템플릿 작성

![](https://blog.kakaocdn.net/dn/n4Lo4/btrOpSAvwcJ/UHlOacWxkfzAmabJ1II6f1/img.png)

-   Profile 템플릿으로 이동할 수 있는 하이퍼 링크 작성

![](https://blog.kakaocdn.net/dn/MXaLI/btrOqiTv6s2/p2ofZuVDzyEimhSl80UGR1/img.png)

---

### **2. Follow**

> **모델 관계 설정**

-   ManyToManyField 작성 및 Migration 진행

![](https://blog.kakaocdn.net/dn/vRFrW/btrOtbZnLZo/7QDRoT8RUlSjg8e5fJGMrk/img.png)

![](https://blog.kakaocdn.net/dn/2lrWC/btrOo5GRa4f/Fr5nqncYWXmdnGq99bP7iK/img.png)

-   url 및 view 함수 작성

![](https://blog.kakaocdn.net/dn/pMOyu/btrOtGEPU11/FWkkBU2zoU0d3ma6CHlJd1/img.png)

-   프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성

![](https://blog.kakaocdn.net/dn/b3BVZd/btrOtICEe6G/XJq4pYfPBwPiAenZ03UHFk/img.png)

-   데코레이터 및 is_authenticated 추가

![](https://blog.kakaocdn.net/dn/bjkmzf/btrOs3Uzomo/KgPMmFvchYcehK4vzWrXzk/img.png)