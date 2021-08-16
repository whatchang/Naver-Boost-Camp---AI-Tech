# weekend 3-monday 

## 목차 

1. [학습 회고](#1-학습-회고)
2. [Transformer에 대한 궁금한 내용](#2-Transformer에-대한-궁금한-내용)
3. [보충 공부할 내용](#3-보충-공부할-내용)

----

### 1. 학습 회고

*  유튜버 나동빈님의 Transformer에 대한 논문 리뷰를 시청했다. 전반적으로 저번주에 공부했던 Transformer와 겹치는 부분이 많았기 때문에 이해가 잘 되었지만 중간중간에 '뭐징?", "????" 하는 부분이 있었다. 이 부분에 대해서는 아마도 기초적인 배경지식이 부족해서 그러지 않나 싶다. 그리고 궁금한 것들도 생겼다. 이것에 대해서는 밑에다가 정리할 생각이다. 

* 원래는 논문 리뷰를 보고 블로그 글을 통해서 추가로 공부하고 다시 논문 리뷰 보려고 했는데 게을러서 논문 리뷰 1회 시청밖에 못했다 ㅎㅎ;;; 반성하자😫



### 2. Transformer에 대한 궁금한 내용
* decoder에서 encoder에서 나온 key/value vector와 decoder의 query vecoter를 이용하여 multi-head attention과정을 수행한다. 결국 이러한 과정은 우리가 원하는 언어(K)로 번역하는 과정에서 A라는 단어를 K라는 언어의 단어로 바꿀때 얼마나 적합한지?를 계산하는 과정이라고 이해를 했는데 이 부분에서 잘 이해가 안된다. encoder(다른 언어에서)의 key/value vecoter가 decoder(우리가 번역하고자 하는 언어)의 query vector간의 상관관계? 부분이 잘 이해가 안된다. <- 아!!! 정리하다 보니까 궁금증이 해결되었다 ㅎㅎ;; <br> 학습을 통해서 각 query/key/value vector를 구하기 위한 weight 값들이 학습이 되면서 A라는 단어가 K언어에서 적합한 의미를 가진 단어로 출력이 될 것 같다.

### 3. 보충 공부할 내용
* 코드 구현 부분
* residual 부분
* 디테일한 부분에 대해서(왜 이렇게 해주었는지, 어떤 과정으로 다음과 같이 되었는지)
* [참고할 사이트 1 - KLP in korean](https://nlpinkorean.github.io/illustrated-transformer/)
* [참고할 사이트 2 - 딥러닝을 이용한 자연어 처리 입분(위키독스)](https://wikidocs.net/31379)
* [반복해서 시청할 영상 - Transformer논문 리뷰](https://www.youtube.com/watch?v=AA621UofTUA&list=PLRx0vPvlEmdADpce8aoBhNnDaaHQN1Typ&index=8)
