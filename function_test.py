import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    #text_문자열로 시작하면 자동실행
    def test_can_start_a_list_and_retrieve_it_later(self):
        # 영애씨는 온라인 일정관리 앱을 알게 되어 홈페이지에 방문한다.
        self.browser.get('http://localhost:8000')

        # 홈페이지에 방문해 보니 제목이 "일정관리"인 것을 보고 홈페이지에 올바르게 방문한 것을 확인한다.
        # assert '일정관리' in self.browser.title, "Browser title was " + self.browser.title
        self.assertIn('일정관리', self.browser.title)
        self.fail('테스트 종료')
        self.tearDown()

        # 일정을 입력할 수 있는 페이지로 바로 이동한다.

        # 영애씨는 생일날 미역국을 끓이기 위해 텍스트박스에 "시장에서 미역 사기"를 입력한다.
        # 영애씨가 엔터를 입력하면 페이지를 새로고침해서 모든 일정 목록을 보여준다.
        # "1: 시장에서 미역 사기"가 첫 번째 할일로 일정 목록에서 보여진다.

        # 영애씨는 추가로 할일 텍스트박스에 입력할 수 있고
        # "미역을 물에 리기"라고 입력한다.

        # 다시 페이지를 새로고침해서 입력한 일정 두 가지 모두 목록에 표시한다.

        # 영애씨는 일정 목록이 사이트에 올바로 저장되었는지 궁금해서
        # 고유 URL 생성을 확인한다.

        # 영애씨는 URL을 방문하고 일정 목록이 올바르게 있음을 확인한다.

        # 영애씨는 이제 만불족하고 잠을 자러간다.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
