import random

# 元素の情報を辞書で定義します。
elements_info = {
    "H": {"name": "水素", "atomic_number": 1, "atomic_mass": 1.008, "description": "最も軽い元素で、宇宙に豊富に存在します。"},
    "He": {"name": "ヘリウム", "atomic_number": 2, "atomic_mass": 4.0026, "description": "低温で液体ヘリウムとして存在し、浮遊気球に使用されます。"},
    # 他の元素の情報も追加してください。
    # ...
}

def element_gacha():
    # ランダムに元素記号を選択します。
    random_symbol = random.choice(list(elements_info.keys()))
    return random_symbol

# ガチャを実行して元素記号を取得します。
selected_symbol = element_gacha()
selected_element = elements_info[selected_symbol]

# 選択された元素の情報を表示します。
print(f"選択された元素: {selected_element['name']}")
print(f"原子番号: {selected_element['atomic_number']}")
print(f"原子質量: {selected_element['atomic_mass']}")
print(f"説明: {selected_element['description']}")
