import telebot
import re
def zonashorarias(hora):
    horas = { "HORA DE LA CLASE!!!:\n 🇪🇸 España: " : hora, "🇵🇪 Peru: " : hora - 6,"🇩🇴 Republica Dominicana: " : hora - 4, "🇲🇽 Mexico: " : hora - 7, "🇪🇸 Canarias: " : hora - 1, "🇻🇪 Venezuela: " : hora - 5}
    return horas
token = '5025557251:AAHi8smeeuG7KQZINcqAwO1JpHRVopUDqdo'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["help"])
def ayuda(message):
    bot.reply_to(message, "Comandos Disponibles\n 1.Libros\n 2.linkclase\n 3.Portfolio\n 4.Invitacion\n 5.clase\n 6.Redteam\nCERTIFICACIONES\n 7.OSCP \n 8.CEH \n 9.eCPPTv2\n 10.OSWE\n 11.Pentest+\n 12.eJPT\n 13.eWPTXv2\n 14.Mas" )
@bot.message_handler(commands=["clase"])
def enviar(message):
    horasstring = ""
    try:
        message.text = re.sub("/clase ", "", message.text)
        #bot.reply_to(message, message.text)
        hora, minutos = message.text.split(":")
        #bot.reply_to(message, hora + minutos)
        horas = zonashorarias(int(hora))
        for pais, hora in horas.items():
            horasstring += (pais + str(hora) + ":" + str(minutos) + '\n')

        bot.reply_to(message, horasstring)
    except:
        bot.reply_to(message, "Añada una hora por favor")
        print(message)
@bot.message_handler(commands=["linkclase"])
def enlace(message):
    bot.reply_to(message, "Enlace Clases: https://meet.jit.si/Clasesluijait")
       # horas, minutos = map(int, message.text.split(':')
@bot.message_handler(commands=["Portfolio","portfolio"])
def portfolio(message):
    bot.reply_to(message, "Porfolio del desarrollador: https://luijait.es\n Github del Desarrollador: https://github.com/luijait")
@bot.message_handler(commands=["Invite","Invitacion","invitacion","invitación"])
def invitacion(message):
    bot.reply_to(message, "Invitacion a este canal de telegram: https://t.me/+ztgFD3ifWJQ0NmE0")
@bot.message_handler(commands=["Roadmap","roadmap"])
def roadmap(message):
    bot.reply_to(message, "Construye tu camino en el pentesting!!: https://github.com/SundownDEV/hacker-roadmap")
