"""
input
길이 n 인 리스트
1~ 100까지의 숫자로 이루어진 리스트
1~100까지의 숫자가 중복되어 랜덤하게 리스트를 구성하고 있음.
다만 이 리스트는 오름차순으로 정렬 되어있음.
ex)
[1, 1, 4, 78, 99, 100]
[1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 8, 8, 8, 9, 9, 10, 11, 12, 13, 14]
output
이 리스트 안에 1, 2, 3, 4, 5가 총 몇개있는지 출력하는 함수
재귀 함수 방식을 이용하여 함수를 완결하여 오시오.
"""


class Sample:
    FIRST = None
    LAST = None

    def count_number(self, test, 첫번째의_위치=None, 리스트의_마지막_요소의_위치=None):
        """
        :param test:  1~ 100까지의 숫자로 이루어진 리스트, 정렬이 되어있어
        :param 첫번째의_위치: 리스
        :param 리스트의_마지막_요소의_위치:
        :return:
        """
        if not 첫번째의_위치:
            첫번째의_위치 = 0
        if not 리스트의_마지막_요소의_위치:
            리스트의_마지막_요소의_위치 = len(test) - 1
        if 첫번째의_위치 == 리스트의_마지막_요소의_위치:
            return test.index(test[첫번째의_위치+1])
        mid = (첫번째의_위치 + 리스트의_마지막_요소의_위치) // 2
        check_list = [1, 2, 3, 4, 5]
        mid_번째_요소 = test[mid]
        if mid_번째_요소 in check_list:
            self.FIRST = mid + 1
            return self.count_number(test, self.FIRST, 리스트의_마지막_요소의_위치)
        else:
            self.LAST = mid - 1
            return self.count_number(test, self.FIRST, self.LAST)


input_1 = [1, 2, 3, 5, 8, 9]
output_1 = 4
s = Sample()
print(output_1 == s.count_number(input_1, 0, len(input_1) - 1))

input_2 = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 8, 8, 8, 9, 9, 10, 11, 12, 13, 14]
output_2 = 12
s = Sample()
print(output_2 == s.count_number(input_2, 0, len(input_2) - 1))

input_1 = [1, 2, 3, 5, 8, 9]
output_1 = 4
s = Sample()
print(output_1 == s.count_number(input_1, 0, len(input_1) - 1))
input_1 = [1, 2, 3, 5, 8, 9]
output_1 = 4
s = Sample()
print(output_1 == s.count_number(input_1, 0, len(input_1) - 1))


