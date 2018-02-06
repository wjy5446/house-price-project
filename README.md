# house-price-project

## 일정

- EDA ~2/19
- Feature Selection ~2/26
- Modeling ~ 3/4
- Upload ~3/5
- Presentation ~3/7




## 작업 방식

**제가 임시로 만들어 본 작업 방식입니다. 다른 좋은 작업 방식 있으시면 저에게 알려주세요 ^^**



- 각자 작업은 자신의 이니셜로 만들어 진 "**Branch (YJY, WBY, LDH)**"에서 "**각자 이름의 폴더**"에서  이루어진다.

- 작업 완료시에는 commit 내용은 다음과 같이 적는다. (대략적인 내용 + 자세한 내용(옵션)) 자세히 적으면 좋아요!

  ```
  Analysis the data.
  Analysis the "survived" column using the .describe()

  ```

- 각자 작업은 Fork를 이용해 자신의 작업공간에서 이루어진다. 



- 각자 작업이 완료되면 온라인/오프라인 회의를 통해 전체 프로젝트에 쓸 코드를 정한다.
- 회의를 통해 정해진 코드는 Master Branch에서 **Pull request**를 통해 메인 repo에 업로드한다. 


참고 : [Git을 이용한 협업 워크플로우 배우기](http://blog.appkr.kr/learn-n-think/comparing-workflows/)




### Branch

- master



### 폴더이름

- LeeDohaeng : 이도행님의 작업공간

- WangBoyun : 왕보연님의 작업공간

- YoonJaeyoung : 윤재영님의 작업공간

- Total : 전체 팀의 작업공간

- data : Home-price가 data 정보가 있는 곳

  ​

## 주의사항

- 작업 시작 전에 `git checkout 자신branch`로 변경한다.
- 메인 repo에 변경사항이 있는 경우, 메인 repo와 동기화 한다. (메인 repo 변경 사항이 있는 경우, 슬랙  DM를 통해 알려 드립니다.^^)




## 메인 repo와 동기화하는 방법

1. `git fetch upstream`
2. `git merge upstream/master`
3. `git merge upstream/자신의브랜치`