@bot.message_handler(commands=["Cursos","cursos"])
def cursos(message):
    bot.reply_to(message, '''
    1. Creador de Licencias de Software en Visual Basic net
    http://www.mediafire.com/file/mbgsqhlyxzxekic/1._Creador_de_Licencias_de_Software_en_Visual_Basic_net.rar/file
📚 Libros de Programación
PHP + MySQL
Programacion desde cero
Java desde cero
Desarrollo web con Java
https://mega.nz/folder/ZQZmxBLK#pdS_K3jc0Cfn7vuq0N-z2Q
Seguridad informática:
https://onedrive.live.com/?cid=cbd7bc08311464ee&id=CBD7BC08311464EE%2137688&authkey=!AA2cxRLqaxPfjTA
Libros de programación:
   https://onedrive.live.com/?authkey=%21ADTyoMKzCePpfuo&id=CBD7BC08311464EE%2133018&cid=CBD7BC08311464EE

💻 Curso Hacking Redes Sociales
Aprende sobre el hackeo en las redes sociales
https://mega.nz/folder/C9JXnCQC#-G4GIw1g7DEZRYbizvN4zQ
Introducción a Terminal y Línea de Comandos
https://mega.nz/folder/W1wWwJha#CMA_jFjQawmI2OjsRV-7Cg
Curso de ASP.NET Core
https://mega.nz/folder/7ppjxIYa#k3eVBILI2ChWu9hrIQWz7Q
Curso de Autenticación con Oauth
https://mega.nz/folder/Pk4jwCKS#eKkIp9UZC6fRvr7lLlMjAw
Curso de Bootstrap
https://mega.nz/folder/e1phzKLY#mKiOlUJfhhK96EJm6wMGng
Curso de C# con .Net Core               
https://mega.nz/folder/3phVVQ6I#P7D_sLv6qXBv6Ggy55bi9A
Curso de CSS Grid Layout
https://mega.nz/folder/DhwzgYjC#2lGGnEN5uOedtIK8fgu6Jw
Curso de Desarrollo Web Online
https://mega.nz/folder/bx5TBIhI#0gjjbW8tZJ91lDE4LhARJA
Curso de Electron Apps de escritorio en Windows y Mac
https://mega.nz/folder/fh4FTIIT#mMKoeSp07ZzTj5kEaENg2g
Curso de Hacking Ético
https://mega.nz/folder/b4h1haxA#49RMMkLsGBTtC41C7JAzig
Nombre:Curso de linux
Sinopsis:
Aprende todo sobre Linux y características que te ofrece este sistema operativo.
Formato: .mp4
Módulos: 19
Peso: 6.37 GB 
Link:
https://mega.nz/folder/Xc9AkDaB#mV3EAsdknUiG2OYdg1dRngj
+300 cursos de platzy
https://mega.nz/#F!vZ5FTADT!AVMhZdDva33ZO6S1m7bK3A!KIohWAbI
🔰35 GB de libros de informática que cubren todo, desde algoritmos hasta XML🔰
 ¿Alguna vez quisiste convertirte en un mago de la informática?  no busque más.  Esta colección de libros de ciencias de la computación fue creada específicamente para que usted se convierta en un mago de la computación por magos de la computación.
 Son 3616 archivos y 35 GB que cubren todo, desde algoritmos hasta XML.
 La biblioteca de Gentoomen está compuesta por casi 4 mil títulos que cubren más de 25 temas que van desde algoritmos y criptografía hasta inteligencia artificial.
 Enlace: https://g.sicp.me/book
🔰CURSOS DE HACKING ANDROID🔰
 1) Prueba de penetración
 ✅ Guía de video
 https://mega.nz/folder/CY0zUACT#OVODsvO2PkC5Biv43i__NQ
 2) Configure su laboratorio
 ✅ https://mega.nz/folder/TM1jyABL#40eUd_dpLEchdUAxbXPEiQ
 3) Encontrar su camino alrededor de Kali
 ✅ https://mega.nz/folder/fVl3hI7J#tKsrQ4rjzd97b7sah6gwYw
 4) PAQUETE DE HERRAMIENTAS IMPORTANTE
 ✅ https://mega.nz/folder/fB9T0CAD#6jdad6-5XW-fSFhuhYO7Uw
    5) Explotaciones
    ✅ https://mega.nz/folder/fElDXIwA#y6qSr6jMk5dTkXUaDeEe_w
    6) Hackear dispositivos Android:
    ✅ https://mega.nz/folder/HJ8BwQrI#JiQhByO7NvsuU_nRslRhZw
    7) Ingeniería social
    ✅ https://mega.nz/folder/vUshmAgD#lJpAwyKwLss9ogVZzrnFvw
    😍 Hackear usando dispositivos Android
     ✅ https://mega.nz/folder/aVsFzQ4S#MYrQ9rc3pjDjq2pjVHCtoA"
            ''')
@bot.message_handler(commands=["redteam","RedTeam","Redteam","redTeam"])
def redteam(message):
    bot.reply_to(message,'''
    Recursos para RedTeaming:
    https://0xsp.com/offensive/red-ops-techniques/red-team-cheatsheet
    https://github.com/wsummerhill/CobaltStrike_RedTeam_CheatSheet
    https://github.com/werisnais/Red_Team
    Personalmente recomiendo este repositorio:
    https://github.com/an4kein/awesome-red-teaming
    Personalmente recomiendo este libro como guia de referencia: 
    https://es1lib.org/book/2328870/62593c    
    ''')
@bot.message_handler(commands=["blueteam","Blueteam","BlueTeam","blueTeam"])
def blueTeam(message):
    bot.reply_to(message,'''
    Recomendacion Personal:
    https://github.com/chrisjd20/Blue-Team-Cheat-Sheets/blob/master/BTCSwGSEnotes.pdf
    https://dragos.com/media/The_Four_Types%20of_Threat_Detection.pdf
    https://github.com/trimstray/the-book-of-secret-knowledge
    https://gist.github.com/alexiasa/fba4466849fde5b9ec3dd3cd7d1b3e9f
    https://dragos.com/media/The_Four_Types%20of_Threat_Detection.pdf
    https://github.com/MalwareArchaeology/ATTACK
    https://zeltser.com/analyzing-malicious-documents/
    https://github.com/ytisf/theZoo
    https://packettotal.com/malware-archive.html



    
    ''')
