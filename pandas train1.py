# 📊 Fitness Data Analysis Project using Pandas, NumPy & Matplotlib
# هذا المشروع يستعرض مهارات تحليل البيانات الأساسية باستخدام مكتبة Pandas.
# يشمل تنظيف البيانات، التحليل الإحصائي، التصور البياني، واستخراج رؤى قابلة للاستخدام.
# مناسب للمهتمين بتحليل بيانات اللياقة أو تعلم أساسيات علم البيانات بلغة بايثون.

# استيراد المكتبات الأساسية
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

# قراءة البيانات من ملف CSV
df = pd.read_csv("data.csv")

# عرض عنوان توضيحي للتقرير
print("📊 Data Analysis Report - Fitness Dataset\n")

# استعراض مبدئي للبيانات
print(df.head())
print(df.info())
print(df.shape)
print(df.index)
print(df.columns)
print(df.describe())

# طباعة نوع كل عمود
for col in df.columns:
    print(f"the type of the column {col} is {df[col].dtype}")

# التحقق من القيم المفقودة
print(df.isnull().sum())

# حذف الصفوف التي تحتوي على قيم مفقودة
df = df.dropna()
print(df.shape)

# حذف الصفوف المكررة إن وُجدت
print(df.duplicated().sum())
df = df.drop_duplicates()

# تنسيق أسماء الأعمدة لتكون سهلة الاستخدام
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.columns)

# تحويل نوع عمود "calories" إلى أعداد صحيحة
df["calories"] = df["calories"].astype("int64")

# التأكد من أنواع البيانات بعد التنظيف
for col in df.columns:
    print(f"the type of the column {col} is {df[col].dtype}")

# التحليل الإحصائي لعمود السعرات
print(f"the mean for the column calories is {df['calories'].mean()}")
print(f'the median for the column calories is {np.median(df["calories"])}')
print(f'the std for the column calories is {np.std(df["calories"])}')

# تحليل تكرار القيم في عمود "duration"
print(df["duration"].value_counts())

# رسم بياني شريطي يوضح توزيع "duration"
plt.bar(df["duration"].value_counts().index, df["duration"].value_counts(),
        color="r", width=10, edgecolor="k")
plt.xlabel("the duration")
plt.ylabel("the repetition")
plt.title("the repetition of the duration")
plt.show()

# رسم scatter لتوضيح العلاقة بين pulse و calories
plt.scatter(df["pulse"], df["calories"])
plt.xlabel("Pulse")
plt.ylabel("Calories")
plt.title("Pulse vs Calories")
plt.show()

# رسم histogram لتوزيع قيم pulse
plt.hist(df["pulse"], color="r", edgecolor="k", width=0.9)
plt.title("Pulse Distribution")
plt.show()

# تصفية البيانات: أشخاص سعراتهم >50 ونبضهم >100
sub = df[(df["calories"] > 50) & (df["pulse"] > 100)]
print(sub)

# إنشاء عمود جديد يمثل مجموع النبض والنبض الأقصى
df["total"] = df["pulse"] + df["maxpulse"]
print(df)

# تحليل تجميعي: متوسط النبض حسب المدة
group = df.groupby("duration")["pulse"].mean()
print(group)

# حفظ البيانات النظيفة إلى ملف CSV نهائي
df.to_csv("the result.csv", index=False)
