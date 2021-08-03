# Day 2 ( Python basic for AI 3강 / AI Math 5 ~ 6 강)

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)
2. [과제 수행 과정 / 결과물 정리](#2-과제-수행-과정--결과물-정리)
3. [피어세션 정리](#3-피어세션-정리)
4. [학습 회고](#4-학습-회고)



----

### 1. 강의 내용 정리

* Python basic for AI 3강
    * 3-1강 : Python Data Structure
        * 문자열(String) - 시퀀스 자료형으로 문자형 data를 메모리에 저장 <br>
        ∴ 여러 유용한 메소드가 많기 때문에 해당 메소드(replace, len, in(연산자) 등) 잘 알고 있어야 함

        * Stack - 나중에 넣은 데이터가 먼저 반환하도록 설계된 데이터 구조이다(LIFO).<br>
        &nbsp; - &nbsp;리스트 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; pop() : 가장 마지막 원소를 꺼낸다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; append() : 가장 마지막에 원소를 추가한다.<br><br>

        * Queue - 먼저 넣은 데이터를 먼저 반환하도록 설계된 데이터 구조(FIFO)<br>
        &nbsp; - &nbsp;deque <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; pop() : 가장 먼저 들어간 원소를 꺼낸다.(실제로 deque에서 가장 마지막 원소 제거)<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; appendleft() : deque의 가장 왼쪽에 원소를 삽입한다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ☆ &nbsp; list에서도 queue 구현이 가능한데 왜 deque를 사용하는 것일까?<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -> 리스트의 insert보다 deque에 appendleft가 더 빠르기 때문이다.
        <br><br>

        * Tuple - 값의 변경이 불가능한 리스트<br>
        &nbsp; - &nbsp;(&nbsp;)을 이용하여 선언 <br>
        &nbsp; - &nbsp;사용하는 이유 -> 사용자의 실수에 의한 에러를 사전에 방지하기 위해서 <br><br>

        * Set - 값의 순서없이 저장, 중복 불허하는 자료형.<br>
        &nbsp; - &nbsp;set() 혹은 {}를 통해서 선언할 수 있다. <br>
        &nbsp; - &nbsp;합집합, 교지합, 차집합 등의 집합연산이 가능 <br>
        <br>

        * Dictionary - 데이터를 key와 value의 쌍으로 저장하는 방식<br>
        &nbsp; - &nbsp;key값을 활용하여 데이터(value)값을 관리한다. <br>
        &nbsp; - &nbsp;{key : value}로 선언을 한다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; values() : value정보를 담고 있는 객체<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; keys() : key정보를 담고 있는 객체<br><br>

        * collection - 사용자의 편의성을 위해 제공되는 여러 모듈의 집합<br>
        &nbsp; - &nbsp;deque : stack과 queue 자료구조를 지원, list보다 효율적이다. <br>
        &nbsp; - &nbsp;Counter :  시퀀스 데이터의 원소들을 각 원소와 원소의 총 개수로 표현하는 dictionary를 반환<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; word counter의 기능으로 활용할 수 있다.<br><br>
        &nbsp; - &nbsp;OrderedDict : Dictinary와 달리, 데이터를 입력한 순서대로 반환함(과거에는 그랬으나 현재는 기본 Dictionary로 이것을 보장해준다.) <br>
        &nbsp; - &nbsp;defaultdict :  Dictionary type의 기본 값을 지정하여 신규값 생성시 활용할 수 있는 자료구조<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Text mining접근법 - Vector Space Model에 유용하게 사용될 수 있다.<br><br>
        &nbsp; - &nbsp;namedtuple :  Tuple 형태의 data를 이름을 지정하여 선언하게 도와주는 자료구조<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; pop() : 가장 마지막 원소를 꺼낸다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; append() : 가장 마지막에 원소를 추가한다.<br><br>

    * 3-2강 : Pythonic code
        * Pythonic code란? - 파일썬 특유의 문법을 활용한 코드이다.<br>
        &nbsp; - &nbsp;이것을 배워야 하는 이유는? -> 많은 사람들이 이 방식으로 코드를 작성하기 때문에 해당 코드들을 이해하기 위해서 배워야 한다<br><br>

            
        - 인터프리터 언어(프로그램 실행시 기계어로 바꿔줌, os에 상관없이 실행 가능) <-> 컴파일 언어(실행전 어셈과 기계어로 번역해줌, os에 따라 실행이 안 될 수도 있음)
        - 객체 지향
        - 동적 타이핑 언어 - 프로그램 실행시 데이터 타입을 정하는 방식
        - 다양한 라이브러리가 있다.
        
        &nbsp;&nbsp;☆ 파이썬의 유래 : 몬티 파이썬이라는 코메디 그룹에서 이름이 유래되었다. 그리고 여기서 파이썬은 그리스 신화속 괴물 뱀을 말한다.
        <br>

        * split & join - 문자열을 나누거나 합치는데 사용됨<br>
        &nbsp; - &nbsp;split() : 특정 기준으로 나눠서 list형태로 반환 <br>
        &nbsp; - &nbsp;join() : 특정 기준으로 문자열로 구성된 list의 원소들을 하나의 문자열로 만든다. <br>
        <br>

        * list comprehension - list를 만들때 일반적인 for문을 활용하여 append하는 것보다 좋은 효율을 지닌 방식.<br>
        &nbsp; - &nbsp;기본적인 사용 방식 : [x for i in range(len(5))]<br>
        &nbsp; - &nbsp;특정(기준이 있는)값 필러링하는 방식 : [i for i in range(len(5)) if i % 2 == 0]<br>
        &nbsp; - &nbsp;삼항식을 이용한 방식 : [i if i % 2 == 0 else i * 2 for i in range(len(5))] <br>
        &nbsp; - &nbsp;2차원 배열 만들기 : [[x for i in range(len(5)) for _ in range(len(5))]] <br>
        <br>

        * enumerate & zip <br>
        &nbsp; - &nbsp;enumerate : list의 원소를 순서대로 추출하는데 이때 번호를 붙여서 추출한다 <br>
        &nbsp; - &nbsp;zip : 2개 이상의 list의 값을 병렬적으로 추출한다. <br>
        <br>

        * lamda & map & reduce - legacy한 방식이지만 여전히 많이 사용된다.<br>
        &nbsp; - &nbsp;lambda : C언어에 매크로 함수와 비슷한것 같다.<br> ex) lambda x, y : x + y  <br>
        &nbsp; - &nbsp;map : 2개 이상의 list에 함수를 적용하는 방식으로 사용된다.<br>ex) map(lambda x, y : x+y, list(1,2,3,4,5), list(1,2,3,4,5)) -> list(2,4,6,8,10) <br>
        &nbsp; - &nbsp;reduce : 하나의 list에 똑같은 함수를 중첩?해서 적용<br> ex) reduce(lambda x, y : x + y, list(1,2,3,4,5)) - > 15  <br>
        <br>

        * iterable object - sequence형 자료형에서 데이터를 순서대로 추출하는 객체<br>
        &nbsp; - &nbsp;iter()을 사용하여 iterator 객체를 생성할 수 있다. <br>
        &nbsp; - &nbsp;내부적으로 __ inter__ 와 __ next __가 사용된다.<br>
        <br>

        * generator - iteralbe o<br>
        &nbsp; - &nbsp;iterable 객체를 특수한 형태로 사용할 수 있도록 해주는 함수<br>
        &nbsp; - &nbsp;yield 사용시 특정 시점에서 element를 반환. -> 메모리를 효율적으로 사용할 수 있다. <br>
        <br>

        * asterisk - 값의 순서없이 저장, 중복 불허하는 자료형.<br>
        &nbsp; - &nbsp;* : 곱셈 연산<br>
        &nbsp; - &nbsp;*args : 튜플형태의 가변인자<br>
        &nbsp; - &nbsp;*list() : unpacking 해주는 기능<br>
        &nbsp; - &nbsp; ** : 제곱연산  <br>
        &nbsp; - &nbsp; **kwargs : dictionary형태의 가변인자(keyward 형태로 인자를 전달함)<br>
        <br>

   
        <br><br>
