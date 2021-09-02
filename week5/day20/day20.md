<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp;  <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp;  <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# day20

## 목차 



<!--4. [흥미있던 질문들](#4-흥미있던-질문들)-->

1. [학습 회고](#2-학습-회고)



----


### 1. 학습 회고

#### 오늘 마스터님께서 파이참 사용법에 관한 영상을 slack에 공유해주셔서 그걸 따라하면서 어제 해결하지 못한 jupyter부분을 해결하려고 하였으나 ㅠㅠ jupyter server configure를 하는 부분에서 강의 내용과 다르게 자꾸 안되는 부분이 있어서 막혀버렸다 ㅠㅠ
#### 강의와 내 현재 문제의 차이점은 강의에서는 jupyter server가 8888포트였다면 AI stage에서 받은 서버에서 실행되고 있는 jupyter server의 포트는 8890이었다;;; 그래서 강의와 같이 입력을 하면 잘못된 형식이라는 에러를 발생시키고 포트번호를 바꿔서 8888이라고 넣어보면 설정이 바뀌지 않고 그대로 auto server라고 나온다 ㅎㅎ;;; 그래서 이 부분에 대해서 AI stage 이슈 및 건의 게시판에 글을 작성하였다. 현재는 VScode로 작업하는 중이다.
<br>

#### 전날과 마찮가지로 setting부분에서 시간을 많이 소비해서 시도해 본 것을 Efficient-b7 모델을 사용한 것 밖에 없다. 한 epoch 1시간 20분 정도 걸리는 것 같다 ㅎㅎ;;; 그리고 data augmentation도 우리팀 최고 기록을 세웠던 캠퍼님 방식을 사용했다. 결과는 아마도 내일정도에 볼 수 있을 것 같다. ㅠㅠ
<br>

#### 시도해본 것 정리
1. 모델 Main model -> EfficientNet-b7
2. undersampling + data augmentation(rotate) -> data augmentation(팀 최고 기록 방식 사용)  