@bot.message_handler(commands=["ewptxv2","eWPTXv2","eWPTxv2"])
def ewptxv2(message):
    bot.reply_to(message,'''
    eWPTXv2 (eLearnSecurity Web Application Penetration Tester eXtreme)
Esta certificación es la más avanzada en temas de pentesting a aplicaciones web con la que cuenta hoy en día eLearning Security, actualmente al igual que la anterior, va por la versión 2, de ahí sus siglas (eWPTXv2), esta certificación tiene como objetivo acreditar que la persona que la posea cuenta con las capacidades para ejercer como un pentester de aplicaciones web a un nivel avanzado, esto incluye las habilidades en procesos y metodologías de pruebas de penetración, conocimientos avanzados de diferentes sistemas de gestión de bases de datos, análisis e inspección de aplicaciones web, procesos y metodologías de pruebas de penetración, entre muchas otras, además que esta certificación está destinada a personas con un alto conocimiento técnico en tema de seguridad de aplicaciones web y, como ay es típico de eLearning Security, esta certificación no tiene fecha de expiración.

Precio: El voucher para el examen de la certificación tiene un precio de 400$, únicamente el voucher, al igual que en el caso del eCPPTx2, si se desea obtener la formación necesaria para afrontar el examen (además de tener sólidos conocimientos previamente asimilados en seguridad de aplicaciones web) se deberá adquirir el INE Cyber Security Pass de INE y cursar la ruta de aprendizaje de Web Application Penetration Tester Professional.

Examen: El examen de esta certificación, como ya es típico de eLearning Security, es completamente práctico, te dan 7 días para realizar los distintos objetivos que te proponen y otros 7 días para hacer un informe ejecutivo y otro técnico donde se documente todo lo que hizo. En este examen debes conseguir y documentar todas las vulnerabilidades posibles, no te piden un mínimo, sencillamente debes intentar encontrar todas las que puedas, al tratarse de una certificación en su mayoría dedicada al pentesting web, deberás identificar y explotar vulnerabilidades como SQLi, SSRF, XSS, CSRF, XXE, entre muchas otras.
    
    ''')
@bot.message_handler(commands=["CEH","Ceh","ceh"])
def ceh(message):
    bot.reply_to(message,'''
    CEH (Certified Ethical Hacker)
La certificación CEH ofrecida por EC-Council, es una de las certificaciones más conocidas y antiguas, esta certificación busca acreditar que la persona que la posea tiene los conocimientos necesarios para, entre otras cosas, buscar vulnerabilidades en sistemas tal y como lo haría un cracker pero con fines éticos, si bien es una certificación que no es del agrado de muchos ya que, su examen es completamente teórico, (hablando exclusivamente de la certificación CEH, no de la CEH (Practical) donde el examen si es práctico y dura 6 horas), si bien esta certificación no tiene su lado práctico en el examen, tiene mucho reconocimiento laboral en todo el mundo, es una de las certificaciones más requeridas cuando se trata de ofertas de empleo como pentester, hacker ético y, en algunas ocasiones hasta en puestos de analista de ciberseguridad, entre otros.

He de decir que, en temas de aprendizaje práctico hay muchas certificaciones que son mejores que esta, las cuales tocaremos más adelante, no se puede negar que, esta certificación está decayendo bastante con el pasar del tiempo, aunque eso no quita que en ella se aprendan conceptos y que tenga un gran reconocimiento global, así que para empezar con una base está bien. También, es importante mencionar que, esta certificación caduca a los tres años de su emisión, es decir, si te certificas como CEH hoy, tu certificación será válida hasta dentro de tres años, cuando llegue el momento tendrás que recertificarte si así lo deseas. Actualmente va por la versión 11 (CEHv11) que salió en septiembre del 2020.

Precio: El precio de esta certificación puede ser discutido por el representante de ventas o el centro de capacitación, dependiendo también, del modo de capacitación, esto en caso de que se quiera hacer la formación reglamentaria para poder presentar el examen, también el costo puede variar dependiendo la región. En España, ya hay varios centros autorizados que ofrecen esta formación reglamentaria de EC-Council para esta certificación y, te dan, además de la formación, el voucher para el examen, todo esto por un precio que ronda los 1800€. Por otro lado, si ya se tienen dos años de experiencia en el sector de la seguridad informática, se puede pagar una tarifa no reembolsable de elegibilidad de 100$ y, comprar el voucher para el examen directamente sin necesidad de hacer la formación.

Examen: El examen es de opción múltiple, donde tienes 4 horas para responder cerca de 120 preguntas, para aprobar, necesitas conseguir una puntuación mayor al 70%.
    ''')
