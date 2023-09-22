import random

# 元素の情報を辞書で定義します。
elements_info = {
    "H": {"name": "水素", "atomic_number": 1, "atomic_mass": 1.008, "description": "最も軽い元素で、宇宙に豊富に存在します。"},
    "He": {"name": "ヘリウム", "atomic_number": 2, "atomic_mass": 4.0026, "description": "低温で液体ヘリウムとして存在し、浮遊気球に使用されます。"},
    "Li": {"name": "リチウム", "atomic_number": 3, "atomic_mass": 6.94, "description": "軽い金属で、リチウムイオン電池に使用されます。"},
    "Be": {"name": "ベリリウム", "atomic_number": 4, "atomic_mass": 9.0122, "description": "軽量で非常に堅い金属です。"},
    "B": {"name": "ホウ素", "atomic_number": 5, "atomic_mass": 10.81, "description": "軽い金属で、ホウ酸などの化合物に含まれます。"},
    "C": {"name": "炭素", "atomic_number": 6, "atomic_mass": 12.011, "description": "生命の基本要素で、ダイヤモンドや石炭などに存在します。"},
    "N": {"name": "窒素", "atomic_number": 7, "atomic_mass": 14.007, "description": "空気中の主要成分で、植物の成長に重要です。"},
    "O": {"name": "酸素", "atomic_number": 8, "atomic_mass": 15.999, "description": "生命の維持に必要で、大気中に豊富に存在します。"},
    "F": {"name": "フッ素", "atomic_number": 9, "atomic_mass": 18.998, "description": "強力な酸化剤で、歯科用途に使用されます。"},
    "Ne": {"name": "ネオン", "atomic_number": 10, "atomic_mass": 20.180, "description": "発光ガスとして使用され、看板やディスプレイに用いられます。"},
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
