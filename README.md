# Regression Project 느낀점

### 결론

- 데이터 사이언스는 처리 순서보다는 **인사이트** 가 목적이다.
- 데이터 전처리(feature selection, remove outlier, Feature transformation)이 중요!!



### 데이터 컬럼 갯수에 대한 느낀점

- 데이터 컬럼이 많을 수록(대략 30개 이상) t-test, f-test 정확도는 떨어진다. 
  - 조건수가 높게 되어, weight 값 생성이 줄어든다.
- 데이터 컬럼이 많을 때에는 Lasso나 Ridge를 이용해 Regression을 사용한다.





### 카테고리에 대한 느낀점

- 카테고리가 많을수록 성능은 더 떨어질 수가 있다. 
  - 이유는 0과 1로만 이루어져 있기 때문에 numeric보다 다중공선성이 생길 확률이 매우 높다.
  - 이 문제를 해결하기 위해서는 treatment 기법을 활용(상수항 제거)하거나 feature embeding으로 카테고리를 카테고리로 변형해 주는 것이 좋다. 



### 다중공선성

- 다중공선성은 샘플의 오차에 따라서 웨이트 값이 크게 달라질 수 있기 때문에 발생한다. 
- 다중공선성 자체 때문이 아니라, 샘플이 많이 찌그려져 있기 때문에 역행렬을 구할 수 없기 때문이다. 그러므로 스케일이 매우 커도 샘플 오차는 심하게 생길 수 있다.
- numeric data은 스케일링(Scaling)을 통해 공선성을 줄일 수 있다.





### Feature Selection

- Regression에서 중요한 것은 어떤 데이터가 중요한 지 feature를 골라내는 것이다.(좋은 모델을 만드는 것이 아니라 인사이트를 확인하는 것이 목적이라면...)
- Feature Selection 방법 :
  - numeric data + categorical data :  PCA, Lasso, stepwise method 
  - numeric data : t-test를 이용한 p-value
  - categorical data : one-way ANOVA, ANOVA 분석 F-test

  ​



### Feature Transform, Outlier 제거

- 실제로 프로젝트를 진행했을 때, Transform과 Outlier 제거로 꽤 큰 성능을 얻었다. 실제로 성능을 높일 때에는 이 두가지로만 큰 성능을 얻어 낼 수 있다.
- Outlier 제거 방법 : (Cook's distance, leverage, pearson residual)  
  - Outlier는 모델을 만든 다음에 제거한다.
- Feature Transform : partical plot에서의 y와 x의 관계를 보고 선택이 가능하다.
  - log : skew가 높은 데이터
    - 타켓 데이터는 정규성을 띄어 주는지 확인.
    - log를 취하는 이유 : outlier를 제거하기 위해서 사용.
  - square : sqaure와 poly-nomial regression과 함께 이용도 가능하다.
  - 세제곱




### Missing Value Treatment

- regression에 의한 결측값 처리는 다중 공선성 때문에 좋지 않을 수 있다. 
- 제일 좋은 방법은 관련 있는 데이터를 보면서 넣어주는 방법 또는 최빈값을 넣어주는 방법
- 솔직히 missing value treatment는 성능에 큰 영향을 주지 않는다. 여기서는 결측값 처리 방법보다는 **결측값 존재 여부**가 더 중요하다.




### 데이터 특징의 갯수 없을 때

- 현재 진행한 House Price는 데이터 컬럼의 갯수가 많을 때 였다. 하지만 데이터가 없을 때에는 직접 데이터의 컬럼을 생성해 주어야 한다. 이 때는 **Domain지식**이 매우 필요하다. 





### 데이터 사이언스에 접근 방법에 대한 생각

- 처음 분석을 했을 때, 데이터를 분석하는 알고리즘에 대해서 고민을 많이 했다. 하지만 그렇게 분석할 때의 단점은 데이터에 자체에 집중하지 않고 데이터의 인사이트를 발견을 소홀히 하게 된다. 실제로 House-Price에서도 ''어떻게 데이터를 삭제할까?'로 접근했기 때문에 삭제하는 알고리즘 설계에 집중하고 데이터 자체는 많이 들어다 보지 않았고, 데이터 분석를 최종적으로 할 때에도 regrulized regression에서 모든 데이터를 얻었기 때문에 인사이트를 발견하기가 어려웠다. 
- 결국 데이터 사이언스에서 중요한 것은 성능보다는 **데이터를 통해 인사이트를 얻는 것**이다.  





### 교차 검증

- 데이터 샘플의 수가 적으면 교차 검증의 정확도가 매우 떨어진다. 그럴 때에는 K-fold의 K의 갯수를 늘려 여러 번 반복하는 것이 좋다.
- 실제로 했을 때에는 교차 검증으로만 테스트 성능을 확인할 수 있다.



