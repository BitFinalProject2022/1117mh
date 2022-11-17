import numpy as np
from rembg import remove
import cv2
import tensorflow as tf
import os
import glob
from PIL import Image
import PIL
import matplotlib.pyplot as plt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def do_image(path):

    # file_name = path.split("/")[-1]
    # user_num = path.split("/")[-2]

    # cv2로 imgage 읽어와서 input_re에 값 대입
    input_re = cv2.imread(path)
    # rembg 라이브러리의 remove를 이용하여 배경 제거
    output = remove(input_re)

    #save_path = "E:/Project/images/closet/" + str(user_num) + "/"
    #full_path = save_path + str(file_name)[:18] + ".png"
    #cv2.imwrite(full_path, output)
    cv2.imwrite(path, output)

    # path = np.array(path)

    return path

# 상의 분류 코드 : 1
def top_image(path):

    print('상의로 왔다')
    answer = ['후드', '자켓', '니트/가디건', '긴팔/맨투맨', '원피스', '패딩', '셔츠', '반팔']
    loaded_model = tf.keras.models.load_model('E:/Project/tb_top.hdf5')
    img = np.array(path)
    img = img.astype('float32')
    img = img / 255
    img = np.expand_dims(img, 0)
    test_result = loaded_model.predict(img).argmax(axis=-1)
    result = list([int(x) for x in test_result])
    print(answer[result[0]])
        #  첫번째 answer는 이름 값, 두번째는 DB 저장을 위한 숫자번호
    return answer[result[0]], result[0]+1


# 하의 분류 코드 : 2
def bottom_image(path):
    print('하의로 왔다')
    answer = ['청바지', '긴바지', '반바지', '스커트']
    loaded_model = tf.keras.models.load_model('E:/Project/tb_bottom.hdf5')
    img = np.array(path)
    img = img.astype('float32')
    img = img / 255
    img = np.expand_dims(img, 0)
    test_result = loaded_model.predict(img).argmax(axis=-1)
    result = list([int(x) for x in test_result])
        #  첫번째 answer는 이름 값, 두번째는 DB 저장을 위한 숫자번호
    return answer[result[0]], result[0]+1


# 기타 분류 코드 : 3
def etc_image(path):

    print('기타 등등으로 왔다')
    answer = ['모자', '신발']
    loaded_model = tf.keras.models.load_model('E:/Project/model_capshoes.hdf5')
    img = np.array(path)
    img = img.astype('float32')
    img = img / 255
    img = np.expand_dims(img, 0)
    test_result = loaded_model.predict(img).argmax(axis=-1)
    result = list([int(x) for x in test_result])
        #  첫번째 answer는 이름 값, 두번째는 DB 저장을 위한 숫자번호
    return answer[result[0]], result[0]+1


def type_image(path):

    result = Image.open(do_image(path)).convert('RGB')
    result_img = result.resize((220, 220))
    print(result)
    loaded_model = tf.keras.models.load_model('E:/Project/major_2_classification.hdf5')
    img = np.array(result_img)
    img = img.astype('float32')
    img = img / 255
    img = np.expand_dims(img, 0)
    test_result = loaded_model.predict(img).argmax(axis=-1)
    #    print(answer[test_result[0]])  #answer 이름대로
    print("의류 분류 타입 숫자 출력 값 : ")
    result = list([int(x) for x in test_result])
    big_cate = []

    if result[0] == 0:  # bottom 분류
        result = bottom_image(result_img)  # 분류 이름 값과 small 분류(숫자) 값
        big_cate.append(2)  # big 분류 (숫자)

    elif result[0] == 1:  # etc 분류
        result = etc_image(result_img)  # 분류 이름 값과 small 분류(숫자) 값
        big_cate.append(3)  # big 분류 (숫자)

    elif result[0] == 2:  # top 분류
        result = top_image(result_img)  # 분류 이름 값과 small 분류(숫자) 값
        big_cate.append(1)  # big 분류 (숫자)

    return result, big_cate



