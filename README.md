# myCrawler

패키지 링크: https://pypi.org/project/my_crawler/0.0.1

깃허브 레퍼지토리: https://github.com/JeonChaeHwan/myCrawler

다운로드: pip install mywab

사용방법: from my_crawler import mycrawler as mc

저는 1학년 때 파이썬을 사용하는 수업들에서 bs4의 beautifulSoup와 requests를 사용해 웹 크롤링을 하는 방법을 배우면서, 웹 크롤링의 복잡성(HTML 구조를 파싱하고, 데이터를 추출하는 등의 작업이 필요함)을 느끼게 되었습니다. 이를 완화하고자 둘을 import해 myweb를 만들게 되었습니다.


1. get_html(url):
  URL로부터 HTML을 가져오고, 에러 발생 시 에러 코드를 출력한다.

2.parse_html(html):
  html을 파싱한다.
  
3. extract_text(soup, selector):
특정 텍스트를 추출한다.

4. extract_links(soup):
  모든 링크를 추출한다.
