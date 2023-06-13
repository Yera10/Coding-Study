import sys
input = sys.stdin.readline

# rstrip 필수.
# readline으로 입력받으면, 입력 후 Enter가 줄바꿈 기호로 입력되기 때문.
input_str = input().rstrip()
print(input_str)
