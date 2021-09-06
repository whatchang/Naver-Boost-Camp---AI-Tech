<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp;  <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp;  <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# day24

## 목차 



<!--4. [흥미있던 질문들](#4-흥미있던-질문들)-->

1. [학습 회고](#1-학습-회고)
2. [피어세션](#2-피어세션)


----


### 1. 학습 회고

#### 오늘은 competiton이나 공부를 하지 않았고 이때까지 한 것에 대해서 회고록 작성 및 wrap-up report를 팀원들과 함께 작성하였다. 
#### wrap-up report는 다 작성하지 못해서 내일 저녁7시에 다시 모여서 하기로 하였다. 음... 이제 곧 해어지니까 뭔가 많이 아쉽다 ㅠㅠ
#### Competition은 결과적으로 public에서는 23등 private에서는 22등으로 최종 22등을 했다.
#### 결과는 비록 좋은 편은 아니지만 이번 competiton을 통해서 많은 것을 느꼈고 다음에는 어떤 자세/관점/방식으로 참여할지 감이 잡힌 것 같다.
<br>

#### 다음번에 Competiton 임할 자세
1. EDA <- 매우 중요, 이것을 통해서 문제 상황 파악, train data 파악, 어떻게 학습 및 전처리를 할 지 고민하는 단계
2. pretrained model 사용시 해당 모델의 특징들을 제대로 알고 사용하기 -> model에 따라서 data augmentation 방식이 성능에 영향을 줄 수 있다. <- 이번 Efficient-b7보다 DenseNet191, ResNext 등이 똑같은 data augmentation시 성능이 더 좋았다.
3. 등수보다는 가설을 세우고 검증하는 것에 집중하기
4. 가설과 그에 해당하는 결과를 잘 기록해두기(이때 시각적인 자료들이 있으면 좋음 <- tensorboard나 wandb)

<br>



### 2. 피어세션

* 20210902 피어세션

🔍[마스크 데이터 분류 대회]

* cosine annealing 
    * cosine annealing에서 max와 min을 지정해줄 수 있다.
    * 범수님 : 기존과 비교했을때 성능에 큰 영향을 주지 않았음.
    * 성욱님 : 기존에서는 정확도가 80% 대이었는데 적용이후 90% 대로 향상되었다. 
* 오늘은 피어세션을 짧게 하고 대회 막바지에 집중하기로 하였다.