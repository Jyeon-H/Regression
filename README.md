# 보행성 점수 예측 및 특징 분석
본 레퍼지토리는 기존 연구의 재현 실험을 바탕으로 진행된 논문 프로젝트입니다. 
<br><br>

## 💬 개요
이미지 시각 정보 기반 보행성 점수를 예측하는 회귀 모델 개발 및 특징 중요도를 활용한 모델 해석 가능성 확보
<br><br>

## 📌 목표
- 주관적 판단에 의존하지 않는 정량적 보행성 평가 기준 수립
- 세그멘테이션 기반 특징 추출 및 회귀 모델 학습
- SHAP 기법을 통한 특징 중요도 분석 및 성능 변화 분석
- SCI(E) 등재 학술지 (MDPI Applied Sciences)에 논문 게재
<br><br>

## 🙋🏻‍♀️ 수행 역할
- **기존 연구의 코드 재구현 및 실험 환경 재구성**
- MMSegmentation을 활용한 이미지 세그멘테이션 과정 구현
- 회귀 모델의 성능 평가 및 특징 중요도 해석
- 실험 결과를 바탕으로 논문 작성 및 제출
<br><br>

## 🗂️ 데이터
- **구성** : 21,168장 거리 이미지 및 각 이미지에 해당하는 보행성 점수 (0-100)<br>
- **특징 추출** : ADE20K로 학습된 UperNet을 사용한 150개 클래스 추출 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 클래스별 영역 비율을 회귀 모델의 입력으로 변환
- **출처** : 사전 연구를 통해 수집된 데이터로, 외부 공개는 제한됩니다.
<br><br>

## 🔍 모델 및 방법
- **주요 기술** : Python, TensorFlow, scikit-learn, MMSegmentation, XGBoost, SHAP
- **세그멘테이션** :
  - ADE20K로 사전학습된 UPerNet
- **회귀 모델** :
  - MLP
  - Ridge
  - Lasso
  - SVR
  - XGBoost
- **평가 지표** :
  - MSE
  - MAE
  - RMSE
  - R2
  - Accuracy
- **해석 기법** :
  - SHAP (SHapley Additive exPlanations) 기반 특징 중요도 분석 <br>
  - 상위 66개 특징 중 30개부터 66개까지 2개 단위로 점진적 추가
  - 총 33개 조합에 대해 모델 성능 비교
- **연구 흐름도**
  ![Figure1](https://github.com/user-attachments/assets/b5bbf09a-f6ed-4f54-8486-b5b641d3674e)
  <br><br>

## 📊 주요 결과
- 세그멘테이션 결과 예시
<img width="700" height="350" alt="seg1" src="https://github.com/user-attachments/assets/e3c40225-4299-4bfd-ba31-2c9b9b22d21d" />
<img width="700" height="350" alt="seg2" src="https://github.com/user-attachments/assets/0adb8ad2-b06b-4e5f-ad73-5400925ee1ef" />

- SHAP 기반 상위 중요 특징 (Top 5)
  |Rank|MLP|Ridge|Lasso|SVR|XGBoost|
  |---|---|---|---|---|---|
  |1|building|road|road|sidewalk|road|
  |2|tree|sidewalk|sidewalk|road|building|
  |3|sky|sky|tree|building|sky|
  |4|road|building|sky|sky|sidewalk|
  |5|car|car|flag|tree|tree|
- XGBoost 결과 기반 시각화
  - 클래스별 중요도 (Top 15)
  <img width="400" height="300" alt="XGBoost회귀모델" src="https://github.com/user-attachments/assets/9c28715a-1450-4948-82f8-7da72e3db671" />

  - 특징 개수에 따른 성능 변화
  <img width="700" height="200" alt="Figure6" src="https://github.com/user-attachments/assets/176e30e4-7275-4999-aa81-953c65c0bbc4" />


## 🔁 회고
기존 연구 코드를 스스로 재구성하며 전반적인 흐름을 이해하였고, 논문 작성을 병행하며 결과 정리 및 커뮤니케이션 능력을 향상시켰습니다. <br>
세그멘테이션, 특징 추출, SHAP 등 다양한 머신러닝 해석 기술을 적용하며 실무 경험을 강화하였습니다.
