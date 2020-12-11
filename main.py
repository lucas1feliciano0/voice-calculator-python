import pyaudio,os
import speech_recognition as sr
import playsound
from gtts import gTTS



# Funções matemáticas
def plus(number1, number2):
    result = number1 + number2

    speak(f"O resultado de {number1} mais {number2} é {result}")


def sub(number1, number2):
    result = number1 - number2

    speak(f"O resultado de {number1} menos {number2} é {result}")


def mult(number1, number2):
    result = number1 * number2

    speak(f"O resultado de {number1} vezes {number2} é {result}")


def div(number1, number2):
    result = number1 / number2

    speak(f"O resultado de {number1} dividido por {number2} é {result}")
# Funções de voz

def speak(text):
    print(text)
    tts = gTTS(text=text, lang="pt-br")
    filename = "user_audio.mp3"

    tts.save(filename)
    playsound.playsound(filename)
    os.remove('user_audio.mp3')


def listen_numbers(operation):
    speak(f'Você escolheu a {operation}!')
    speak('Agora diga um número.')

    number1 = None 
    number2 = None

    while True:
        try:
            number1_audio = r.listen(source)
            number1_recognized = r.recognize_google(number1_audio,language='pt-BR')
            number1 = int(number1_recognized)

            break

        except ValueError:
            speak(f'Ei! {number1_recognized} não é válido. Fale novamente')

        except sr.UnknownValueError:
            speak('Vish! Não entendi. pode repetir o número?')

    speak('Agora diga outro número.')

    while True:
        try:
            number2_audio = r.listen(source)
            number2_recognized = r.recognize_google(number2_audio,language='pt-BR')
            number2 = int(number2_recognized)

            break
        
        except ValueError:
            speak(f'Ei! {number2_recognized} não é válido. Fale novamente')

        except sr.UnknownValueError:
            speak('Vish! Não entendi. pode repetir o número?')

    return number1, number2
    

def mainfunction(source):
    speak('Seja bem-vindo à calculadora de voz.')
    speak('Diga uma das quatro operações matemáticas')

    r.adjust_for_ambient_noise(source)

    while True: #Para que pergunte novamente caso não entenda
        audio = r.listen(source)
        
        try:
            user = r.recognize_google(audio,language='pt-BR')

            print(user)

            if user == "somar" or user == "soma":
                number_plus_1, number_plus_2 = listen_numbers('soma')

                plus(number_plus_1, number_plus_2)
                break

            elif user == "menos" or user == "subtrair" or user == "subtração":
                number_sub_1, number_sub_2 = listen_numbers('subtração')

                sub(number_sub_1, number_sub_2)
                break
            elif user == "multiplicação" or user == "vezes" or user == "multiplicar":
                number_mult_1, number_mult_2 = listen_numbers('multiplicação')

                mult(number_mult_1, number_mult_2)
                break
            elif user == "divisão" or user == "dividir":
                number_div_1, number_div_2 = listen_numbers('divisão')

                div(number_div_1, number_div_2)
                break
            else:
                speak(f'Opa! {user} não é uma opção válida. Pode falar novamente?')

        except sr.UnknownValueError:
            speak('Não entendi. Fale novamente.')
    

if __name__ == "__main__":
    r = sr.Recognizer()

    with sr.Microphone() as source:
        while 1:
            mainfunction(source)