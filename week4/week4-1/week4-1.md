<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp;  <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp;  <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# week4-1 

## 목차 

1. [강의 내용 정리](#1-강의-내용-정리)


<!--4. [흥미있던 질문들](#4-흥미있던-질문들)-->

2. [학습 회고](#2-학습-회고)



----

### 1. 강의 내용 정리

* day18 강의 정리 
    



### 2. 학습 회고
<br>

#### day18 이미지 분류 대회 8강 정리를 끝냈다. 그후에는 DenseNet과 우리 팀에서 성능이 가장 좋았던 모델을 Main으로 삼아서 학습을 시킨후 eval을 통해 나온 csv를 비교 분석을 하였다.
#### 놀라운 점은 DenszeNet161의 경우 신기하게 기존의 data를 undersampling한게 성능이 더 좋았지만 Main model의 경우에는 undersampling + data augmentation이 더 효과적이었다.
#### 그러나 팀 최고 score는 갱신하지 못하였다. 그리고 csv파일로 비교분석한 결과 팀 최고 기록 csv > DenseNet undersampling csv > Main model undersampling + data augmentation csv 순으로 
#### 결과가 좋았고 DenseNet은 팀 최고 기록과 비교했을때 나이부분에서 잘 구별을 못하였고 Main model undersampling + data agumentation csv는 나이와 성별, 마스크 착용여부 등 전체적으로 성능이 좋지 못하였다.
<br>

#### 그래서 Main model의 성능을 높이기 위해서 이상한? 방법을 사용해 보았는데 먼저 Undersampling으로 5-fold 1 epoch으로 학습시킨 후 해당 모델을 다시 5-fold 1 epoch으로 한 번더 학습시켜줬더니 그전보다 더 좋아졌지만 성별부분에서 아직 학습이 잘 안되는 것 같았다. 이 부분에 대해서는 다른 방식으로 접근해서 해결해 볼 생각이다.

<br>

#### 오늘도 고생많았고 내일도 화이팅해보자~!!!
