questions += ["Qual è il tuo colore preferito?", "Dove vivi?", "Cosa fai?"]
answers += ["Mi piace il blu!", "Vivo nel cloud.", "Aiuto le persone con le domande."]
while True:
    question = input("Fai una domanda: ")
    if question.lower() == "exit":
        break
    print("Risposta: " + answer_question(question))
model.save('chatbot_model.h5')
model = tf.keras.models.load_model('chatbot_model.h5')
