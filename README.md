# 치네아카 CINEACCA 

이탈리아 학생 단편영화 스트리밍 플랫폼🎬  
Italian student short film streaming platform  

https://cineacca.com

인스타그램
https://www.instagram.com/cineacca/  

## 💻개발 언어 및 환경 Languages

Frontend : JavaScript, HTML, SCSS  
Backend : Django🐍

## ⏱개발 기간 Development period
  
2021년 7월 31일 ~ 2021년 12월 28일 (약 5개월)  
July 31, 2021 ~ December 28, 2021  
  
## 🔍현재 상태 Current State  
  
🟢 서비스 중  
Now available  


## 📝 개발 후기 Development Reviews


### 아이디어와 서비스 기획 Idea and planning service

다니던 영화학교 친구들이 졸업을 앞둔 시점에서 기념할 수 있는 졸업작품 전시회 같은 웹사이트를 목표로 시작했다. 
그리고 개발 과정에서 아이디어를 확장시켜 영화를 공부하는 학생들이 자신들의 단편 영화 작품을 다른 학생들이나 대중에게 보여주고 평가와 의견이 오가는 공간을 만들어보면 꽤 근사할 것 같았다. 
대부분의 이런 학생들은 자신만의 Youtube 채널을 이용하고 있는데 당연히 노출될 기회도 적고, 자신과 비슷한 활동을 하고 있는 학생들을 찾기도 어렵다. 
하지만 학생 영화를 전문적으로 다루는 서비스라면 그들의 작품들이 플랫폼에서 주목받기 더 쉬울 것이고 결과물에 대한 질 높은 피드백들이 오갈 수 있을 것이라 생각했다.
그렇다면 학생들에게 자신의 분야에 대한 자극과 동기부여 그리고 평가와 성장의 공간으로서 Youtube나 Vimeo 보다 더 매력적인 플랫폼이 될 수 있을것이다.
또한 뿐만 아니라, 전문 종사자들에게도 필드의 미래를 엿볼 수 있는 아주 흥미로운 공간이 될 수 있지 않을까 생각했다.

### 개발 과정에서의 문제 Problems & solution in development

- 비디오 압축 Compress video   
  Video file upload 는 가장 힘든 파트 중 하나 였다. Django로 file upload 를 구현하는 것은 간단하지만, 문제는 다루는 파일이 그리 간단하지 않다는 것에 있다. 서비스는 짧은 비디오가 아닌 대게 최소 10분 이상의 비디오 파일을 다루게 될 것이다. 용량이 굉장히 클 것이고 이 비디오 파일을 압축하는 과정이 필요했다.압축에는 ffmpeg를 사용했고 로컬에서 시험하며 모든 비디오에 적용될 수 있는 적절한 압축 조건을 찾았다. 압축은 빨랐고 결과물도 아주 좋았다. 하지만 product 에서 나의 Heroku 서버는 아주 작은 비디오 압축에서조차 이 프로세스를 버텨내지 못했다. 나는 티어가 높은 서버의 사용료를 지불할 수 없었으므로 Nomad Coder애서 Youtube 클론 수업에서 다뤄봤던 ffmpeg wasm을 사용하기로 했다. 즉, 서버 리소스 대신에 브라우저에서 유저의 컴퓨터로 압축을 진행하는 것이다. 이 과정에서 많은 시행착오가 있었던 것 같다. 이렇게 하면 시간이 훨씬 더 오래 걸린다는 단점이 있지만 내게 주어진 조건에서는 최선의 방법이었던 것 같다. 이 경우 유저가 업로드한 파일을 백엔드에서 처리하는게 아니기 때문에, 프론트에서 압축된 파일을 input에 올라온 원본 파일과 교체해야했는데 File 객체를 생성하여 컨버팅된 파일을 담고 이것을 dataTransfer 를 통해 input으로 넣어주었다.
  
  
- 배포 그리고 공포의 과금사태 Deploy and unexpected charges  
  처음으로 AWS 배포에 도전했다. 생소한 개념들이 많아서 굉장히 혼란스럽고 어려웠다. EC2, S3, RDS를 이용하여 겨우 배포했는데, upload file을 처리할때 Nginx Request Entity Too Large 에러가 났다. 검색해보니 Nginx의 기본 설정 때문이었고 수정이 가능했다. 그리고 여러가지 작동 시험을 하며 그렇게 1주일 정도가  지났는데 doc을 읽다가 우연히 내가 선택한 티어가 과금이 된다는 사실을 알게 되었다. 지불내역을 보니 약 30만원 가량이 청구 되어있었다. RDS에서 돈이 무지막지하게 빠져나가고 있었는데 왜인지는 모르겠지만 내가 선택한 밀라노 리전에서는 다시 확인해봐도 프리티어 옵션이 없었다. 부랴부랴 모든 것을 삭제하고 Heroku에 재배포하기로 했다. Heroku 배포는 훨씬 더 간단했으며 더 저렴했다. 스토리지는 S3 대신에 GCS를 선택했다. 과금은 다행히 AWS측에서 잘 해결해주었다.


### 배포 이후의 문제 Problems & solution in product

