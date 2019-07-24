# ml-SanchezPaikRecipes
이 레포지토리는 ml-SanchezPaikRecipes의 food detection부분을 위한
레포지토리 입니다. apple에서 제공하는 딥러닝 라이브러리 turi create을 이용해
손 쉽게 mlmodel을 만들 수 있습니다.  
*이 레포지토리는 Mac OS와 Linux OS 에서만 사용가능합니다.*  
*한 이미지 안에 한 음식이 가득 차있다고 가정하겠습니다.*  

## Preparing Datasets
이 레포지토리는 food-11 dataset을 기반으로 만들어졌습니다.  
1. 먼저 label.txt에 detection할 데이터의 label을 넣으세요. label.txt에서의 
줄의 수는 각 label의 index에 대응됩니다.  
- Example: label.txt
``` txt
Bread
Dairy product
Dessert
Egg
Fried food
Meat
Noodles/Pasta
Rice
Seafood
Soup
Vegetable/Fruit'
```
2. images라는 폴더를 만든 후 그 폴더 안에 이미지 데이터셋을 넣으세요 이때
이미지의 파일명은 다음을 따릅니다.
```
FoodIndex_FileName.Extension
```
- Example: 빵과 달걀 이미지
``` txt
0_001.jpg // 빵시작
0_002.jpg
0_003.jpg
0_004.jpg
   ...
0_100.jpg
3_001.jpg // 달걀 시작
3_002.jpg
3_003.jpg
3_004.jpg
   ...
3_100.jpg
```

3. 다음 명령어를 입력합니다
``` bash
python make_csv.py
python make_dataset.py
```

## How to Train
다음 명령어를 입력합니다
``` bash
python yolo.py
```
그러면 yolo_food.mlmodel 파일이 나올것이고 coreml에 적용하시면 됩니다.