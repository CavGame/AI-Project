import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Dataset base: Domande e risposte
questions = ["Ciao, come stai?", "Che ore sono?", "Qual è il tuo nome?"]
answers = ["Sto bene, grazie!", "Non ho un orologio.", "Mi chiamo AI."]

# Tokenizzazione delle frasi
tokenizer = Tokenizer()
tokenizer.fit_on_texts(questions + answers)
vocab_size = len(tokenizer.word_index) + 1

# Converti testo in sequenze numeriche
input_sequences = tokenizer.texts_to_sequences(questions)
output_sequences = tokenizer.texts_to_sequences(answers)

# Padding per uniformare la lunghezza
max_length = max(len(seq) for seq in input_sequences)
input_sequences = pad_sequences(input_sequences, maxlen=max_length, padding='post')
output_sequences = pad_sequences(output_sequences, maxlen=max_length, padding='post')

# Creazione del modello
model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=64, input_length=max_length),
    LSTM(128, return_sequences=True),
    LSTM(128),
    Dense(128, activation='relu'),
    Dense(vocab_size, activation='softmax')
])

# Compilazione del modello
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Prepara output per l'addestramento (shift delle sequenze)
output_sequences = [seq[1:] + [0] for seq in output_sequences]

# Addestramento del modello
model.fit(input_sequences, output_sequences, epochs=500, batch_size=2)

# Funzione per rispondere a una domanda
def answer_question(question):
    seq = tokenizer.texts_to_sequences([question])
    seq = pad_sequences(seq, maxlen=max_length, padding='post')
    pred = model.predict(seq)
    pred_word = tokenizer.index_word.get(pred.argmax(axis=1)[0], "Non so rispondere.")
    return pred_word

# Prova il cervello
print(answer_question("Ciao, come stai?"))