- 비디오 압축 과정에서의 좋지 않은 유저경험 Bad UX in the video compression process  
  서비스 오픈 후 공통된 의견 중 하나는 압축과정에서 시간이 너무 많이 걸린다는 것이었다. 하지만 서버를 이용한 압축을 할 수 없었지만 적어도 유저가 얼마나 더 기다려야하는지 모른채로 답답해하지 않도록 Upload Form에서 압축이 시작되면 Progress Bar를 추가해 진행도를 보여주었고 이제 한결 낫다는 반응이긴 했다. 하지만 진짜 근본적인 문제는 ffmpeg/wasm 을 사용하는데 있다. 서버가 아닌 유저의 브라우저에서 하는 대용량의 압축작업은 서버에서 이루어지는 것보다 느릴뿐만 아니라  유저의 컴퓨터 환경, 인터넷 연결 상태  등 여러가지 변수에 크게 영향을 받게 되고 결국은 이는 유저마다 각기 다른 사용경험을 가지게 만든다.

- 서버의 한계 Limitations of Heroku servers  
  간혹 비디오 압축 과정이 끝나고 Form을 submit하면 App이 crash 되면서 upload에 실패하는 문제들이 보고 되었다. H13 에러였고 request 시간 초과로 인한 문제였다. Heroku는 30초 이상이 걸리는 연결에 대해서 자동으로 중지시켜버린다. upload의 요청시간은 파일의 용량이나 인터넷 상태에 따라서 달라질 수 있고 가뜩이나 인터넷이 빠르지 않은 이탈리아에서는 최종 파일의 용량이 그리 크지 않은데도 30초 이내 request가 처리되지 못하고 업로드가 실패하는 경우가 많았다.
  문제 해결을 위해 검색을 하며 redis, salary 등을 통한 비동기처리를 하면 되지 않을까 생각했다. 즉, 업로드 작업을 30초 제한과 상관없이 백그라운드에서 수행하여 완료할 수 있지 않을까 싶었지만 예상처럼 작동하지 않았고 30초 룰은 이것과는 상관이 없다는 것을 알게 되었다. 결국 AWS나 GCS로 다시 이전하는 것이 유일한 방법인데, DB를 dump하고 restore하는 과정을 해결하지 못하고 있다.


### 이 프로젝트를 통해 배운 것 So What I learn

- 개발이 어떻게 이루어지는지 전반적인 과정을 이해할 수 있었다. 다음부터는 더 계획적이고 체계적으로 개발을 진행할 수 있을 것 같다.
  
- Django와 Python 그리고 javascript 사용에 많이 익숙해졌다. 클론 코딩에서 배운 것들을 토대로 직접 프로젝트를 구현하다보니 Django의 패턴들이 점점 눈에 들어오기 시작했다. 클론 코딩에서 해보지 않았던 것들을 직접 찾아 배워야하는 경우도 많아서 전보다 Python과 Django에 대한 이해도가 좀 더 넓어진것 같다.

- gulp를 이용한 빌드 자동화를 이해하고 다룰 수 있다.
    
- 리뷰의 CRUD를 구현하면서 비동기 통신을 이용한 API 요청과 처리를 이해할 수 있게 되었다.
    
- AWS와 Heroku 에 배포를 하면서 배포 과정 전반을 경험해볼 수 있었다. Heroku의 요청시간 30초 제한 문제를 겪으며 AWS와 Heroku가 어떻게 다른지에 대해서도 알게 되었다.
  
- Document 읽기와 정보 검색에 익숙해졌다. 내가 배우지 않은 것을 검색해서 습득하고 적용할 수 있게 되었다. 왜 검색도 실력이라는 말의 의미를 알 것 같다.
  또 doc에서 원하는 정보를 찾아내는 일도 점점 수월해졌다. 프로젝트 후반부로 갈수록 Slack 채널 등에 질문을 하기전에 문제의 원인과 해결책을 혼자서 찾아내는 경우가 많아졌다.

  
### 반성점 reflection
  
- 더러운 코드  
  구현에만 집중하다보니 유지보수하기 어려운 코드가 되었다. 리팩토링을 어떻게 해야하는지도 잘 모르고 있다.
  이 부분에 대해서 많은 공부가 필요할 것 같다. 다음부터는 코드의 질을 높이는 데에도 많은 노력을 기울이고 싶다.

- 부족한 기초지식  
  기본기와 기초 지식이 너무 부족한 것 같다. 개발과정 중의 문제를 해결하는 과정에서 생소한 개념들을 많이 마주쳤고 결국 잘 이해하지 못하고 넘어간 것도 많다. CS나 웹 기본지식 등을 함께 공부할 필요성을 느꼈다. 
  
- 로그를 남기자  
  결코 작지 않은 프로젝트였고 문제들에 가로막힌 순간도 많았는데 해결 자체에만 급급했던 것 같다. 어떤 문제를 만났고 원인은 어디에 있었으며 그것들을 어떻게 해결했는지 기록으로 남겼더라면 해결 과정에서 더 많이 생각하고 공부할 수 있었을텐데 하는 아쉬움이 든다. 이제와서 리뷰를 한꺼번에 남기려니 겪었던 과정들에 대한 기억이 가물가물하다..ㅠㅠ 다음 프로젝트부터는 개발 기록을 남겨서 경험에서 최대한 많은 것들을 이끌어낼 수 있도록 하고 싶다.
