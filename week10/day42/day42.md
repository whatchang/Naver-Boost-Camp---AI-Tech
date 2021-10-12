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


2. [과제 정리](#2-과제-정리)



3. [피어세션 정리](#3-피어세션-정리)



4. [학습 회고](#4-학습-회고)

## 1. 공부한 내용 정리
* KLUE 강의 - 8강 듣기 <- 정리 추후에 할 예정
<br>

* KLUE 대회 관련 
    * 모델 커스텀 완료(pre-trained모델에 convolution layer + linear layer 추가 완료) -> But GPU 메모리 부족 현상이 나타남(batch size를 2로 줄이고 output size도 줄였는데도;;;).
    * 모델 커스텀 하면서 모르는게 여러게 생김
        * convolution 연산이 그렇게 많은지?
        * 참고용 code에서 중간중간에 mean을 해준 이유? 

                ex)
                 h = torch.stack([self.dropout_bert_stack(x) for x in x[-4:]]).mean(dim=0) 
        
                또는 

                z = self.cnn(h.transpose(1, 2)).mean(2)

        * 참고용 code에서 왜 다음과 같이 해주었을까? -> 해당 내용을 알기 위해서는 참고용 code의 데이터 셋과 다른 코드부분들을 봐야할 것 같다.

                x = torch.sum(h * attention_mask[..., None], dim=1)  # (B, L, 768) * (B, L, 1) -> (B, 768)
                x /= torch.sum(attention_mask, dim=-1, keepdim=True)  # (B, 768) / (B, 1) -> (B, 768)

<br>

## 2. 과제 정리
없음

<br>

## 3. 피어세션 정리

* 참석자
    * 김신곤, 김재영, 박세진, 손희락, 심우창, 이상준, 전상민

* 주간 일정
    * 화: 데이터 제작 투표, 대회 관련 논의
    * 수: RoBERTa 논문 리뷰, 대회 관련 논의
    * 목: 대회 관련 논의
    * 금: 강의 리뷰

* 강의 일정
    * 8강 GPT 언어모델
    * 9강 GPT 언어모델 기반의 자연어 생성
    * 10강 최신 자연어처리 연구

* 멘토링
    * 대회 관련 질문

* 대회 관련
    * no label 비율을 줄여서 MLM모델을 추가로 학습
    * Loss 함수를 다양하게 적용해보기
    * hyperparameter search를 통해 최적의 파라미터 찾기
    * CNN layer추가하여 성능 확인해보기
<br>

## 4. 학습 회고

* gpu 메모리 부족으로 인해 커스텀한 모델을 사용해보지는 못했지만 그래도 구현한 것으로 매우 만족한다 ㅎㅎ
* 왜 메모리 부족이 발생한 것인지는 내일 멘토링시간에 질문해야 겠다.
<br>