# Day 3 ( Python basic for AI 4강 ~ 5강 / AI Math 7 ~ 9 강)

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)
2. [과제 수행 과정 / 결과물 정리](#2-과제-수행-과정--결과물-정리)
3. [피어세션 정리](#3-피어세션-정리)
4. [학습 회고](#4-학습-회고)



----

### 1. 강의 내용 정리

* Python basic for AI 4강 ~ 5강
    * 4-1강 : Python Object Oriented Programming
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

    * 4-2강 : Module and Project
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
    * 5-1강 : File / Exception / Log Handling
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

    * 5-2강 : Python data handling
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
   
        
* AI Math 7 ~ 9강
    * 7강 : 동계학 맛보기
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

    * 8강 : 베이즈 통계학 맛보기
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

    * 9강 : CNN 첫걸음
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

#### AI Math 퀴즈 과제 난이도는 어렵지 않아서 다 맞췄으나 공식을 외우고 있지 않거나 제대로 이해 못한게 있어서 퀴즈를 풀 때 강의 pdf를 보면서 풀었다 ㅎㅎ;

<br>

#### 그리고 선택과제는 아직 풀어보지 못 했지만 다행히 제출을 안 해도 된다 ㅎㅎ

<br>

#### 그래서 오늘은 내일 피어세션때 다른 캠퍼들에게 도움이 될만한 내용에 대해서 공부를 하고 공유할 생각이다.


<br><br>


### 3. 피어세션 정리

<br>
🔍[이전 질문 리뷰]<br><br>
SGD 효율성에 대한 질문 : SGD의 연산량이 GD보다 연산량이 더 많아서 덜 효율적이지 않는가?<br>
    * 경사하강법의 종류 : BGD, SGD, MSGD(지난 시간에 SGD라고 생각했던 것)<br>
&nbsp;&nbsp;&nbsp;&nbsp;=> 그러므로 정확한 용어로 사용하면 MSGD의 연산량이 BGD보다 연산량이 더 효율적인가?<br><br>
	* 통용적으로 SGD라고 하면 MSGD를 뜻한다.<br>
iteration : mini_bach를 한 번 학습한 것<br>
		 * BGD는 mini_bach가 total_data이고 SGD는 1개이고 MSGD에서는 지정한 mini_bach 개수이다.<br>
epoch : total_data를 한 번 학습을 끝낸 것<br><br>
	Answer<br><br>
iteration의 횟수는 BGD가 가장 적지만 1 iteration을 하는데 시간이 가장 오래 걸리며 SGD는 1 iteration 당 1개의 데이터만 학습시키므로 1 epoch를 하는데 많은 iteraion이 필요하다. MSGD의 경우는 mini_batch의 수에 따라 1 epoch 당 iteraion의 수를 결정하므로 현실적인 HW성능을 고려할 수 있다는 점에서 효율성이 좋을 것이다.
효율적이려면 가중치 W를 학습시키는 시간의 복잡도가 낮을수록 좋다.<br><br>
 iteration당 시간 복잡도 <br>
&nbsp;&nbsp;&nbsp;&nbsp;*(total_data : 데이터의 총 개수, d : 임의의 일부 데이터 사이즈, batch size : 사용자가 저한 mini_batch 크기)<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;GD : O( total_data *^2)<br>
&nbsp;&nbsp;&nbsp;&nbsp;SGD : O(1 * d^2)<br>
&nbsp;&nbsp;&nbsp;&nbsp;MSGD : O(batch size * d^2 )<br><br>
📒[금일 질문 목록]<br><br>
왜 Relu가 비선형 함수인가?<br>
&nbsp;&nbsp;&nbsp;&nbsp;선형함수 특징<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. 그래프로 그렸을때 직선이어야 한다. 즉, 선이 중간에 꺾이면 안된다. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. 매트릭스로 표현할때 표현이 가능해야 한다.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;함수가 중첩이 되더라도 선형이 된다. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ex) f(x) = ax + b, f(f(x)) = f(ax+b) = a(ax+b) + b = a^2 * x + ab + b
동차성 : f(ax) = a(fx)과 가산성 : f(x1 + x2) = f(x1) + f(x2)을 만족해야 한다.
 <br><br>
sigmoid와 relu 차이<br>
&nbsp;&nbsp;&nbsp;&nbsp;1. sigmoid를 많이 사용할 시 , gradient vanishing 현상이 나타날 수 있다. <br>
&nbsp;&nbsp;&nbsp;&nbsp;2. sigmoid미분시 값이 커질수록 값이 작아지므로 gradient vanishing 현상이 나타날 수 있다. <br>
&nbsp;&nbsp;&nbsp;&nbsp;3. relu(x의 값이 0 이상일때) 미분값이 1임으로 중첩을 많이 하더라도 gradient vanishing현상이 나타나지 않는다.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=> 따라서 sigmoid보다 relu가 활성화 함수를 여러 번 중첩을 할 때 좋은 성능을 낸다.<br><br>
KL-Divergence <br>
&nbsp;&nbsp;&nbsp;&nbsp;분산이 다를때 사용한다.<br><br>
 
 
📎[멘토링시간 질문 정하기]<br>
* AI 직무에 학부생이 살아남을 수 있나?<br>
* AI과정에 통계학에 대한 지식? 얼마나 필요한가? 어떤 곳에 활용될 수 있는가?<br>
* 박기훈 멘토님의 현재 직무, 하고 계신 일은 무엇인가요?<br>
* 멘토활동 어떻신가요?<br>
* 부스트캠프 기간 중에 커리어에 도움이 될만한 활동 추천 내용이 있나요?<br>
* 멘토활동을 참여하게 된 계기.<br>
* 네트워킹데이? 커넥팅데이?<br>
    * 어떤식으로 진행 되었는지, 무엇을 하는지에 대해서<br><br>



### 4. 학습 회고

#### AI Math 7강 '통계학 맛보기'가 생각보다 많이 어려웠다. 피어세션때 서로 이야기를 해보니 나뿐만 아니라 다른 사람들도 어려움을 느낀 것 같다. 그러나 개인적인 생각으로 내가 다른 사람들보다 더 이해를 하지 못한 것 같다. 왜 그런가 곰곰히 생각을 해보니 수식에서 사용되는 수학 기호를 잘 모르는 것이 가장 큰것 같다. 그래서 주말에 기본적인 수학 기호들에 대해서 공부를 하고 차근차근 복습을 해야겠다.
<br>

#### 내일 모더레이터 해야 하는데 오늘 모더레이터를 맡아주신 캠퍼님이 너무 잘해주셔서 부담이 된다 ㅠㅠ 
<br>

#### 그건 그렇고 오늘 모더레이터 해주신 캠퍼님이 확실히 준비를 많이 하시고 진행도 잘 하셨다. 특히 어제 나온 질문에 대해서 공부하고 ppt로 설명을 해주는데 쉽게쉽게 잘 알려주셨다. 어찌나 몰입이 잘 되던지 시간가는줄 모르고 듣고 있었다. 오늘 나온 질문들도 모더레이터 하신 캠퍼님이 다 설명을 해주셔서 내일 내가 준비해야 될게 없다... 음..., 그래서 강의 내용중에 정규표현식에 관한 부분이 있었는데 이에 대해서 좀 더 자세하게 설명하는 ppt를 만들어야 되나 고민이다. 아니면 다른 주제로 해야 하나.... ㅎㅎ..... 
<br>

#### 아무튼 오늘도 포기하지 않고 천천히 잘 따라가서 기분이 좋다. 내일도 화이팅~👍