* AI Math 5 ~ 6강
    * 5강 : 딥러닝 학습방법 이해하기
        * 지난시간 내용 - 선형모델이 풀지 못하는 문제를 풀기 위해서 비선형모델 신경망이 사용됨<br>
        

        * 소프트맥스(softmax) : 모델의 출력을 확률로 해석할 수 있게 변환해 주는 연산<br>
        &nbsp;  - 분류 문제를 풀 때 선형모델과 소프트맥스 함수를 결합하여 사용한다.<br>
        &nbsp;  - numpy를 이용하여 구현할때 소프트맥스 연산이 지수 함수를 이용한 거라서 오버플로우가 발생할 수 있으므로 이것을 예방할 수 있도록 구현해줘야 한다.<br>
        &nbsp; &nbsp;☆ 추론을 할 때는 원-핫 벡터를 이용하여 최대값을 가진 주소만 사용하기 때문에 이때는 소프트맥스를 이용하지 않음<br>

        * 신경망 - 선형모델과 활성함수(activation functiona)를 합성한 함수이다.<br>
        &nbsp;  ☆ 활성함수에서는 해당 주소?만을 실수 형태의 input으로 받는다. 그러나 소프트맥스는 전체 주소에서 벡터형태로 받는다.<br>
        &nbsp;  ☆ 활성함수를 거쳐야지 선형을 비선형으로 만들어 줄 수 있다. 그래서 딥러닝에서 매우 중요하다.<br>
        &nbsp;  - 다층 퍼셉트론 : 신경망이 여러층으로 합성된 함수<br>
        &nbsp;  - 역전파(backpropagation) <- __이것에 대해서는 좀 더 공부하고 정리하기__<br><br>

    * 6강 : 확률론 맛보기
        * 딥러닝에서 확률론이 필요한 이유? <br>
        &nbsp;  - 회귀분석에서 예측오차의 분산을 가장 최소화하는 L2노름을 구하기 위해<br>
        &nbsp;  - 분류 문제에서는 모델 예측의 불확실성을 최소화하는 교차엔트로피를 유도하기 위해서<br>
        &nbsp;  __☆ 교차 엔트로피에 대해서 알아보기__
        <br>

        * 확률변수 <br>
        &nbsp;  1. 이산형 - 확률변수가 가질 수 있는 경우의 수를 모두 고려하여 확률을 더해서 모델링한 것<br>
        &nbsp;  2. 연속형 - 데이터 공간에 정의된 확률변수의 밀도 위에서 적분을 통해 모델링한 것<br>
        * 조건부 확률<br>
        &nbsp;  - 데이터에서 추출된 패턴을 기반으로 확률을 해석하는데 사용<br>
        &nbsp;  - 분류문제에서 softmax(Wφ + b)은 데이터 x로부터 추출된 특징패턴 φ(x)과 가중치행렬 W을 통해 조건부확률 P(y|φ(x)) 을 계산한다.<br>
        &nbsp;  - 회기문제의 경우, 연속확률분포이므로 조건부기대값을 이용한다.<br>
        
        * 기대값 : 데이터를 대표하는 통계량 -> 이것을 이용하여 분산, 첨도, 공분산 등을 계산할 수 있다.
        * 몬테가를로 샘플링 : 확률분포를 모를 때 데이터를 이용하여 기대값을 계산하기 위해서 사용되는 방식으로 이산형이든 연속형이든 상관없이 사용할 수 있다.<br>
        &nbsp;  __☆  이것에 대해서는 좀 더 공부하고 정리하기__<br><br>

