# Dynamic Programming

> - 큰 문제를 작은 여러개의 문제로 나누어 푸는 문제
> - 작은 문제가 반복되어 일어나는 경우
> - 최적화된 재귀
> - 다항시간에 문제를 해결하는 것 (?)

## DP 의 조건
> ### 1. 부분 반복 문제
> - 예) 피보나치 수열
> - 모든 문제를 부분 문제로 쪼갤 수 있고, 재귀 함수를 통해 해결할 수 있다. (?)
> ### 2. 최적 부분 구조
> - 작은 부분 문제에서 구한 최적의 답으로 합쳐진 큰 문제의 최적의 답을 구할 수 있다.
> 

## 구현방법
> 1. Bottom-up
> > - 작은 문제부터 구현
> > - 풀기 쉽지만, 가독성이 저하되는 단점
> 2. Top-down
> > - 큰 문제를 풀 때, 작은 문제가 풀리지 않았다면 그제서야 작은 문제를 해결
> > - 재귀함수로 구현하는 경우가 대부분 Top-down
> > - 가독성이 좋지만, 구현하기 어려운 단점

## DP 활용 방법
> - 문제에서 요구하는 답을 문장으로 표현한다.
> - 문장에 나와있는 변수 개수 만큼 메모를 위한 캐시 배열을 생성한다.
> - **문제를 부분 문제로 나누고, 점화식을 구하여 문제를 함수로 표현**한다.
> - Top-Down의 경우 재귀 함수, Bottom-Up의 경우 for문을 활용하여 답을 도출한다.

## 적용 (??)
> - Diff Utility (Longest Common Subsequence 문제 기반): 두 개의 파일의 차이점을 알아내기 위해 쓰인다. Git에서도 사용된다.
> - Resource Allocation(0-1 배낭knapsack 문제 기반)
> - 연관 검색어 검색 (Edit distance 문제 기반)
> - 플로이드-워셜 알고리즘Floyd-Warshall Algorithm: 그래프의 모든 정점의 쌍의 최단 거리를 찾아내는 알고리즘.
> - 벨만-포드 알고리즘Bellman-Ford Algorithm: source router와 destination router 사이 최단 거리를 찾아내는 알고리즘.

---
### References
https://www.hanbit.co.kr/media/channel/view.html?cms_code=CMS4008657032