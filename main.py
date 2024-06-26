# Importa la biblioteca pyTelegramBotAPI que se utiliza para interactuar con la API de Telegram
import telebot
# Importa la biblioteca random de Python para seleccionar opciones aleatorias.
import random

#Conexión con nuestro bot
MI_TOKEN = "" # Almacena el token de acceso del bot proporcionado por BotFather.
bot = telebot.TeleBot(MI_TOKEN) # Crea una instancia del bot utilizando el token.

# La lista de opciones que reune las curiosidades sobre Batman y la ruta a las imágenes que aparecerá con cada opción.
options = [
    ("A diferencia de muchos otros superhéroes, Batman no posee poderes sobrehumanos. Es un humano ordinario con habilidades físicas y mentales extraordinarias.", "C:/Users/...jpg"),
    ("Batman en realidad tiene miedo a los murciélagos. Esto surgió después de caer en un pozo infestado de ellos en su infancia.", "C:/Users/...jpg"),
    ("A pesar de ser un superhéroe, Batman tiene un estricto código de no matar.", "C:/Users/...jpg"),
    ("El mayor trauma de Batman, que ha definido gran parte de su motivación y su misión como superhéroe, es el asesinato de sus padres, Thomas y Martha Wayne. Este evento trágico ocurrió cuando Bruce Wayne era un niño pequeño, testigo de cómo un criminal les arrebató la vida en un violento asalto en las calles de Gotham City.", "C:/Users/...jpg"),
    ("Bruce Wayne es conocido por ser uno de los hombres más ricos del mundo. Su riqueza proviene de la fortuna familiar acumulada por generaciones, gracias a las industrias Wayne y otras inversiones. Se calcula que tiene miles de millones.", "C:/Users/...jpg"),
    ("Batman y Robin se conocieron cuando Dick Grayson, un joven acróbata huérfano, presenció el asesinato de sus padres por un gánster llamado Tony Zucco. Bruce Wayne, en su identidad de Batman, investigó el crimen y decidió adoptar a Dick como su pupilo y compañero en la lucha contra el crimen. Dick se convirtió en Robin, el Chico Maravilla, y juntos formaron un equipo dinámico combatiendo la injusticia en Gotham City.", "C:/Users/...jpg")
]

# Creamos una lista de opciones que ya se hayan utilizado para que no se repitan.
used_options = []


#Creación de comandos básicos
@bot.message_handler(commands=["start"])
def send_start(message):
    start_text = "¡Saludos! Soy Alfred Pennyworth, el leal mayordomo de Bruce Wayne, también conocido como Batman."
    photo_path = "C:/Users/...jpg"      
    
    bot.send_message(message.chat.id, start_text)
    
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=["story"])
def send_story(message):
    story_text = (
        "Durante muchos años, he servido a la familia Wayne con devoción, cuidando de la Mansión Wayne y "
        "ayudando a Batman en su lucha contra el crimen en Gotham City. He sido testigo de sus "
        "momentos más oscuros y brillantes, siempre listo para ofrecer una taza de té caliente, un consejo "
        "sabio o una mano amiga./n/n"
        "Sin embargo, mi transformación en un bot fue resultado de los planes retorcidos del Joker. Durante "
        "uno de sus ataques a la Mansión Wayne, el Joker intentó borrar cualquier rastro de ayuda para Batman. "
        "Bruce Wayne, anticipando sus movimientos, transfirió mi conciencia y "
        "conocimientos a esta forma digital para preservar mi papel crucial en su lucha contra el crimen./n/n"
        "Ahora, como un asistente virtual, estoy aquí para acompañarte con la misma lealtad y eficacia. /n/n "
        "Dicho esto, te doy la bienvenida a esta nueva era. ¿En qué puedo ayudarte hoy?"
    )
    bot.send_message(message.chat.id, story_text)

@bot.message_handler(commands=["curiosities"])
def send_start(message):
    global options, used_options

    # Verificar si quedan opciones disponibles
    if len(options) == 0:
        bot.send_message(message.chat.id, "¡Ya has visto todas las curiosidades! Si hay alguna interesante que quieras que añada no dudes en escribírmelo por LinkedIn 📩")
        # Reiniciar las opciones para la próxima vez que se envíe el comando
        options = used_options.copy()
        used_options = []
        return
    
    # Elegir una opción aleatoria que no se haya usado antes
    option = random.choice(options)
    
    text = option[0]
    photo_path = option[1]

    # Enviar mensaje y foto
    bot.send_message(message.chat.id, text)
    
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    
    # Agregar la opción usada a la lista de usados y quitarla de las opciones disponibles
    used_options.append(option)
    options.remove(option)

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)