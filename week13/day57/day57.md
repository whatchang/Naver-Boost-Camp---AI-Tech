<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp; <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# Day 

## 목차 

1. [공부한 내용 정리](#1-공부한-내용-정리)

2. [진행중인 실험](#2-진행중인-실험)

3. [학습 회고](#3-학습-회고)

## 1. 공부한 내용 정리

논문 읽기 - Latent Retrieval for Weakly Supervised
Open Domain Question Answering



<br>

## 2. 진행중인 실험

DPR 모델 customizing하는 실험 - [github issue](https://github.com/boostcampaitech2/mrc-level2-nlp-04/issues/26) -> 끝

새로운 실험 - [not in-batch, random sample(use elasticsearch) train 방식](https://github.com/boostcampaitech2/mrc-level2-nlp-04/issues/36)

<br>


## 3. 학습 회고

DPR 모델 customizing하는 실험

커스텀 모델 성능이 말도 안되게 매우 안 좋았다. 이 부분은 대회 끝나면 원인을 파악해 봐야겠다(지금은 성능을 올리는 것에 좀 더 집중하려고 한다).

새로운 실험으로 elasticsearch의 BM25로 negative sampling을 만들고 이것을 not in-batch의 random 방식으로 학습시켜보려고 한다. 이전에 DPR 구현에서 실패를 하였지만 해당 원인이 transpose의 문제였다는 것을 토론게시판 글을 보고 알게 되었다. 그래서 이 점을 참고해서 구현해 볼 생각이다.

해당 실험의 기대 효과는 in-batch 방식이 아니다 보니 여러 samples 중에서 positive sample을 찾도록 만들 수 있기 때문에 학습 난이도가 올라가서 결과적으로 좋은 성능의 모델을 만들 수 있지 않을까 싶다.

<br>