@bot.message_handler(commands=["ecppt","ecpptv2","ecppt2"])
def eccpt(message):
    bot.reply_to(message,'''
    eCPPTv2 (eLearnSecurity Certified Professional Penetration Tester)
Esta certificación, ofrecida por parte de eLearning Security, que actualmente va por la versión 2, de ahí sus siglas (eCPPTv2), es la certificación que le sigue en términos de contenido al eJPT, es una certificación altamente reconocida y que tiene como objetivo acreditar que la persona que la posea tiene las capacidades necesarias para ejercer como pentester profesional, esto incluye la capacidad de realizar una prueba de penetración con un informe de grado comercial, evaluación de la vulnerabilidad de las redes, recopilación y reconocimiento de información, desarrollo de exploits, entre muchas otras aptitudes. Muchos creen que esta certificación puede ayudar o incluso superar al OSCP, aunque eso ya es criterio de cada uno, lo que es verdad es que es una de las mejores certificaciones hablando de pentesting y, tampoco tiene fecha de expiración.

Precio: El voucher para el examen de la certificación tiene un precio de 400$, únicamente el voucher, si se desea obtener la formación necesaria para afrontar el examen se deberá adquirir el INE Cyber Security Pass de INE y cursar la ruta de aprendizaje de Penetration Testing Professional.

Examen: El examen de esta certificación como ya es típico de eLearning Security, es completamente practico donde debes comprometer activos, cuando compres el voucher se te hará llegar un correo electrónico donde te indicará el alcance del examen, se trata de una “carta” donde te indican lo que debes demostrar y cómo debes hacerlo, luego de comprometer los activos, deberás realizar un informe de calidad comercial donde hagas evidencia de cada vulnerabilidad que se detectó y se explotó, además que se debe dar remediaciones de estos fallos encontrados.
    ''')
@bot.message_handler(commands=["oswe","OSWE"])
def OSWE(message):
    bot.reply_to(message,'''
    OSWE (Offensive Security Web Expert)
Esta certificación, también ofrecida por Offensive Security, es una certificación enfocada mayoritariamente al pentesting de aplicaciones web, para obtener esta certificación se debe aprobar su examen y completar el curso AWAE (Advanced Web Attacks and Exploitation). Esta es una certificación que, el mismo Offensive Security dice que es una opción de especialización de habilidades luego de haber aprobado el OSCP y es que, esta certificación tiene como objetivo acreditar que el que la posea cuenta con las capacidades para realizar pruebas de penetración de caja blanca a aplicaciones web, metodologías de seguridad web, detectar vulnerabilidades lógicas que escáneres empresariales no suelen detectar, Inyecciones SQL ciegas, entre muchas otras habilidades. Además, al igual que pasa con el OSCP, esta certificación no tiene fecha de expiración.
Precio: El precio de esta certificación es relativo igual que pasaba con la anterior, puede variar dependiendo del tiempo que se desee acceder a los laboratorios prácticos, va desde los 1299$ hasta los 1499$, al igual que en la certificación anterior, lo que cambia es el tiempo de acceso al laboratorio, el curso y la tarifa para el examen siempre se mantienen presentes.
Examen: El examen de esta certificación es completamente practico, donde tienes 48 horas, en las primeras 24 horas debes comprometer distintos activos que, a medida que los vayas comprometiendo te darán puntos, necesitas obtener como mínimo 85/100 puntos para aprobar y, en las siguientes 24 horas debes hacer un informe donde se expongan capturas y se detalle el proceso que se siguió para comprometer los activos.


    ''')
@bot.message_handler(commands=["Pentest+","pentest+"])
def pentest(message):
    bot.reply_to(message,'''
    CompTIA PenTest+
Esta certificación ofrecida por CompTIA es, bastante valorada a nivel laboral, casi como la anterior que estábamos comentando, esta certificación tiene como objetivo acreditar que la persona que la posea tenga los conocimientos necesarios para realizar con éxito pruebas de penetración, análisis de vulnerabilidades, comprender los requisitos legales y de cumplimiento, entre otras habilidades, se recomienda altamente antes de ir por esta certificación, haber cursado las certificaciones de CompTIA Security+, Network+ o tener como mínimo 3-4 años de experiencia en seguridad de la información, además, es importante resaltar que, esta certificación debe ser validada después de los 3 años después de su lanzamiento.

Precio: El precio de esta certificación va desde 370$ hasta 949$, dependiendo del tipo de paquete que se elija.

Examen: El examen es de opción múltiple y basado en el rendimiento, tendrás 165 minutos para responder a, como máximo, 85 preguntas, donde apruebas teniendo un puntaje mínimo de 750 en una escala de 100-900.
    ''')
