# Weekend 1-2 ( Python basic for AI 6~7강)

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)
2. [과제 수행 과정 / 결과물 정리](#2-과제-수행-과정--결과물-정리)
3. [학습 회고](#4-학습-회고)



----

### 1. 강의 내용 정리

* Python basic for AI 6~ 7강
    * 6강 : nummpy
        * numpy 특징 <br>
        &nbsp; - &nbsp;일반 List에 비해 빠르고, 메모리 효율적이다. <br>
        &nbsp; - &nbsp;반복문 없이 데이터 배열에 대한 처리를 지원 <br>
        &nbsp; - &nbsp; 선형대수와 관련된 다양한 기능을 제공 <br>
        &nbsp; - &nbsp; dynamic typing을 지원하지 않는다. -> 그래서 메모리 효율적이다. <br>
        <br>

        * 선언 및 형태<br>
        &nbsp; - &nbsp;선언 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; np.array를 통해서 선언<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; np.array(list, dtype)을 통해서 원소 type을 지정해 줄 수 있다.<br>
        &nbsp; - &nbsp; 형태<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; shape : numpy array의 dimension(크기, 형태) 구성을 반환 -> ex) [[1,2,3], [4,5,6]]은 shape가 (2,3)이다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; (2,3)에서 앞에 오는 원소는 가장 높은 차원을 뜻하고 이후에 순차적으로 작아진다. ex) (3,1,2) -> 3차원 : 3, 2차원 : 1, 1차원 : 2를 뜻하며 이것을 배열로 나타내면 [[[1,2]], [[3,4]], [[5,6]]] 이 된다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; dtype : nummpy array데이터 type을 반환함. 위의 예시의 dtype은 int이다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; rank에 따라 불리는 이름이 있다.<br>
        <img src='./img/rank.png'>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; ndim : dimension의 개수 -> rank<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; size는 총 원소의 수를 뜻한다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; ntype : ndarray object의 메모리 크기를 반환한다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; reshape : Array의 shape의 크기를 변경한다. 이때 변경전후의 원소의 갯수는 동일하다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; flatten : 다차원 array를 1차원 array로 변환시킨다.<br>
        <br>
        * indexing & slicing<br>
        &nbsp; - &nbsp;indexing <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; [0,0] 표기법을 지원해준다.<br>

        &nbsp; - &nbsp; slicing<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 행과 열 부분을 나눠서 slicing이 가능하다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; matrix의 부분 집합을 추출할 때 유용하다. <br>
        <img src='./img/slicing.png'><br><br>

        * creation function <br>
        &nbsp; - &nbsp;arrange <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; array의 범위를 지정하여, 값의 list를 생성하는 명령어<br>

        &nbsp; - &nbsp; ones, zeros, empty and someting_like<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; ones : 1로 가득찬 ndarray 생성<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; zeros : 0로 가득찬 ndarray 생성<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; empty : shape만 주어지고 비어있는 ndarray 생성 -> ndarray가 초기화 되어 있지 않음<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 기존 ndarray의 shape 크기 만큼 1, 0 또는 empty array를 반환<br>

        &nbsp; - &nbsp; identity : 단위 행렬(i 행렬)을 생성함<br>
        &nbsp; - &nbsp; eye : 대각선이 1인 행렬, 이때 대각선의 기준을 k로 설정할 수 있다.<br>
        <p align='center'><img src='./img/eye.png' width=350></p>
        &nbsp; - &nbsp; diag : 대각 행렬의 값을 추출함. 이때도 위와 같이 시작 행렬을 k로 설정할 수 있다.<br>

        &nbsp; - &nbsp; random sampling : 데이터 분포에 따른 sampling으로 array를 생성<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; np.random.uniform : 균등분포로 랜덤 생성<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; np.random.normal : 정규분포로 랜던 생성<br>

        * operation function <br>
        &nbsp; - &nbsp; sum : ndarray의 원소들 간의 합을 구함, list의 sum 기능과 동일<br>
        &nbsp; - &nbsp; axis : 모든 operation function을 실행할 때 기준이 되는 dimension 축<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; array의 범위를 지정하여, 값의 list를 생성하는 명령어<br>
        &nbsp; - &nbsp; mean & std : ndarray의 원소들 간의 평균 또는 표준 편차를 반환<br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 이 외에도 다양한 수학 연산자를 제공함<br>
        &nbsp; - &nbsp; concatenate : 2개의 ndarray를 axis에 따라 붙이는 함수<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; vstack<br>
        <p align='center'><img src='./img/vstack.png' width=350></p><br><br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; hstack<br>
        <p align='center'><img src='./img/vstack.png' width=350></p><br><br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; concatenate / axis = 0<br>
        <p align='center'><img src='./img/concatenate0.png' width=350></p><br><br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; concatenate / axis = 1<br>
        <p align='center'><img src='./img/concatenate1.png' width=350></p><br><br>


        * array operations <br>
        &nbsp; - &nbsp; Element-wise operations : array간 shape이 같을 때 일어나는 연산<br>
        &nbsp; - &nbsp; Dot product : Matrix의 기본 연산, dot 함수 사용<br>
        &nbsp; - &nbsp; transpose : np.transpose 또느 object.T를 사용<br>
        &nbsp; - &nbsp; broadcastsing : shape이 다른 배열 간 연산을 지원하는 기능<br>
        <p align='center'><img src='./img/broadcasting.png' width=350></p><br><br>

        * comparisons <br>
        &nbsp; - &nbsp; all : 데이터 전부 조건에 만족 여부 반환<br>
        &nbsp; - &nbsp; any : 데이터 일부 조건에 만족 여부 반환<br>
        &nbsp; - &nbsp; np.where<br>
        &nbsp;&nbsp;&nbsp;&nbsp; 1. &nbsp; 조건에 만족 여부 반환<br>
        &nbsp;&nbsp;&nbsp;&nbsp; 2. &nbsp; 조건에 만족 여부에 따라 지정된 값 반환<br>
        &nbsp; - &nbsp; argmax : darray내 최댓값 index 반환<br>
        &nbsp; - &nbsp; argmin : darray내 최솟값 index 반환<br>

        * boolean & fancy index <br>
        &nbsp; - &nbsp; boolean index : 특정 조건에 따른 값을 배열 형태로 추출, 이때 comparison operation 함수들도 모두 사용가능하다.<br>
        &nbsp; - &nbsp; fancy index : darray를 index value로 사용해서 값 추출 -> object.take도 같은 기능<br>


        * numpy data i/o <br>
        &nbsp; - &nbsp; loadtxt, savetxt : text type의 데이터를 읽고 저장하는 기능<br>
        &nbsp; - &nbsp; save, load : .npy(pickle 형태)로 저장, .npy 확장자 파일을 읽어옴<br>
        <br><br>

    * 7-1 강 : Module and Project
        * Module<br>
        &nbsp; - &nbsp;프로그램에서 특정 기능을 수행하는 작은 단위(개인적인 생각)<br>
        &nbsp; - &nbsp;모듈화를 통해서 재사용성을 높일 수 있다.<br<br>

            
       * 패키지<br>
        &nbsp; - &nbsp;모듈을 모아놓은 단위, 하나의 프로그램<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 패키지 구현시 폴더별로 __ init __ .py 만들고 안에 __ all__ 맨글링으로 사용할 하위 모듈(디렉토리) 이름 리스트와 'from . import 모듈 이름' 넣어준다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; ex)<br>
        ![make_pakage](./img/make_pakage.png)
        <br>

        * 가상환경<br>
        &nbsp; - &nbsp;프로젝트 진행 시 필요한 패키지만 설치하는 환경 <br>
        &nbsp; - &nbsp;anaconda로 가상환경 만들고 사용하는 법<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 생성 : conda create -n 가상환경_이름 파이썬버전<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 가상환경 호출 : conda activate 가상환경_이름<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 가상환경 해제 : conda deactivate<br>
        <br><br>

       
    * 7-2 강 : File / Exception / Log Handling
        * Exception - 시퀀스 자료형으로 문자형 data를 메모리에 저장 <br>
        &nbsp; - &nbsp;종류 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 예상 가능한 예외<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; 발생여부를 사전에 인지할 수 있는 예외<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; 예를 들어서 사용자의 잘못된 입력, 파일 호출 시 파일 없음 등과 같은 상황<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; => &nbsp; 개발자가 if나 except를 통해서 예외처리를 해줘야 한다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 예상이 불가능한 예외<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; 인터프리터 과정에서 발생하는 예외, 개발자 실수, 논리적 오류 등<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; 예를 들어서 리스트의 범위를 넘어가는 index에 접근한다거나 어떤수를 정수 0으로 나누는 행위<br>
        &nbsp; - &nbsp;예외처리(Exception Handling)<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; try ~ except 문법 사용<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; try 범위 안에는 예외 발생 가능한 코드를 넣고 except 범위에는 예외 발생시 대응하는 코드를 넣으면 된다. 이때 (except exception type)과 예외 타입을 정해줄 수 있고 이때는 해당 예외 발생시 예외처리 코드를 수행한다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; try ~ except  ~ else 문법 사용<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; try ~ except에 else를 추가한 구문으로 예외가 발생하지 않았을 경우 else부분의 코드가 실행된다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; try ~ except  ~ finally 문법 사용<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; try ~ except에 finally를 추가한 구문으로 예외가 발생여부와 상관없이 실행되는 코드부분이다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; raise 예외 타입<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; 강제로 exception을 발생.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; assert 예외조건<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp; 특정 조건에 만족하지 않을 경우 예외 발생<br><br>

        * File Handling<br>
        &nbsp; - &nbsp;open : 파일 처리를 위한 함수로 읽기/쓰기/추가 모드가 있다. <br>
        &nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; 일반적으로 open을 하여 사용한 다음 마지막에 close를 통해서 닫아줘야 한다. 이 과정이 귀찮다면 with구문과 함계 open을 사용하면 된다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; with 구문이란 - 주말에 찾아보기 ㅎㅎ<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; read() : 파일 전체의 데이터를 읽어들인다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; readline() : 파일 1줄을 읽어들인다.(개행전까지)<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 쓰기모드 때 encoding 형식을 지정 해줄 수 있다.<br>
        &nbsp; - &nbsp;Pickle<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 파이썬의 객체를 영속화하는 built-in 객체이다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; RCE(Remote Code Execute)공격이 가능하므로 인터넷으로 모르는 사람의 pickle을 다운받을때 조심하도록 해야 한다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[pickle_취약점](https://watchout31337.tistory.com/167)<br>
        <br><br>

        * Logging Handling<br>
        &nbsp; - &nbsp;로그를 남기는 이유 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 프로그램이 실행되는 동안 일어나는 정보를 기록함으로써 문제 발생시 참고할 수 있는 자료로 유용하게 쓰일 수 있다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 로그 기록은 실행시점에 남겨야 하는 기록과 개발시점에서 남겨야하는 기록으로 나눠진다.<br>
        &nbsp; - &nbsp;로그 레벨 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL 순서대로 레벨이 낮아진다(낮을수록 유저도 알아야하는 정보에 가깝다).<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; logging.StreamHandler는 log level이 warning으로 설정이 되어있다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 셋팅된 레벨이하의 로그들을 출력해 준다. 아래의 예시는 기본레벨 셋팅으로 되어있다.<br>
        
	<p align='center'><img src = "./img/log_level.png" width="350px"></p>

        
    <br><br>

    * 정보 설정하기(프로그램 옵션 설정하기)<br>
        &nbsp; - &nbsp;configparser<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 프로그램의 실행 설정을 file에 저장한다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Section, Key, Value값의 형태로 설정된 파일을 사용<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; 설정파일을 Dict Type으로 호출후 사용<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; configparser 모듈을 이용한다.<br>

        * argparser<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; console창에서 프로그램 실행시 setting정보를 저장한다.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; Command-Line Option이라고 부름<br>
        &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; argparse 모듈을 사용한다.<br>
        <img src='./img/argparser.png'>
        <br><br>

<br><br>

### 2. 과제 수행 과정 / 결과물 정리


<br><br>


### 3. 학습 회고

#### 강의 내용을 요약하면서 여러 생각이 들었다. 내가 진도를 빨리 가는것에만 집중하고 있지 않았나? 내가 강의를 통해서 배운게 뭐지? 그 강의 내용에 대해서 내가 설명할 수 있나? 등에 대해서 고민을 해보았고 결국 내 스스로 진도를 빨리 나가는 것에만 생각하고 정작 그 강의를 통해서 무얼 배웠고 알았는지에 대해서는 전혀 발전이 없었다. 오히려 강의를 애매하게 이해해서 원래 알고 있던 개념만 더 흔들릴 뿐이었다. 그래서 다음주부터는 주말에 강의를 듣더라도 강의 내용 정리를 통해서 내가 오늘 들었던 강의 내용을 잘 소화했는지 체크하며 공부할 것이다.
<br>


#### 오늘 피어세션에서 새로 습득한 정보를 공유하는 시간을 가졌는데 매우 즐거운 시간이었다. 다들 경청하고 모르는 것에 대해서 서로 질문하고 답하는 모습을 보면서 공부에 대한 자극을 계속 받게 되었다. 비록 지금은 실력이 없어서 다른 사람들이 질문을 할 때 나는 항상 대답을 못하고 다른 사람이 답변을 해주는 것만 듣지만 오늘부터 지식을 차곡차곡 쌓아서 질문에 답을 할 수 있는 경지에 올라가고 싶다.😄
<br>

#### 아무튼 오늘도 포기하지 않고 천천히 잘 따라간 내 자신에게 고맙고 내일도 화이팅~👍
#### 주말에 남은 강의 내용 정리하고~
#### 강의 듣고~
#### 모르는 개념 찾고~
#### 선택 과제 남은 거 하고~
#### 내일의 나, 힘내~ 🤣


