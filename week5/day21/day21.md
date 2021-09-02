<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp;  <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp;  <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# day21

## 목차 



<!--4. [흥미있던 질문들](#4-흥미있던-질문들)-->

1. [학습 회고](#2-학습-회고)



----


### 1. 학습 회고

#### 오늘은 jupyter notebook으로 작업했던 code를 python idle로 옮기는 작업을 해주었다. 그리고 train, validation을 나눈후 train dataset에만 data augmentation을 해주는 코드를 새롭게 작성하였다.

<br>

#### 그리고 train과 valid을 나눌때 id가 겹치지 않도록(학습되는 사람과 평가 받는 사람이 겹치지 않도록) 코드를 새롭게 작성하는 중이다. 

<br>

#### 어제 돌려놓았던 EfficientNet-b7의 성능을 생각보다 좋지 않았다 ㅠㅠㅠㅠ 12시간정도 돌렸지만.... 결과는 .... 처참했다 ㅎㅎ... ㅠㅠ

#### 오늘 시도해 본 것

1. 어제 돌렸던 모델 결과 : Acc : 73.4921%	F1 : 0.6557
2. 코드 옮기기(jupyter notebook -> python idle)
3. train, valid을 id 기준으로 분류하는 코드 작성하는 중
4. train dataset에만 data augmentation 적용하기 작성 
