import pandas as pd

# 加载数据
data_path = 'data.csv'
data = pd.read_csv(data_path)

# 删除列名中的多余空格
data.columns = data.columns.str.strip()

# 检查缺失值和重复记录
missing_values = data.isnull().sum()
duplicates_check = data.duplicated().sum()

# 删除重复记录
data_cleaned = data.drop_duplicates()

# 对某些文本列填充缺失值为"Unknown"
text_columns_to_fill = ['condition', 'type', 'paint_color','size','county']
data_cleaned[text_columns_to_fill] = data_cleaned[text_columns_to_fill].fillna('Unknown')



# 将清洗后的数据保存为新的CSV文件
cleaned_data_path = 'data.csv'
data_cleaned.to_csv(cleaned_data_path, index=False)