<br><br>

### 2. 과제 수행 과정 / 결과물 정리
<br>

#### AI Math 퀴즈 과제는 어렵지 않았으나 tanh(x)의 미분을 구하는 문제에서 실수로 틀렸다 ㅠㅠ 
### (1-tanh(x))(1+tanh(x))이고 x=1일때 이니까 답은 1인데 1-1 = 0 으로 잘못 생각하는 바람에 😵‍💫

<br><br>

### 파이썬 과제에서는 여러 실수를 반복함으로써 느낀게 몇 가지 있다.
1. 문제를 제대로 안 읽는다. -> 고쳐야 된다! 
2. join, replace, in, strip, split 등에서 대략적인 사용법은 알지만 해당 메소드를 return, input, 사용하기 위한 데이터 타입의 조건 등을 제대로 숙지를 못하여 과제를 하는데 어려움을 겪었다.
3. 오류가 나면 생각 혹은 고민을 한 후 수정해야 하는데 아무생각 없이 수정을 하고 실행결과값만 보면서 의미없는 시간을 보낸다. -> 너무 조급해 하는 것 같음. 여유를 가지는 연습이 필요한 것 같다. 

<br>

### 3. 피어세션 정리

<br>
🔍[이전 질문 리뷰]
<br>
Moore-Penrose Inverse Matrix: 해당 공식의 이해 방법 및 유도 과정을 토의함
 
