import cv2
import os

# 이미지 저장 폴더 생성
if not os.path.exists('version1'):
    os.makedirs('version1')

# 100개의 이미지 생성
for i in range(100):
    # 이미지 생성
    image = cv2.imread('sample/image.png')

    # 사각형 좌표 설정
    start_point = (i % 10 * 50 + 50, i // 10 * 50 + 50)  # 사각형의 시작 좌표
    end_point = (i % 10 * 50 + 200, i // 10 * 50 + 200)  # 사각형의 끝 좌표

    # 사각형 그리기
    color = (23, 125, 255)  # 사각형의 색상 BGR
    thickness = 10  # 선의 두께
    image_with_rectangle = cv2.rectangle(image, start_point, end_point, color, thickness)

    # 이미지 저장
    cv2.imwrite(f'version1/image_{i + 1}.png', image_with_rectangle)