############################### 등록하기 위한 메소드들은 아래에 정의한다 #####################################
#
# def top_image2(path):
#
#     print('상의로 왔다')
#     answer = ['후드', '자켓', '니트/가디건', '긴팔/맨투맨', '원피스', '패딩', '셔츠', '반팔']
#     loaded_model = tf.keras.models.load_model('E:/Project/tb_top.hdf5')
#     img = np.array(path)
#     img = img.astype('float32')
#     img = img / 255
#     img = np.expand_dims(img, 0)
#     test_result = loaded_model.predict(img).argmax(axis=-1)
#     result = list([int(x) for x in test_result])
#     print(result[0])
#
#     return result[0]+1
#
#
#
# def bottom_image2(path):
#     print('하의로 왔다')
#     answer = ['청바지', '긴바지', '반바지', '스커트']
#     loaded_model = tf.keras.models.load_model('E:/Project/tb_bottom.hdf5')
#     img = np.array(path)
#     img = img.astype('float32')
#     img = img / 255
#     img = np.expand_dims(img, 0)
#     test_result = loaded_model.predict(img).argmax(axis=-1)
#     result = list([int(x) for x in test_result])
#
#     return result[0]+1
#
# def etc_image2(path):
#
#     print('기타 등등으로 왔다')
#     answer = ['모자', '신발']
#     loaded_model = tf.keras.models.load_model('E:/Project/model_capshoes.hdf5')
#     img = np.array(path)
#     img = img.astype('float32')
#     img = img / 255
#     img = np.expand_dims(img, 0)
#     test_result = loaded_model.predict(img).argmax(axis=-1)
#     result = list([int(x) for x in test_result])
#
#     return result[0]+1
#
# # 소분류 코드
# def type_image3(path):
#
#     result = Image.open(do_image(path)).convert('RGB')
#     result_img = result.resize((220, 220))
#     print(result)
#     loaded_model = tf.keras.models.load_model('E:/Project/major_2_classification.hdf5')
#     # loaded_model.save('imgTest/check/closet_model.hdf5')
#     # # files = glob.glob('./data/temp/images/*')
#     # img = Image.open('Image/test1/1_re.jpg')
#     # plt.imshow(img)
#     # plt.axis('off');
#     img = np.array(result_img)
#     img = img.astype('float32')
#     img = img / 255
#     img = np.expand_dims(img, 0)
#     test_result = loaded_model.predict(img).argmax(axis=-1)
#     #    print(answer[test_result[0]])  #answer 이름대로
#     print("의류 분류 타입 숫자 출력 값 : ")
#     result = list([int(x) for x in test_result])
#
#     if result[0] == 0:
#         result = bottom_image2(result_img)
#
#     elif result[0] == 1:
#         result = etc_image2(result_img)
#
#     elif result[0] == 2:
#         result = top_image2(result_img)
#
#     return result
#
#
# # 대분류 코드
# def type_image2(path):
#
#     result = Image.open(do_image(path)).convert('RGB')
#     result_img = result.resize((220, 220))
#     print(result)
#     loaded_model = tf.keras.models.load_model('E:/Project/major_2_classification.hdf5')
#     # loaded_model.save('imgTest/check/closet_model.hdf5')
#     # # files = glob.glob('./data/temp/images/*')
#     # img = Image.open('Image/test1/1_re.jpg')
#     # plt.imshow(img)
#     # plt.axis('off');
#     img = np.array(result_img)
#     img = img.astype('float32')
#     img = img / 255
#     img = np.expand_dims(img, 0)
#     test_result = loaded_model.predict(img).argmax(axis=-1)
#     #    print(answer[test_result[0]])  #answer 이름대로
#     print("의류 분류 타입 숫자 출력 값 : ")
#     result = list([int(x) for x in test_result])
#     result2 = []
#     # 하의 bottom
#     if result[0] == 0:
#         result2.append(2)
#
#     # 기타 etc
#     elif result[0] == 1:
#         result2.append(3)
#
#     #상의 top
#     elif result[0] == 2:
#         result2.append(1)
#
#     return result2[0]