@bot.message_handler(commands=["eJPT","ejpt"])
def eJPT(message):
    bot.reply_to(message,'''
    eJPT (eLearning Junior Penetration Tester)
Esta certificación ofrecida por la academia eLearning Security, a mi parecer es una de las mejores certificaciones si se quiere iniciar en el mundo del pentesting de forma práctica, esta certificación tiene como objetivo acreditar que las personas que la posean tienen los conocimientos esenciales para la realización de una prueba de penetración. Es una certificación completamente práctica y, la más introductoria en temas de pentesting por parte de eLearning Security, a diferencia de las certificaciones anteriores, esta certificación tiene validez de por vida.
Precio: El precio del voucher del examen cuesta alrededor de 200$, es opcional tomar el curso de preparación, aunque es recomendable.
Examen: El examen de esta certificación se basa en que tienes que hacer una prueba de penetración sobre un escenario basado en la vida real, tendrás 3 días para resolver 20 retos, aquí no hay nada de responder preguntas de opción múltiple, es todo valerte de tus habilidades para poder aprobar, que es lo ideal sin duda.
    ''')
@bot.message_handler(commands=["OSCP","oscp","Oscp"])
def oscp(message):
    bot.reply_to(message,'''
OSCP (Offensive Security Certified Professional)
Esta certificación es una de las mejores en esta disciplina, Offensive Security es la empresa que mantiene actualmente la distribución de Linux, Kali Linux, una distribución muy usada en seguridad informática, de hecho, es uno de los factores que hacen que esta certificación tenga mucha relevancia, es una certificación completamente práctica, para obtener esta certificación, se debe aprobar su examen y completar el curso PWK (Penetration Testing with Kali Linux) donde se enseña todo lo necesario para realizar con éxito una prueba de penetración, aunque para aprobar el examen no te puedes valer solamente del material del cuso, hay que indagar mucho más por tu propia cuenta, además que, también ponen a tu disposición un laboratorio donde puedes practicar con máquinas de cara al examen.
La certificación tiene como objetivo acreditar que las personas que la posean cuentan con las capacidades de ejecutar ataques organizados de manera contralada, la identificación de vulnerabilidades, la realización de una prueba de penetración, entre muchas otras. Además, esta certificación no tiene fecha de expiración, es válida de por vida.
Precio: El precio de esta certificación es bastante relativo ya que, tienen distintas tarifas dependiendo del tiempo que se quiera tener acceso a su laboratorio practico, va desde 999$ hasta 1349$, lo que cambia en las distintas tarifas es el tiempo de acceso al laboratorio, el precio del curso y tarifa para el examen siempre se mantienen presentes.
Examen: El examen de esta certificación se realiza en dos días, el primer día, tienes literal las primeras 24 horas para comprometer cinco máquinas, cada máquina dependiendo de su dificultad te dará una serie de puntos, se deben conseguir como mínimo 70/100 puntos para poder aprobar y, las siguientes 24 horas, es decir, el segundo día, se tendrá que hacer un reporte sobre el proceso que se siguió para comprometer dichas máquinas, es importante resaltar que, durante el examen está prohibido el uso de herramientas automatizadas, tales como metasploits, sqlmap, entre otras, por lo que se debe optar por otros procesos más manuales. Esta certificación tiene tanto reconocimiento laboral como la CEH (yo diría que mucho más), además que en esta certificación se demuestra completamente las habilidades prácticas y no tanto el conocimiento teórico de la persona certificada.
de eLearning Security, es completamente practico donde debes comprometer activos, cuando compres el voucher se te hará llegar un correo electrónico donde te indicará el alcance del examen, se trata de una “carta” donde te indican lo que debes demostrar y cómo debes hacerlo, luego de comprometer los activos, deberás realizar un informe de calidad comercial donde hagas evidencia de cada vulnerabilidad que se detectó y se explotó, además que se debe dar remediaciones de estos fallos encontrados.
    ''')
@bot.message_handler(commands=["Libros","libros"])
def libros(message):
    bot.reply_to(message,'''AQUI TODOS LOS LIBROS QUE NECESITAS PARA SER HACKER: https://z-lib.org
    Recomiendaciones Personales by Luijait: 
    https://es1lib.org/book/2328870/62593c
    https://es1lib.org/book/610566/04930f?dsource=recommend
    https://es1lib.org/book/866637/a8ebab?dsource=recommend
    https://es1lib.org/book/1053096/4eac6c?dsource=recommend
    https://es1lib.org/book/1216358/a8f462?dsource=recommend
    https://es1lib.org/book/1274723/254e0e?dsource=recommend
    https://es1lib.org/book/3399523/14ceb5?dsource=recommend
    https://es1lib.org/book/764350/b2b155?dsource=recommend
    https://es1lib.org/book/489772/3a51c3
    
    ''')
@bot.message_handler(commands=["Mas","mas"])
def info(message):
    bot.reply_to(message,"Si tienes alguna sugerencia contactame")
bot.polling()

