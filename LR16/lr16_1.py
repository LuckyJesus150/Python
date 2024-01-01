import nltk
import matplotlib.pyplot as plt
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from string import punctuation

# Завантаження тексту з Project Gutenberg
nltk.download('gutenberg')
file_id = 'bryant-stories.txt'
text = gutenberg.raw(file_id)

# Токенізація слів
nltk.download('punkt')

words = word_tokenize(text)

# Визначення кількості слів у тексті
num_words = len(words)
print(f"Кількість слів у тексті: {num_words}")

# Визначення 10 найбільш вживаних слів та побудова діаграми
fdist = FreqDist(words)
top_words = fdist.most_common(10)
print("10 найбільш вживаних слів у тексті:")
print(top_words)

# Побудова стовпчастої діаграми
plt.figure(figsize=(10, 5))
fdist.plot(10, cumulative=False)
plt.title('10 найбільш вживаних слів у тексті')
plt.show()

# Видалення стоп-слів та пунктуації
nltk.download('stopwords')
stop_words = set(stopwords.words('english') + list(punctuation))
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

# Визначення 10 найбільш вживаних слів після фільтрації та побудова діаграми
filtered_fdist = FreqDist(filtered_words)
filtered_top_words = filtered_fdist.most_common(10)
print("10 найбільш вживаних слів після видалення стоп-слів та пунктуації:")
print(filtered_top_words)

# Побудова стовпчастої діаграми після фільтрації
plt.figure(figsize=(10, 5))
filtered_fdist.plot(10, cumulative=False)
plt.title('10 найбільш вживаних слів після видалення стоп-слів та пунктуації')
plt.show()
