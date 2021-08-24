<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# Day 16 이미지 분류 3~4강

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)

2. [Competition](#2-Competition)

3. [피어세션 정리](#3-피어세션-정리)

<!--4. [흥미있던 질문들](#4-흥미있던-질문들)-->

4. [학습 회고](#4-학습-회고)



----

### 1. 강의 내용 정리

* 이미지 분류 3~4강
    * 3강 : Dataset
        * Pre_processing<br>
        &nbsp; - &nbsp; data science에서 가장 많은 시간을 투자하는 단계이다. 그만큼 힐들고 어렵다.<br>
        &nbsp; - &nbsp; Bounding Box : 이미지의 특정 범위를 표시하기 위해서 사용. -> 박스로 범위를 표시한다.<br>
        &nbsp; - &nbsp; Resize : 계산의 효율을 위해 적당한 크기로 사이즈 변경.<br>
        <br>

        * Genreralization <br>
        &nbsp; - &nbsp;  train set -> train, validation으로 만들어 검증을 하자! -> overfitting, underfitting을 주시하자!<br>
        &nbsp; - &nbsp; data augmentation : 주어진 데이터가 가질 수 있는 경우와 상태의 다양성 <br>
        &nbsp; - &nbsp; torchvision.transforms : Image에 적용할 수 있는 다양한 함수들. -> 여러 경우 수의 이미지를 생성할 수 있다.<br>
        &nbsp; - &nbsp; 다른 여러 library를 참고하여 사용하자!<br>
        &nbsp; - &nbsp; '무조건'이라는 것을 조심하자 -> 모든 데이터는 모든 경우/상황에 따라 다르므로 '무조건 이것은 사용해야 된다'라는 것은 없다.<br>
        <br>

    * 4강 : Hyperparameter Tuning
        * 개요<br>
        &nbsp; - &nbsp; 좋은 성능을 내기 위해서 좋은 모델과 좋은 데이터의 적당한 양을 가지고 학습을 시킨 후 마지막으로 성능을 올릴 수 있는 방법 중에 하나가 바로 'Hyperparameter Tuning'입니다. <br> 
        <br>

        * Hyperparameter Tuning<br>
        &nbsp; - &nbsp; 모델 스스로 학습하지 않는 값은 사람이 지정 -> ex. learning rate, 모델의 크기, optimizer 등 <br>
        &nbsp; - &nbsp; hyperparameter에 의해서 성능이 크게 좌우될 때도 있었지만 요즘은 큰 폭은 아니지만 어째든 조금이라도 성능에 영향을 준다. <- 마지막까지 최선을 다하기 위해서는 사용해야 한다. <br>
        &nbsp; - &nbsp; Hyperparameter tuning 방식 <br>
        &nbsp;&nbsp;&nbsp;&nbsp; 1. &nbsp; Grid : hyperparameter의 값의 범위를 일정범위 기준으로 나눠서 찾는 방법.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; 2. &nbsp; Random : hyperparmeter의 값을 무작위로 선택해서 찾는 방법.<br>
        &nbsp;&nbsp;&nbsp;&nbsp; => &nbsp; 예전에는 Random 방식을 이용해서 성능이 잘 나오는 구간의 hyperparameter 범위를 찾아주고 그 구간에서 grid를 이용해서 찾아주는 방식을 많이 사용했다고 한다. <- 지금은 베이지안 기법들을 주로 많이 사용한다고 함(<- 논문 이름 : BOHB) <br>



        <br>
    

### 2. Competition
<br>



<br>

### 3. 피어세션 정리
<br>
20210824 피어세션

🔍[마스크 데이터 분류 대회]

* 어느 부분에 집중하고 있는지?
    * 모델
    * 전처리
* batsize에 대한 custom data 처리 방식
    * collate_fn 사용해줬다. 질문: collate_fn은 필수인가? <- DataLoader를 사용하면 colalte_fn은 필수가 아니다.
    * x와 label를 따로 따로 해주었다.
    * Label 새로 생성
    * glob 사용
    * 규칙을 발견해서 코드 작성
* DataLoader
    * 이미지 폴더 모듈 관련 :torchvision안에 있는 ImageForder 
        * 장점 : labeling이 어느정도 되어 있어서 전처리시 편리
        * 단점 : 복사로 인한 메모리 차지 
    * tranforms 함수 중에서-  getitem관련 문제 
* 모델 관련
    * VGG  + 2 layer추가 = 높은 validation 값
    * wide-resnet : train set 에서 90%까지 나옴 but overfiting 조심해야 된다.
    * 정확도가 터무니없게 나올때 어디부분이 잘못된 것인지 확인할 수 있는 방법?
* 학습 관련
    * train, validation split 
    * transform에서 normalization해주는 이유
        * 불균형을 해결할 수 있다.
        * 속도가 빨라진다. 
        * 예를 들어서 MNIST에서 반전시킬 경우255값에 치우쳐있게 된다. 이럴때 분산에 정도를 줄여줄 수 있다.
* EDA 활용에 대해서
    * 마스크별 RGB histogram,  마스크 착용여부 RGM histogram 
    * open cv의 casecadeclassifcation 이용 -> BUT 예전에 만들어진 거라서 성능이 좋지 않다.
    * open cv의 detect_face, detect_gender 이용하면 좋다. <- 모든 이미지에 대해서 bounding box를 찾아서 활용하면 좋지 않을까 싶다. 잘못된 라벨링에 대한 문제를 해결할 수 있다.
    * PCA를 활용해보자
    * 공개 코드 -> range(len())부분 오타 : 지워주면 될 것 같다.
* 기타
    * CrossEntropy함수 안에서 자동으로 softmax를 취해준다.

<br><br>

### 4. 학습 회고

