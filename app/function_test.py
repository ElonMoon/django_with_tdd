from selenium import webdriver
import os
import unittest

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME_DRIVER = os.path.join(ROOT_DIR, '.utils')


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome(CHROME_DRIVER+'/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 에디스(Edith)는 멋진 to-do 애플리케이션이 나왔다는 소리를 듣고
        # 해당 홈페이지를 확인한다
        self.browser.get('http://localhost:8000')

        # 그녀는 해당 페이지의 제목(title)과 헤더(header)가 to-do 리스트인 것을 알고 있다
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 그녀는 바로 to-do 에 작업을 추가한다

        # 그녀는 텍스트 박스에 '공작 깃털 구매'라고 적는다
        # (에디스의 취미는 루어낚시다)

        # 그녀가 엔터를 입력하면, 홈페이지가 갱신되고
        # 페이지 리스트에 "1: 공작 깃털 구매"라는 아이템이 to-do 리스트에 추가된다

        # to-do 작업을 추가할 수 있고
        # 그녀는 "루어 만들 때 공작깃털 사용"이라 입력한다

        # 홈페이지는 갱신되고, 두 to-do 아이템 목록이 보여진다

        # 에디스는 그녀의 to-do 목록이 사이트에 기록되는지 궁금해한다
        # 홈페이지는 고유한 URL 생성한다
        # URL 에 대한 설명문이 있다

        # 그녀는 해당 URL 에 접속한다 - 그녀의 to-do 목록은 아직 존재한다

        # 그녀는 만족하고 자러 간다


if __name__ == '__main__':
    unittest.main(warnings='ignore')