<br><br>
📒[금일 질문 목록]
<br>
L2 Norm을 사용한 경사하강법의 미분에 대해 질문함
경사하강법의 목적식에 관해 환기함
모든 데이터에 대해 한 번에 최적화하는 방식에 비해 미니배치 훈련 방식의 연산량 감소 이유에 대해 질문함
 
<br><br>
📎[멘토링]
<br>
박기훈 멘토님과의 멘토링
일정 : 8월 5일 목요일 20시 예정
토의 내용 : 목요일 추가 과제관련 질문을 포함한 질문 목록을 생각해보기로 함.
 
<br><br>
📝[‘피어세션이 피어(peer)씁니다’자료 구성]
<br>
우리의 각오 : 단 한 명의 낙오자도 남기지 않겠다
카카오톡으로 작성 후 금일 모더레이터 김범수님께 제출.
 
<br><br>
🖐[그라운드 룰 수정 건의]
<br>
기존 그라운드 룰 중 ‘코드 리뷰와 강의 내용 리뷰’에 관해, 앞으로의 학습 난이도 증가에 따른 시간소요가 늘어날 것으로 예상됨
따라서 피어세션 진행 형식을 미리 정하면 계획적으로 시간을 활용할 수 있을 것
각 팀원이 주 단위로 AI 관련 기술, 이론, 논문 등을 발표하는 룰이 제안됨. (금요일, 10~15분 소요 예상)
팀원 발표에 경청하기의 룰이 제안 됨
심우창님, 최성욱님 이번주 금요일(8/6) 발표 예정
개인 스터디 노트 공유: 강의 정리, 과제 코드 리뷰, 퀴즈 내용을 포함해야 함
 <br><br>

🍋[팀 Github]
<br>
각 팀원 이름으로 구성된 branch에서 작업
과제 코드 리뷰 및 첨삭을 위한 git 저장소 구축

* 이번 피어세셕에 나왔던 질문 - 경사하강법 매운맛 강의에서 증명에 관한 것


### 4. 학습 회고

#### 오늘은 어제보다 들어야 하는 강의 수가 적어서 일찍 잠을 잘 수 있을것 같았지만 늦게 잘 것 같다. 그런데 어제처럼 너무 늦게 잠고 싶지 않아서 ㅠㅠ 파이썬 기본 강의 4강은 내일 들으려고 한다....😭
#### 너무 무리하지 말고 페이스 조절 잘 하면서 동료 캠퍼들을 잘 따라가야 겠다. 


