로그인과 로그아웃의 로직을 이해했다면, 이제 **유효한 데이터**를 저장하기 위한 **회원가입**에 대해 알아보자.

**User Object**와 **User CRUD**에 대해 이해할 수 있을 것이다. (회원 가입, 회원 탈퇴, 회원정보 수정, 비밀번호 변경)

#### **목차**

1.  회원가입
2.  Custom user & Built-in auth forms
3.  회원 탈퇴
4.  회원정보 수정
5.  비밀번호 변경

---

### **1. 회원 가입**

Login과 Logout이 Session에 대한 과정이었다면, 회원가입은 **User를 Create하는 것**이며 **UserCreationForm built-in form**을 사용한다.

> **UserCreationForm  
> **

-   주어진 username과 password로 권한이 없는 새 user를 생성하는 **ModelFrom**
-   아래 3개의 필드를 가진다.
    1.  username (from the user model)
    2.  password1
    3.  password2

**# 로직 작성**

![](https://blog.kakaocdn.net/dn/33UAc/btrMtFOKHCc/lMnQthTfU2u74jeIDXvLCk/img.png)

![](https://blog.kakaocdn.net/dn/rrE0j/btrMkMviH41/XutPujmbWVoSYCz30tf1A0/img.png)

![](https://blog.kakaocdn.net/dn/cQFZB8/btrMrTfnuFk/2lnq0ZMXkRgRSG6tIYFd1K/img.png)

-   base.html에 회원가입 링크 작성

![](https://blog.kakaocdn.net/dn/bCsPwP/btrMkfY2kWX/SqNSJNM1WZISyLNA9xK0bk/img.png)

-   유효한 데이터에 대해 회원가입 로직 작성 (views.py)

![](https://blog.kakaocdn.net/dn/qVG0z/btrMlkSQBMP/KkLMiazoLz2vSnjDAtx6ek/img.png)

여기까지 진행한 후 회원가입을 해보면 **에러 페이지**를 확인할 수 있다.

-   회원가입에 사용하는 UserCreationForm이 우리가 대체한 커스텀 유저 모델이 아닌 **기존 유저 모델**로 인해 작성된 클래스이기 때문

![](https://blog.kakaocdn.net/dn/2iM2w/btrMqtVysIg/rV1yG3QD2mMq3oiFp8PmPk/img.png)

---

### **2. Custom user & Built-in auth forms**

-   Custom user와 기존 built-in auth forms 간의 관계
-   Custom user로 인한 Built-in auth forms 변경

> **AbstractBaseUser의 모든 subclass와 호환되는 forms**

-   아래 Form 클래스는 User 모델을 대체하더라도 커스텀하지 않아도 사용 가능하다.
    1.  **AuthenticationForm**
    2.  **SetPasswordForm**
    3.  **PasswordChangeForm**
    4.  **AdminPasswordchangeForm**
-   커스텀하지 않아도 되는 이뉴는 **기존 User 모델을 참조하는 Form XXXXX**

> **커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms  
> **

1.  **UserCreationForm**
2.  **UserChangeForm**

두 form 모두 **class Meta: model = User**가 등록돼 form이기 때문에 **반드시 커스텀(확장)해야 됨**

**# 커스텀**

![](https://blog.kakaocdn.net/dn/bpGjK5/btrMlUsZTVe/mo3Yigk4PENylHC55Ek750/img.png)

> **get_user_model()**

-   **현재 프로젝트에서 활성화된 사용자 모델(active user model) 반환**
-   직접 참조하지 않는 이유
    -   예 - 기존 User모델이 아닌 User 모델을 커스텀 한 상황에서는 커스텀 User 모델을 자동으로 반환해주기 때문
-   Django는 User 클래스를 직접 참조하는 대신 **get_user_model()을 사용**해 참조해야 한다고 **강조**하고 있음

> **CustomUserCreationForm()으로 대체하기**

![](https://blog.kakaocdn.net/dn/VmURX/btrMoyps60B/KNN8AaCVuOxJmaKMweXSw1/img.png)

변경 후 회원가입해본 뒤 테이블 확인

![](https://blog.kakaocdn.net/dn/tulSN/btrMks44H1M/ZaOsHxcQMwsfv861GfSaF1/img.png)

회원가입이 된 것을 확인했다면 바로 로그인을 진행해보자!!

-   user 데이터를 DB에 저장해준 후 **auth_login(request, user)**를 통하여 반환된 user 데이터를 넘겨준다.

![](https://blog.kakaocdn.net/dn/bcSBLf/btrMnmpfDZZ/dCVhumykGDKpRDWWqV06zK/img.png)

**# 참고 -** **UserCreationForm의 save 메서드**

-   user를 반환하는 것을 확인

![](https://blog.kakaocdn.net/dn/byK4a9/btrMmgW4uMH/XmVNYp7yY6E3Tn7xoAdpp1/img.png)

---

### **3. 회원 탈퇴**

회원 가입과는 반대로 **DB에서 유저를 Delete 하는 것**과 같음

![](https://blog.kakaocdn.net/dn/bjja8V/btrMkNOEkR9/ecgFXUhW6cNPajLY8z6nKk/img.png)

![](https://blog.kakaocdn.net/dn/cGOA2v/btrMlkk7ktp/TWgIITfnEhlx044lWuuny1/img.png)

![](https://blog.kakaocdn.net/dn/234cs/btrMtG1hUZC/kXQQjXYtK1HOxfAzgF1d8k/img.png)

**# 참고 - 탈퇴하면서 해당 유저의 세션 정보도 함께 지우고 싶을 경우**

-   **"탈퇴(1) 후 로그아웃(2)"의 순서가 바뀌면 안 됨**  
    -   먼저 로그아웃 해버리면 해당 요청 객체 정보가 없어지기 때문에 **탈퇴에 필요한 정보 또한 없어짐**

![](https://blog.kakaocdn.net/dn/Iw3uM/btrMrv6O5lM/U7DQz5U2KdTysr5nJ1lZ61/img.png)

---

### **4. 회원정보 수정**

회원정보 수정은 **User를 Update 하는** 것이며 **UserChangeForm built-in form**을 사용

> **UserChangeForm**

-   사용자의 정보 및 권한을 변경하기 위해 **admin 인터페이스**에서 사용되는 **ModelForm**
-   UserChangeForm 또한 ModelForm이기 때문에 **instance 인자**로 **기존 user 데이터 정보를 받는 구조** 또한 **동일**함
-   이미 **이전에 CustomUserChangeForm으로 확장**했기 때문에 CustomUserChangeForm을 사용하기

![](https://blog.kakaocdn.net/dn/bqOnyq/btrMoSVGD4B/zSLCiok1idnulHutqWWeXK/img.png)

![](https://blog.kakaocdn.net/dn/bhAzka/btrMp2KyK44/0WYKKvy0Q0RYkMjkSTTRNK/img.png)

![](https://blog.kakaocdn.net/dn/BZqgS/btrMtFOSbI3/R3R2ntQ00PogDpfKTExIS1/img.png)

앞서 login, logout, 회원가입과 마찬가지로 base.html에 링크 달아준다.

![](https://blog.kakaocdn.net/dn/bTMu0z/btrMrwECnGp/XIA53lUN4fW7Shi4x0hxX1/img.png)

수정 정보 페이지를 확인해보자

![](https://blog.kakaocdn.net/dn/bm27sh/btrMkGa7L3b/9hBnGlijkzwQPGqRkg9pA0/img.png)

> **UserChangeForm 사용 시 문제점**

-   일반 사용자가 접근해서는 안 될 정보들(fields)까지 모두 수정이 가능해짐
    -   admin 인터페이스에서 사용되는 **ModelForm**이기 때문
-   따라서 UserChangeForm을 상속받아 작성해 두었던 서브 클래스 **CustomUserChangeForm**에서 접근 가능한 필드를 **조정**해야 함

![](https://blog.kakaocdn.net/dn/r6ggR/btrMoTNQBta/BzHGYhN2REXe5iU0QURkT1/img.png)

다만, 우리는 fields를 다 상속받아 사용하여 fields명을 알 수 없는데  이를 위해서는 **공식 github**을 들어가야 된다.

> **User model 상속 구조 살펴보기**

1. **UserChangeForm 클래스 구조 확인**

-   Meta 클래스를 보면 User라는 model을 참조하는 **ModelForm**이라는 것을 확인할 수 있음
-   [https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L147](https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L147)

2. **User 클래스 구조 확인**

-   실제로 User 클래스는 Meta 클래스를 제외한 코드가 없고 **AbstractUser 클래스를 상속받고** 있음
-   [https://github.com/django/django/blob/main/django/contrib/auth/models.py#L405](https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L147)

3. **AbstractUser 클래스 구조 확인**

-   클래스 변수명들을 확인해보면 **회원 수정 페이지에서 봤던 필드들과 일치**한다는 것을 확인할 수 있음
-   [https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L334](https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L147)

4. **공식문서의 User 모델 Fields 확인**

-   [https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#user-model](https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L147)

Fields명을 확인한 후 수정하고자 하는 필드 작성 후 출력의 변화 살펴보자.

![](https://blog.kakaocdn.net/dn/u5oM7/btrMrwkk0nl/iOKqTMfRz40WLK4h406sd1/img.png)

![](https://blog.kakaocdn.net/dn/Yr6DF/btrMt3hRLFT/h2Emsmgx317yBuG5k1vvk0/img.png)

-   views.py에서 아래와 같이 수정할 데이터를 받고, 유효성 검증을 거치면서 작성해보자.
-   실제 회원정보가 수정되었다는 것을 볼 수 있다.

![](https://blog.kakaocdn.net/dn/cIilur/btrMlWj112P/1ncybF79GNCbXNfoxnGBl1/img.png)

---

### **5. 비밀번호 변경**

-   사용자가 비밀번호를 변경할 수 있도록 하는 Form
-   이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
-   **이전 비밀번호를 입력하지 않고 비밀번호를 설정**할 수 있는 **SetPasswordForm**을 상속받는 서브 클래스

> **PasswordChangeForm**

-   회원정보 수정 페이지에서 비밀번호 변경 form 주소를 확인해보자

```PYTHON
/accounts/password/
```

![](https://blog.kakaocdn.net/dn/v9yiP/btrMmgW5iGe/z3uxkRnByx8cV4M7PnmRdk/img.png)

![](https://blog.kakaocdn.net/dn/bLqUkc/btrMkNgOVYg/LiLRGPkvN3ngwtljZKeqfK/img.png)

![](https://blog.kakaocdn.net/dn/bysY83/btrMozIFGzl/7CwnX3GY8XSKXW3ZYkzehk/img.png)

**# 참고 - SetPasswordForm 살펴보기**

-   PasswordChangeForm은 SetPasswordForm의 하위 클래스이기 때문에 SetPasswordForm을 확인

![](https://blog.kakaocdn.net/dn/rzXuv/btrMt33fAif/002hKLweourukndE45pApK/img.png)

-   아래와 같이 비밀번호 변경 로직을 작성해준 후 비밀번호 변경을 확인해보자
-   변경 후 **로그인 상태가 지속되지 못하는 문제**가 발생한다.

![](https://blog.kakaocdn.net/dn/bsahY0/btrMt419RXA/CkSjLQdXGZP7AGVxIGMUGK/img.png)

> **암호 변경 시 세션 무효화 방지하기**

-   비밀번호가 변경되면 기존 세션과의 **회원 인증 정보가 일치하지 않게 되어** 버려 로그인 상태가 유지되지 못함
-   비밀번호는 잘 변경되었으나 비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문

> **update_session_auth_hash()**

```PYTHON
update_session_auth_hash(request, user)
```

-   **현재 요청(current request)**과 **새 session data가 파생될 업데이트된 사용자 객체**를 가져오고, session data를 적절하게 업데이트해줌
-   암호가 변경되어도 로그아웃 되지 않도록 **새로운 password의 session data로 session을 업데이트**

![](https://blog.kakaocdn.net/dn/bnk4tg/btrMrwYYrYe/05glFhiyhipjpkFLqg7rQ1/img.png)