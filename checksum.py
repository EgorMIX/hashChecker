import hashlib
import os

def calculate_hash(filename, algorithm_choice):
  """Вычисляет хэш-сумму для заданного файла с использованием выбранного алгоритма.

  Args:
    filename: Путь к файлу.
    algorithm_choice: Цифровой выбор алгоритма (1 - sha256, 2 - sha1, 3 - md5).

  Returns:
    Хэш-сумма в виде шестнадцатеричной строки.
  """

  algorithms = {
      1: "sha256",
      2: "sha1",
      3: "md5"
  }

  algorithm = algorithms.get(algorithm_choice)
  if not algorithm:
    return "Неверный выбор алгоритма."

  hash_obj = getattr(hashlib, algorithm)()
  with open(filename, "rb") as file:
    while True:
      chunk = file.read(4096)
      if not chunk:
        break
      hash_obj.update(chunk)
  return hash_obj.hexdigest()

def compare_hash(filename, hash_sum, algorithm_choice):
  """Сравнивает хэш-сумму файла с заданной суммой.

  Args:
    filename: Путь к файлу.
    hash_sum: Целевая хэш-сумма в виде шестнадцатеричной строки.
    algorithm_choice: Цифровой выбор алгоритма (1 - sha256, 2 - sha1, 3 - md5).

  Returns:
    True, если хэш-суммы совпадают, иначе False.
  """

  calculated_hash = calculate_hash(filename, algorithm_choice)
  print(f"Hash of file '{filename}': {calculated_hash}")
  return calculated_hash == hash_sum

def compare_files(filename1, filename2, algorithm_choice):
  """Сравнивает хэш-суммы двух файлов.

  Args:
    filename1: Путь к первому файлу.
    filename2: Путь к второму файлу.
    algorithm_choice: Цифровой выбор алгоритма (1 - sha256, 2 - sha1, 3 - md5).

  Returns:
    True, если хэш-суммы совпадают, иначе False.
  """

  hash1 = calculate_hash(filename1, algorithm_choice)
  hash2 = calculate_hash(filename2, algorithm_choice)
  print(f"Hash of file '{filename1}': {hash1}")
  print(f"Hash of file '{filename2}': {hash2}")
  return hash1 == hash2

def print_hash(filename, algorithm_choice):
  """Вычисляет и выводит хэш-сумму файла.

  Args:
    filename: Путь к файлу.
    algorithm_choice: Цифровой выбор алгоритма (1 - sha256, 2 - sha1, 3 - md5).
  """

  hash_code = calculate_hash(filename, algorithm_choice)
  print(f"Хэш-сумма файла '{filename}': {hash_code}")

# Вывод информации о разработчике
print("Program developed by EgorMIX Version:1.2.1")

# Выбор языка
while True:
  language = input("Choose language:\n1 - Russian\n2 - English\nВведите номер: ")
  if language in ["1", "2"]:
    break
  else:
    print("Incorrect choice. Please enter 1 or 2.")

# Создание словаря для перевода
translations = {
  "ru": {
    "choose_algorithm": "Выберите алгоритм хэширования:\n1 - SHA-256\n2 - SHA-1\n3 - MD5\nВведите номер: ",
    "invalid_choice": "Неверный выбор. Пожалуйста, введите 1, 2 или 3.",
    "invalid_input": "Неверный ввод. Пожалуйста, введите число.",
    "enter_filename": "Введите путь к файлу: ",
    "enter_hash_sum": "Введите хэш-сумму: ",
    "hash_match": "Хэш-сумма файла '{filename}' совпадает с заданной.",
    "hash_mismatch": "Хэш-сумма файла '{filename}' не совпадает с заданной.",
    "enter_first_filename": "Введите путь к первому файлу: ",
    "enter_second_filename": "Введите путь ко второму файлу: ",
    "files_match": "Файлы идентичны.",
    "files_mismatch": "Файлы различаются.",
    "choose_comparison_type": "Выберите тип сравнения:\n1 - Сравнить с хэш-суммой\n2 - Сравнить два файла\n3 - Вывести хэш-сумму файла\nВведите номер: ",
    "print_hash": "Вывести хэш-сумму файла"
  },
  "en": {
    "choose_algorithm": "Choose hash algorithm:\n1 - SHA-256\n2 - SHA-1\n3 - MD5\nEnter number: ",
    "invalid_choice": "Incorrect choice. Please enter 1, 2 or 3.",
    "invalid_input": "Invalid input. Please enter a number.",
    "enter_filename": "Enter file path: ",
    "enter_hash_sum": "Enter hash sum: ",
    "hash_match": "Hash of file '{filename}' matches the given one.",
    "hash_mismatch": "Hash of file '{filename}' does not match the given one.",
    "enter_first_filename": "Enter the path to the first file: ",
    "enter_second_filename": "Enter the path to the second file: ",
    "files_match": "Files are identical.",
    "files_mismatch": "Files are different.",
    "choose_comparison_type": "Choose comparison type:\n1 - Compare with hash sum\n2 - Compare two files\n3 - Print file hash\nEnter number: ",
    "print_hash": "Print file hash"
  }
}

# Получение входных данных от пользователя
if language == "1":
  lang = "ru"
else:
  lang = "en"

while True:
  try:
    algorithm_choice = int(input(translations[lang]["choose_algorithm"]))
    if 1 <= algorithm_choice <= 3:
      break
    else:
      print(translations[lang]["invalid_choice"])
  except ValueError:
    print(translations[lang]["invalid_input"])

# Выбор действия: сравнение с хэш-суммой или сравнение двух файлов
while True:
  comparison_type = input(translations[lang]["choose_comparison_type"])
  if comparison_type in ["1", "2", "3"]:
    break
  else:
    print(translations[lang]["invalid_choice"])

if comparison_type == "1":
  filename = input(translations[lang]["enter_filename"]).strip("'\"") # Удаляем кавычки
  hash_sum = input(translations[lang]["enter_hash_sum"])
  if compare_hash(filename, hash_sum, algorithm_choice):
    print(translations[lang]["hash_match"].format(filename=filename))
  else:
    print(translations[lang]["hash_mismatch"].format(filename=filename))
elif comparison_type == "2":
  filename1 = input(translations[lang]["enter_first_filename"]).strip("'\"") # Удаляем кавычки
  filename2 = input(translations[lang]["enter_second_filename"]).strip("'\"") # Удаляем кавычки
  if compare_files(filename1, filename2, algorithm_choice):
    print(translations[lang]["files_match"])
  else:
    print(translations[lang]["files_mismatch"])
elif comparison_type == "3":
  filename = input(translations[lang]["enter_filename"]).strip("'\"") # Удаляем кавычки
  print_hash(filename, algorithm_choice)
