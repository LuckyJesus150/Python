import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Зчитуємо текст з файлу
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(current_directory, '100words.txt')

with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
    # решта вашого коду

    text = file.read()

# Токенізація по словам
tokens = word_tokenize(text)

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in lemmatized_tokens if token.lower() not in stop_words]

# Видалення пунктуації
filtered_tokens = [token for token in filtered_tokens if token not in string.punctuation]

# Запис обробленого тексту у інший файл
processed_text = ' '.join(filtered_tokens)
with open('processed_text.txt', 'w', encoding='utf-8') as file:
    file.write(processed_text)
