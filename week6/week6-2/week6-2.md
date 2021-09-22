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

2. [학습 회고](#2-학습-회고)

## 1. 강의내용 정리

이전에 삽질했던 'LSTM은 완벽하게 gradient vanishing/exploding 문제를 해결했는가'를 정리하던 중 여러 자료를 더 찾았고 그것을 보면서 이전에 이해안 되었던 부분에 대해서 좀 더 이해하려고 노력하였다. 그렇지만 결국 내용 정리는 다 끝마치지 못했다 ㅠㅠㅠㅠ

참고한 블로그 
[한국 블로그1](https://wegonnamakeit.tistory.com/7) <- input/output weight conflict에 대한 내용이 있다. <br>
[한국 블로그2](https://ratsgo.github.io/natural%20language%20processing/2017/03/09/rnnlstm/) <- LSTM의 전반적인 내용 + backpropagation에 대해서 잘 나온 것 같음 + 유용한 댓글도 많다. but backpropagation에서 의문이 드는 내용이 있다(ht에 대해서 backpropagation을 설명하는게 아니라 ct에 대해서 설명하는 점).<br><br>

[외국 블로그1](https://stats.stackexchange.com/questions/185639/how-does-lstm-prevent-the-vanishing-gradient-problem) <- gradient vanishing문제를 어느정도 해결할 수 이유에 대해서 설명(ht = ot ⊙ ct이므로 이때 ot는 gradient vanshing으로 gradient값이 없더라도 ct에 대한 gradient가 살아남아서 이것이 ht-1에 전달된다는 내용) + 이와 관련된 논문 추천해줌([1] Pascanu, Razvan, Tomas Mikolov, and Yoshua Bengio. "On the difficulty of training recurrent neural networks." ICML (3) 28 (2013): 1310-1318.<br>[2] Bayer, Justin Simon. Learning Sequence Representations. Diss. München, Technische Universität München, Diss., 2015, 2015.)<br>
[외국 블로그2](https://www.quora.com/How-does-LSTM-help-prevent-the-vanishing-and-exploding-gradient-problem-in-a-recurrent-neural-network) <- 각 gate의 outputdl 1보다 클 수 없으므로 gradient exploding문제가 발생하지 않는다고 설명해줌<br>
[외국 블로그3](https://www.reddit.com/r/MachineLearning/comments/34piyi/why_can_constant_error_carousels_cecs_prevent/) <- 여기서는 위의 외국 블로그2의 반박되는 내용이 있다. 여기서는 vanishing문제는 블로그1와 같이 해결이 되었지만 gradient exploding은 2가지 갈래길(ot, ct)중에서 한쪽에서 exploding이 있다면 즉 값이 점점 커진다면 이것은 전체 gradient도 exploding된다고 함. <- 여기서 의문점이 gradient가 증가할 수 있는 구조인가?라는 의문점이 들었다 + 아래 또 다른 댓글에서도 나와 같은 생각을 함(그런데 답변이 없었다 ㅠㅠ).<br>
<br>

#### 논문<br>
- [1]S.HochreiterandJ.Schmidhuber.Longshorttermmemory.Neuralcomputation,9(8):1735–1780,1997. <- LSTM 원본 논문, LSTM이 해결하고자 한 문제 + 접근 방식 + core idea + LSTM 한계 + forward/backward flow를 수식으로 설명해준다. BUT 나의 영어 실력 + 수학 실력 부족 ㅠㅠㅠㅠ -> 그래서 이해하지 못함 + 다 못 읽음
- [2]Pascanu, Razvan, Tomas Mikolov, and Yoshua Bengio. "On the difficulty of training recurrent neural networks." ICML (3) 28 (2013): 1310-1318. <- [논문 정리한 것](../week8/week8-1/week8-1.md)
- [3]Bayer, Justin Simon. Learning Sequence Representations. Diss. München, Technische Universität München, Diss., 2015, 2015. <- 아직 읽어보지 못함

<br>

#### 서적<br>
- [1] Deep Learning from Scratch2 (한빛미디어) <- LSTM의 ht를 구할때 ⊙(아다마르 곱hadamard product, 행렬곱이 아닌 원소곱을 뜻함) 덕분에 곱셈이 누적되는 효과가 발생하지 않아서 기울기 소실 혹은 exploding이 발생하기 어렵다고 나옴.

## 2. 학습 회고

#### 오랫동안 이 주제에 대해서만 삽질하고 다른 것에 정리 혹은 공부를 하지 못해서 불안하지만 만약 이것을 제대로 끝내지 못한다면 '나는 항상 제대로 끝내는게 없네... 내가 그렇지 뭐...'라는 식으로 나를 대할 것 같아서 이번만큼은 제대로 해보려고 한다.
#### 삽질하는 동안 힘들고 지치는 점도 있었지만 새로운 것을 깨닫거나 다른 접근법이 생각이 날때면 기분이 좋아져서 금방 회복된다.
#### 다음주도 삽질을 이어나가고 꼭 끝내서 slack에 공유해봐야겠다!!! 아자! 아자! 화이팅~!
#### 아! 그런데 부스트캠프 수업 + 과제가 더 중요한 일인것은 까먹지 말자!

<br>