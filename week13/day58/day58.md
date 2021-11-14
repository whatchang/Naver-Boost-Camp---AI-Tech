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

없음

<br>

## 2. 진행중인 실험

[not in-batch, random sample(use elasticsearch) train 방식](https://github.com/boostcampaitech2/mrc-level2-nlp-04/issues/36)

<br>


## 3. 학습 회고

elasticsearch의 BM25를 이용하여 유사한 sample set을 만드는 중이다.
그런데 약간의 전처리가 필요한 것 같다. positive와 같지 않은 유사한 negative sample을 수집하기 위해서 postive인 경우 filteringㅇ르 해주는 코드를 단순하게 in 키워드를 사용하여 구현했는데 중간중간에 똑같은 내용이지만 context 중간의 개행들이 추가되어 filtering이 잘 안되는 부분들이 있어서 이 부분을 해결하는 중이다. 

<br>