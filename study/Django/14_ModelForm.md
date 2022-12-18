앞서 Form Class를 작성해보며 느낄 수 있었던 것은 "Model이랑 중복되는 부분이 너무 많다"라는 것이었다.

우리는 이미 Article Model Class에 필드에 대한 정보를 작성하였는데 이를 **Form에 맵핑**하기 위하여 Form Class를 재정의 해야만 하였다.

#### **목차**

1. ModelForm

2. ModelForm with view Functions

3. Form과 ModelForm 비교

---

### **1. ModelForm**

-   ModelForm을 사용하면 위에서 말했던 중복되는 부분들을 제외하고 Form을 더 쉽게 작성할 수 있게 해 준다.
-   Model을 통해 Form Class를 만들 수 있는 **helper class**
-   ModelForm은 **Form과 똑같은 방식으로 View 함수에서 사용**

> **선언**

-   forms 라이브러리에서 파생된 ModelForm 클래스를 **상속**받는다.
-   정의한 ModelForm 클래스 안에 **Meta 클래스**를 선언
-   어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정

![](https://blog.kakaocdn.net/dn/cwJjDA/btrLqWeODBl/kxwtCQISGCZnt60R6Ks2N0/img.png)

-   **기존의 ArticleForm은 주석 처리한 후 재작성**

> **Meta Class**

-   ModelForm의 정보를 작성하는 곳
-   ModelForm을 사용할 경우 참조할 모델이 있어야 하는데, **Meta class의 model 속성이 이를 구성**
    -   참조하는 모델에 정의된 field 정보를 Form에 적용한다.

![](https://blog.kakaocdn.net/dn/cgXRRk/btrLxZ8oOt4/rn4zmsQ1QKqSM8sHIieVrk/img.png)

-   위와 같이 fields 속성에 **'__all__'**를 사용하여 모델의 모든 필드를 포함할 수 있다.
-   또는 **exclude 속성**을 사용하여 모델에서 포함하지 않을 필드를 지정할 수 있음

![](https://blog.kakaocdn.net/dn/bqb4sC/btrLuycR44y/kYoK7EMTFk1voxsOFDvXak/img.png)

-   fields와 exclude를 함께 작성해도 되나 **권장하지 않는다!!**

**# 참고**

> **Meta data**

-   "데이터를 표현하기 위한 데이터"
-   예시 - "사진 파일"
    -   사진 데이터
    -   사진 데이터의 데이터  ( 촬영 시각, 렌즈, 조리개 값 등 ) = 사진의 Meta data

> **참조 값과 반환 값**

```PYTHON
model = Article
```

위와 같이 호출하지 않고 이름만 작성하는 것이 과연 어떤 의미일까?

-   함수를 예시로 들면 아래와 같은 함수가 있을 때 함수의 이름을 그대로 출력하는 것과 호출 후의 결과를 비교해보자.

![](https://blog.kakaocdn.net/dn/dbgWak/btrLwAODxcI/sTteelelKYrs5P4R23g1DK/img.png)

1.  첫 번째 결과는 함수의 **참조 값**을 출력한다.
2.  두 번째 결과는 함수의 **반환 값**을 출력한다.

그렇다면 **참조 값**을 사용하는 경우는 언제가 있을까?

-   **"함수를 호출하지 않고 함수 자체를 그대로 전달하여, 다른 함수에서 "필요한 시점에" 호출하는 경우**

![](https://blog.kakaocdn.net/dn/qTFAz/btrLqXLwCBb/k6kk0ynfYNQGxFBf2q9c51/img.png)

-   view 함수의 참조 값을 그대로 넘김으로써, path 함수가 내부적으로 해당 view 함수를 "필요한 시점에" 사용하기 위해서!
-   결국 클래스도 마찬가지이다. Article이라는 클래스를 **"호출하지 않고(= model을 인스턴스로 만들지 않고)"** 작성하는 이유는 **ArticleForm이** **해당 클래스를 필요한 시점에 사용**하기 위함
-   또한 이경우에는 ~~인스턴스가 필요한 것이 아닌,~~ 실제 Article 모델의 참조 값을 통하여 **해당 클래스의 필드나 속성 등을 내부적으로 참조하기 위한 이유**도 있다.

**주의!!**

-   Meta 클래스는 왜 여기세 작성할까라는 의문이 드는데 클래스 안의 클래스..? 우선! **파이썬의 문법적 개념으로 접근하지 말자.**
-   단순히 모델 정보를 Meta라는 이름의 내부 클래스로 작성하도록  **ModelForm의 설계가 이렇게 되어있을 뿐** 우리는 ModelForm의 역할과 사용법을 숙지해야 한다.

---

### **2. ModelForm with view functions**

ModelForm으로 인해 view 함수의 구조에도 변화가 있을 것인데 지금부터 알아보자!

**# CREATE**

-   유효성 검사를 통과한다면!@!
    -   데이터 저장 후
    -   상세 페이지로 리다이렉트
-   통과하지 못한다면
    -   작성 페이지로 리다이렉트

![](https://blog.kakaocdn.net/dn/bI8ZUZ/btrLwIMDmZ2/0hkaD3suUSkdTgKMJ4IAkk/img.png)

> **"is_valid()" method**

-   유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
-   데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 **is_valid()를 제공**하여 개발자의 편의를 도움

> **form 인스턴스의 errors 속성**

-   is_valid()의 반환 값이 **False**인 경우 form 인스턴스의 **errors 속성에 값이 작성**되는데, 유효성 검증을 실패한 원인이 **딕셔너리 형태**로 저장된다.
-   title에 공백을 넣고 제출한다면 아래와 같은 에러 메시지를 볼 수 있다.

![](https://blog.kakaocdn.net/dn/cejjPx/btrLouixKHf/ZRDi9bAG3LF5zeskn73Li0/img.png)

![](https://blog.kakaocdn.net/dn/ngANp/btrLqXLxdIe/rASfCT0eYMHAqHybu36TVk/img.png)

-   이 같은 특징을 통하여 아래와 같은 구조로 코드를 작성한다면! **유효성 검증을 실패했을 때** 실패 결과 메시지를 출력해 줄 수 있다.

![](https://blog.kakaocdn.net/dn/bck8X3/btrLuj8aACv/gTqb3CTkkYIxnm5w3wpBv1/img.png)

> **The "save()" method**

-   form 인스턴스에 바인딩된 데이터를 통해 데이터베이스 객체를 만들고 저장
-   ModelForm의 하위 클래스는 키워드 인자 **instance 여부**를 통해 **생성할지, 수정할지를 결정**
    -   제공되지 않은 경우 save()는 지정된 모델의 새 인스턴스를 만듦(CREATE)
    -   제공되면 save()는 해당 인스턴스를 수정(UPDATE)

**# UPDATE**

ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를 지정

1.  **request.POST**  
    -   사용자가 form을 통해 전송한 데이터(새로운 데이터)
2.  **instance**  
    -   수정이 되는 대상

> edit - view 수정

![](https://blog.kakaocdn.net/dn/AwtMU/btrLwIspb01/tLLBlUEeXLHp67jNBpKMVK/img.png)

> edit - template 수정

![](https://blog.kakaocdn.net/dn/pUFfY/btrLx00EKzm/md4mAAnlNmMVRXNAgO36pK/img.png)

> update - view 수정

![](https://blog.kakaocdn.net/dn/cXMvu5/btrLtL4VXpd/pbGaYsbWiyJHMpJMBKfEF0/img.png)

---

### **3. Form과 ModelForm**

ModelForm을 이용하여 Form을 더 쉽게 사용하였다고 해서 ModelForm이 더 좋은 것일까???

**No!!라고 말할 수** 있다. 누가 더 좋은 것이 아닌 **역할**이 다른 것이다.

-   Form
    1.  사용자로부터 받는 데이터가 DB와 연관되어 있지 않는 경우에 사용
    2.  DB에 영향을 미치지 않고 단순 데이터만 사용되는 경우 ( 로그인 - 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도 저장 X )
-   ModelForm
    1.  사용자로부터 받는 데이터가 DB와 연관되어 있는 경우에 사용
    2.  데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 맵핑해야 할지 이미 알고 있기 때문에 곧바로 save() 호출이 가능하다.


### **4. Widgets 활용하기**

앞에서 HTML input 요소 표현 방법 중 렌더링을 담당하는 **위젯**에 대해서 간단히 알아보았고 이를 작성하는 방법을 조금만 더 알아보자.

> **작성**

![](https://blog.kakaocdn.net/dn/bmDoQT/btrLtY4JM4M/Ho5PhJVlIwHNTTJkXWFqi0/img.png)

![](https://blog.kakaocdn.net/dn/UzoOU/btrLtYRdQZ4/ctbWaWidKpfRqlMksLye21/img.png)

-   위에 보듯이 2가지 방법으로 작성을 할 수 있다.
-   첫 번째의 경우 Meta 클래스 내부에서 새로운 클래스 변수를 만들어주었고
-    두번째의 경우 ArticleForm 클래스 바로 내부에 작성을 해주었는데 Form필드에 종속된다.
    -   즉, widget을 적용할 실제 모델 필드에 Form필드를 적용시키고 widget을 입힌다.
-   **두 번째 케이스로 작성하는 것을 권장한다!**
    -   Meta 클래스가 목적이 **ModelForm에 대한 모델 정보를 기록하는 공간**인데 Widget은 그런 공간이라 보기 조금 그렇기 때문!!

![](https://blog.kakaocdn.net/dn/n6IKr/btrLtYqaTRN/Z1LkkkPrE4kXMrWAZo23SK/img.png)

활용하기