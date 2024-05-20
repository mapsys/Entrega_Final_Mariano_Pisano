# ENTREGA_FINAL_MARIANO_PISANO

# Demo:

# Instalación:

Debe correr el proyecto en un virtualEnv al que le puede instalar los requerimientos con pip install -r requirements.txt
ya posee un user admin creado:
user: admin
pass: 123

Tambien posee un usuario no admin creado
user: user
pass: user1234



# Ejecución

1. Para la ejecución del proyecto, tipear **_python manage.py runserver_**, y luego dirigirse a su navegador.



# Secciones y funcionalidades

1. Nuestros viajes: Pagina principal del sistema de Blogs. te permite leer diferentes Blogs sobre viajes e intercambiar informacion con los diferentes usuarios
2. Inicio: Te lleva a la pagina principal del sistema
3. Acerca de mi: Un poco de informacion del creador de la pagina
   ---- Si estas logeado-----
4. Mensajeria: Te permite intercambiar mensajes con diferentes usuarios de la plataforma
   NOTA: el nuevo mensaje se puede enviar presionando enter
5. Posteos: Aqui podras ver todos los posts de nuestros lectores
   a. Ver posteos: Podras ver una lista de los posteos existentes
   b. Nuevo posteo: Podras crear una entrada nueva en nuestro blog
   c: Buscar posteos: Podras buscar posteos por su titulo.
6. users (o {Nombre user}) : Administracion de usuaarios
   Si estas logeado:
   a. Ver Perfil: te permite ver informacion de tu perfil y editarlo o cambiar contraseña
   b. Logout: Te permite deslogearte de la plataforma
   Si no estas logeado
   a. Registrarme: te permite crear un usuario nuevo para poder usar la plataforma
   b: Login: Te permite identificarte en la plataforma

# Problemas conocidos:

1. No logro hacer aparecer la imagen del avatar al lado del nombre de usuario

# Mejoras futuras

## Se puede mejorar MUCHISIMO el diseño de la pagina para darle mejor aspecto y mas moderno

## marcar los mensajes como Leidos y mostrar en el menu Mensajeria una campanita de "Mensajes nuevos sin leer"

## hacer que cuando me manden un nuevo mensaje mientras yo estoy en la pagina de una conversacion lo pueda ver aparecer sin tener que refrescar la pagina (se lo pregunte a ChatGPT pero no me parecio valido solo copiar y pegar el codigo aca)
