<!--
구조
*
    *
        * <br>
            &nbsp; - &nbsp;  <br>
                &nbsp;&nbsp;&nbsp;&nbsp; ‣ &nbsp;  <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * &nbsp; <br>
-->

# day22

## 목차 



<!--4. [흥미있던 질문들](#4-흥미있던-질문들)-->

1. [학습 회고](#1-학습-회고)
2. [피어세션](#2-피어세션)


----


### 1. 학습 회고

#### pycharm에 관해서는 해결하지 못해서 이번에는 멘토님에게 slack DM을 보내봤다. 그래도 해결하지 못했다 ㅠㅠ
<br>

#### 어제 만들고 있던 id를 통한 train, vaild를 나누는 것을 완료하였고 1 epoch으로 실험할때 성공적이었지만 2 epoch이상일때는 dataloader부분에서 error가 발생하였다 ㅠㅠ
#### 이 부분에 대해서 많은 시간을 투자하였지만 해결하지 못했고 결국 남은 시간동안 다른 코드를 추가하지 않고 Efficient-b7과 피어세션대 다른 캠퍼님이 말해주신 data augmentation을 이용해서 프로그램을 돌리는 중이다.

<br>

### 2. 피어세션

*20210901 피어세션

🔍[마스크 데이터 분류 대회]

* Focal Loss에서 weight의 역할
* Loss function에서의 retain_graph
 

📒[데이터 전처리]

* FaceDetection을 통해 전처리된 데이터에서 좋은 결과를 얻었음.
* CutMix를 활용하여 학습 진행해봄.
 

📎[DataLoader]

* 전이학습 시 레이어 파라미터 변경 문제 → __repr__에만 반영되고 실제 모델에는 반영되지 않는 것으로 생각됨.
* mask, gender, age클래스를 나누는 방법에 대해 논의해 봄.
* 데이터 로드 시 Shuffle 옵션이 제대로 동작하지 않는 것을 확인했고, 이를 수정했을 때 모델 성능 개선이 되었음
 