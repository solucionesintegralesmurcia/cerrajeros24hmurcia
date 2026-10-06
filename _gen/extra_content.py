# Ampliación de contenido por página: secciones nuevas (EXTRA) y preguntas nuevas (EXTRA_FAQ).
# Todo es texto propio de cada página; no se repite entre páginas.

EXTRA = {}
EXTRA_FAQ = {}

# ------------------------------------------------------------------ INICIO
EXTRA["index.html"] = """
<section class="alt"><div class="wrap">
<h2>Todos los servicios de cerrajería en Murcia</h2>
<p>La mayoría de llamadas son por una puerta que no abre, pero el cerrajero de guardia resuelve cualquier problema con cerraduras, llaves y cierres, en casas, comunidades y negocios:</p>
<div class="grid">
<div class="card"><h3>En casa</h3><ul class="list">
<li>Apertura de puertas de piso, chalet y casa de planta baja</li>
<li>Cambio de bombín y de cerradura completa</li>
<li>Cerrojos adicionales y escudos protectores</li>
<li>Extracción de llaves partidas o atascadas</li>
<li>Cerraduras de buzón, trastero y garaje</li>
</ul></div>
<div class="card"><h3>En comunidades</h3><ul class="list">
<li><a href="cerrajeria-para-comunidades.html">Cerraduras de portal y puertas de zonas comunes</a></li>
<li>Amaestramiento: una llave para cada vecino que abre su casa y las zonas comunes</li>
<li>Cambio de bombines de cuartos de contadores y azoteas</li>
</ul></div>
<div class="card"><h3>En negocios</h3><ul class="list">
<li><a href="persianas-y-cierres-de-local.html">Apertura de persianas y cierres metálicos que no abren</a></li>
<li>Candados de alta seguridad para persianas y portones</li>
<li>Cerraduras de oficinas, almacenes y naves</li>
</ul></div>
<div class="card"><h3>Otros trabajos</h3><ul class="list">
<li><a href="apertura-de-cajas-fuertes.html">Apertura de cajas fuertes</a> de las que se ha perdido la llave o el código</li>
<li><a href="apertura-de-coches.html">Apertura de vehículos</a> con las llaves dentro</li>
<li>Instalación de cerraduras electrónicas y mirillas digitales</li>
</ul></div>
</div>
</div></section>

<section><div class="wrap">
<h2>Las viviendas de Murcia y sus cerraduras</h2>
<p>Murcia tiene una mezcla de viviendas muy variada, y cada una tiene sus problemas típicos de cerradura. Conocerlos ayuda a explicar bien por teléfono lo que pasa y a que el cerrajero llegue con lo necesario:</p>
<h3>Pisos del centro y de los barrios</h3>
<p>Edificios de varias épocas con portal de comunidad. En los más antiguos abundan las puertas de madera con bombín básico; en los más recientes, las blindadas y acorazadas. El aviso más habitual: puerta cerrada de golpe al salir al rellano.</p>
<h3>Casas de pueblo y de huerta</h3>
<p>Muy comunes en las pedanías. Puerta directa a la calle, cochera, patio y a veces almacén. Más puertas que vigilar y cerraduras que sufren el sol y la humedad.</p>
<h3>Chalets y urbanizaciones</h3>
<p>En la falda de la sierra y en municipios como Molina de Segura. Cancela de parcela, puerta principal, garaje y cuartos auxiliares; muchas casas pasan temporadas vacías y necesitan más seguridad.</p>
<h3>Locales y naves</h3>
<p>Persianas metálicas, candados y portones. Cuando fallan, suele ser a primera hora, justo cuando hay que abrir.</p>
</div></section>
"""
EXTRA_FAQ["index.html"] = [
    ("¿Venís también en Navidad, Semana Santa o en fiestas como el Bando de la Huerta?",
     "Sí. El servicio funciona todos los días del año. En fechas de fiesta hay más gente en la calle y más llaves perdidas, así que el teléfono sigue atendiendo como cualquier otro día."),
    ("Me han robado en casa, ¿qué hago primero?",
     "Llama al 112 o a la policía y denuncia antes de tocar la puerta, porque pueden querer revisarla. Después, llama al cerrajero para cambiar o reparar la cerradura: no te quedes con una puerta forzada ni una noche."),
]

# ------------------------------------------------------------------ APERTURA
EXTRA["apertura-de-puertas.html"] = """
<section><div class="wrap">
<h2>Cómo se abre una puerta sin romperla</h2>
<p>Cada cerrajero tiene sus herramientas, pero estas son las técnicas más habituales, de menos a más invasiva. Te las contamos para que sepas qué esperar:</p>
<h3>Apertura del resbalón</h3>
<p>Cuando la puerta solo está cerrada de golpe, se actúa sobre el resbalón desde el hueco entre la hoja y el marco con herramientas finas y flexibles. No toca el bombín y, bien hecha, no deja marcas.</p>
<h3>Apertura del bombín con técnica</h3>
<p>Si la llave está echada, se intenta abrir el propio bombín manipulando sus pitones, sin dañarlo. Funciona con muchos bombines corrientes; los de seguridad están diseñados precisamente para impedirlo.</p>
<h3>Extracción del bombín</h3>
<p>Cuando lo anterior no es posible, se extrae el bombín. La puerta y la cerradura quedan bien, pero el bombín hay que cambiarlo: el cerrajero lleva repuestos y lo sustituye antes de irse.</p>
<h3>Taladro</h3>
<p>Es el último recurso, para bombines de alta seguridad o cerraduras bloqueadas. Si te lo plantean, pide que te expliquen por qué no sirven los métodos anteriores.</p>
</div></section>

<section class="alt"><div class="wrap">
<h2>Lo que necesitas tener a mano</h2>
<ul class="list">
<li><strong>Un documento que vincule tu nombre con la dirección</strong>: DNI, contrato de alquiler, escritura o un recibo de luz o agua. En el móvil también vale.</li>
<li><strong>Si no tienes nada encima</strong>, un vecino que te conozca o el propietario de la vivienda por teléfono. Lo que no hará un cerrajero serio es abrir sin ninguna comprobación.</li>
<li><strong>Un medio de pago</strong>: pregunta por teléfono qué formas de pago acepta el cerrajero que va a ir.</li>
</ul>
</div></section>
"""
EXTRA_FAQ["apertura-de-puertas.html"] = [
    ("¿Cuánto se tarda en abrir una puerta?",
     "Una puerta cerrada de golpe suele abrirse en pocos minutos. Con la llave echada o en una acorazada puede llevar bastante más. El cerrajero te da una idea por teléfono cuando le describes la puerta."),
    ("¿Abrís la puerta de casa de un familiar mayor que no contesta?",
     "Si temes que le haya pasado algo, llama primero al 112: los servicios de emergencia pueden entrar de inmediato. Si solo se trata de abrir la puerta con su permiso o el de la familia, el cerrajero lo hará comprobando antes que tenéis relación con la vivienda."),
]

# ------------------------------------------------------------------ CAMBIO
EXTRA["cambio-de-cerraduras.html"] = """
<section class="alt"><div class="wrap">
<h2>Cómo es un cambio de bombín, paso a paso</h2>
<ol class="steps">
<li><strong>Medición</strong>El cerrajero mide el bombín desde el tornillo de sujeción hacia cada lado de la puerta. Así el nuevo queda a ras, sin sobresalir.</li>
<li><strong>Elección</strong>Te enseña las opciones que lleva, de básica a alta seguridad, y te da el precio de cada una antes de cambiar nada.</li>
<li><strong>Cambio</strong>Afloja el tornillo del canto de la puerta, saca el bombín antiguo y coloca el nuevo. En una puerta normal, es cuestión de minutos.</li>
<li><strong>Prueba y entrega</strong>Comprueba que la llave gira suave por los dos lados y que la puerta cierra bien. Te entrega todas las llaves y, si es de seguridad, la tarjeta de propiedad.</li>
</ol>
</div></section>

<section><div class="wrap">
<h2>Otras cerraduras que cambiamos</h2>
<h3>Buzones</h3>
<p>La llave del buzón es de las que más se pierden. La cerradura se cambia en poco tiempo y te llevas llaves nuevas; si el buzón es de un modelo comunitario, el cerrajero busca una cerradura compatible.</p>
<h3>Cerraduras de sobreponer</h3>
<p>Las que van atornilladas por dentro de la puerta, muy frecuentes en puertas de madera antiguas, de patios y de almacenes. Se pueden cambiar por otra igual o sustituir por un cerrojo de seguridad.</p>
<h3>Cerraduras de puertas de garaje y trastero</h3>
<p>Se usan poco y fallan sin avisar. Si la llave cuesta, cambiarlas a tiempo evita quedarte sin poder sacar el coche.</p>
<h3>Cerraduras de portal</h3>
<p>Cuando hay que cambiarlas por pérdida de llaves o por desgaste, la comunidad puede aprovechar para pasar a un sistema amaestrado: cada vecino con una sola llave para su casa y las zonas comunes.</p>
</div></section>
"""
EXTRA_FAQ["cambio-de-cerraduras.html"] = [
    ("¿Cuántas llaves me dan con el bombín nuevo?",
     "Depende del modelo: los básicos suelen traer tres o cinco llaves, y los de seguridad, varias llaves y una tarjeta para pedir copias. Pregunta por teléfono cuántas incluye el bombín que te ofrecen."),
    ("¿Puedo pedir que todas las puertas de casa se abran con la misma llave?",
     "Sí, si todas usan bombín de perfil europeo. Se instalan bombines con la misma combinación, de modo que una sola llave abre la puerta principal, la cochera o el trastero."),
]

# ------------------------------------------------------------------ SEGURIDAD
EXTRA["cerraduras-de-seguridad.html"] = """
<section class="alt"><div class="wrap">
<h2>Cerraduras electrónicas e inteligentes</h2>
<p>Cada vez se piden más: abren con código, huella, tarjeta o el móvil. Son cómodas si en casa entra mucha gente o si alquilas tu vivienda por días, porque puedes dar y quitar accesos sin hacer copias de llaves.</p>
<ul class="list">
<li><strong>Ventajas</strong>: no hay llaves que perder, accesos temporales para familiares o limpieza, y registro de entradas en algunos modelos.</li>
<li><strong>Lo que hay que mirar</strong>: que la parte mecánica sea de seguridad (un bombín malo con un teclado bonito sigue siendo un bombín malo), que tenga apertura de emergencia si se acaban las pilas y que la instalación no debilite la puerta.</li>
</ul>
<h2>Puertas acorazadas: qué revisar si ya tienes una</h2>
<p>Una puerta acorazada es tan segura como su punto más débil. Si tu puerta tiene años, revisa:</p>
<ul class="list">
<li>Que el bombín no sea el original de serie, que en muchas puertas antiguas es básico.</li>
<li>Que tenga escudo protector y que no se mueva.</li>
<li>Que los pestillos laterales y superiores entren bien en el marco y no haya holguras.</li>
<li>Que las bisagras estén protegidas con pivotes antipalanca.</li>
</ul>
<p>En una sola visita, el cerrajero puede cambiar el bombín, poner escudo y ajustar la puerta sin necesidad de cambiarla.</p>
</div></section>
"""
EXTRA_FAQ["cerraduras-de-seguridad.html"] = [
    ("¿Es segura una cerradura inteligente?",
     "Puede serlo si la parte mecánica es de calidad y tiene apertura de emergencia. Lo importante no es el teclado o la aplicación, sino el cilindro y la cerradura que hay detrás."),
    ("¿Cada cuánto conviene revisar la seguridad de la puerta?",
     "Cuando cambias de vivienda, tras perder llaves o sufrir un intento de robo, y como norma general cada pocos años, porque los métodos de apertura evolucionan y los bombines se desgastan."),
]

# ------------------------------------------------------------------ ZONAS
EXTRA["cerrajero-molina-de-segura.html"] = """
<section><div class="wrap">
<h2>Seguridad en chalets de Molina: lo que más recomendamos</h2>
<p>En una vivienda con parcela, el ladrón tiene más sitios por donde intentarlo y más tiempo, porque los vecinos están más lejos. Estos son los puntos que más se refuerzan en las urbanizaciones de Molina:</p>
<ol class="list">
<li><strong>Puerta principal</strong>: bombín antibumping y antiextracción con escudo protector. Si la puerta es blindada antigua, revisar bisagras y pestillos.</li>
<li><strong>Puerta de garaje</strong>: muchas comunican directamente con la casa. Su cerradura debería ser tan buena como la de la puerta principal.</li>
<li><strong>Cancela de la parcela</strong>: no evita que salten la valla, pero un buen cierre retrasa y disuade.</li>
<li><strong>Cuartos de piscina y almacén</strong>: guardan herramientas que pueden usarse para forzar la casa. Un candado de arco protegido es suficiente.</li>
</ol>
<p>Antes de irte de vacaciones, revisa que todas las cerraduras funcionan bien: es peor descubrir un bombín agarrotado al volver, con las maletas en la puerta.</p>
</div></section>
"""
EXTRA_FAQ["cerrajero-molina-de-segura.html"] = [
    ("¿Atendéis también el casco urbano de Molina, no solo urbanizaciones?",
     "Sí, todo el municipio: pisos y casas del casco urbano, urbanizaciones y pedanías. Al llamar, di la calle y, si es una urbanización, su nombre."),
]

EXTRA["cerrajero-alcantarilla.html"] = """
<section><div class="wrap">
<h2>Cuándo cambiar la cerradura en un piso de Alcantarilla</h2>
<p>Muchos pisos de Alcantarilla cambian de manos o de inquilino con frecuencia, y las llaves antiguas siguen circulando. Cambia el bombín si:</p>
<ul class="list">
<li>Acabas de comprar o alquilar el piso.</li>
<li>Has perdido las llaves o te han robado el bolso o la cartera con documentación.</li>
<li>Notas marcas alrededor del bombín, como arañazos o golpes: puede ser un intento de apertura.</li>
<li>La llave entra dura o hay que «buscarle el punto» para que gire.</li>
</ul>
<p>Si te preocupa la seguridad, aprovecha el cambio para poner un <a href="cerraduras-de-seguridad.html">bombín de seguridad con escudo</a>; en una puerta de piso es la mejora con mejor resultado por lo que cuesta.</p>
</div></section>
"""
EXTRA_FAQ["cerrajero-alcantarilla.html"] = [
    ("He visto arañazos alrededor del bombín, ¿qué hago?",
     "Pueden ser marcas de un intento de apertura. Haz fotos, denúncialo si lo crees necesario y cambia el bombín por uno de seguridad, aunque la puerta siga abriendo bien."),
]

EXTRA["cerrajero-el-palmar.html"] = """
<section><div class="wrap">
<h2>Locales y negocios en El Palmar</h2>
<p>El Palmar tiene mucho comercio de barrio y negocios con persiana metálica a pie de calle. Cuando una persiana no abre a primera hora, cada minuto cuenta:</p>
<ul class="list">
<li><strong>Cerradura de persiana bloqueada</strong>: suele deberse a suciedad o desgaste. Se abre y se cambia la cerradura si hace falta.</li>
<li><strong>Candado que no abre o roto</strong>: se abre o se corta y se sustituye por uno de arco protegido.</li>
<li><strong>Intento de robo nocturno</strong>: si ves la cerradura forzada al llegar, denuncia y llama para reponerla el mismo día.</li>
</ul>
<p>Para negocios con varios empleados, un sistema de llaves amaestradas permite que cada persona abra solo lo que necesita.</p>
</div></section>
"""
EXTRA_FAQ["cerrajero-el-palmar.html"] = [
    ("Tengo un local en El Palmar y no abre la persiana, ¿venís temprano?",
     "Sí, a cualquier hora. Indica si el problema es la cerradura, el candado o el motor de la persiana para que el cerrajero sepa qué llevar."),
]

EXTRA["cerrajero-puente-tocinos.html"] = """
<section><div class="wrap">
<h2>Cuidar las cerraduras de una casa de huerta</h2>
<p>Las cerraduras exteriores de las casas de huerta sufren más que las de un piso: sol, humedad del riego, polvo y años de uso. Con unos cuidados sencillos duran mucho más:</p>
<ul class="list">
<li><strong>Lubrica con grafito o un spray específico para cerraduras</strong> un par de veces al año. Nunca aceite de cocina ni grasa, que atrapan el polvo.</li>
<li><strong>Protege los candados</strong> de la lluvia con un capuchón o colocándolos con el ojo hacia abajo.</li>
<li><strong>No fuerces una llave que no gira</strong>: si se parte dentro, el arreglo es más complicado.</li>
<li><strong>Cambia a tiempo</strong> las cerraduras de puertas que se usan poco, como el almacén o la puerta trasera.</li>
</ul>
</div></section>
"""
EXTRA_FAQ["cerrajero-puente-tocinos.html"] = [
    ("¿Qué lubricante uso para la cerradura de la puerta de la calle?",
     "Grafito en polvo o un spray específico para cerraduras. Evita el aceite de cocina y las grasas, porque con el polvo forman una pasta que acaba bloqueando el bombín."),
]

EXTRA["cerrajero-espinardo-churra.html"] = """
<section><div class="wrap">
<h2>Si alquilas tu piso a estudiantes</h2>
<p>Si eres propietario de un piso para estudiantes en Espinardo, la rotación de inquilinos cada curso hace que las llaves se multipliquen. Algunas ideas que facilitan la gestión:</p>
<ul class="list">
<li><strong>Cambia el bombín entre un curso y el siguiente</strong>, o al menos cuando se va un inquilino que no ha devuelto todas las llaves.</li>
<li><strong>Bombín con tarjeta de propiedad</strong>: solo tú puedes pedir copias, así controlas cuántas llaves hay.</li>
<li><strong>Cerradura electrónica</strong> con códigos por inquilino: das y quitas accesos sin cambiar nada.</li>
<li><strong>Cerraduras en las habitaciones</strong>, si se alquilan por separado.</li>
</ul>
</div></section>
"""
EXTRA_FAQ["cerrajero-espinardo-churra.html"] = [
    ("Soy propietario de un piso de estudiantes, ¿cómo controlo las copias de llaves?",
     "Instala un bombín con tarjeta de propiedad: las copias oficiales solo se hacen presentando esa tarjeta, que tienes tú. Otra opción es una cerradura electrónica con un código por inquilino."),
]

EXTRA["cerrajero-cabezo-de-torres.html"] = """
<section><div class="wrap">
<h2>Puertas de madera antiguas: arreglar antes que cambiar</h2>
<p>Muchas casas de Cabezo de Torres conservan puertas de calle de madera maciza que merece la pena mantener. No hace falta cambiar la puerta para que sea segura:</p>
<ul class="list">
<li><strong>Cerradura nueva en la misma caja</strong> si la antigua está desgastada, respetando el aspecto de la puerta.</li>
<li><strong>Cerrojo de seguridad adicional</strong> por dentro, que no se ve desde la calle.</li>
<li><strong>Bombín de seguridad</strong> con escudo discreto en el color de los herrajes.</li>
<li><strong>Revisión del marco</strong>: si la madera está deteriorada donde entra el pestillo, una placa de refuerzo evita que ceda con una patada.</li>
</ul>
</div></section>
"""
EXTRA_FAQ["cerrajero-cabezo-de-torres.html"] = [
    ("¿Se puede poner una cerradura de seguridad en una puerta de madera antigua?",
     "Sí. Se puede añadir un cerrojo de seguridad, cambiar el bombín por uno de alta seguridad con escudo y reforzar el marco, sin cambiar la puerta ni su aspecto."),
]

EXTRA["cerrajero-la-alberca-santo-angel.html"] = """
<section><div class="wrap">
<h2>Antes de cerrar la casa de verano</h2>
<p>Si tu casa de La Alberca o Santo Ángel se queda vacía unos meses, dedica un rato a esta lista antes de irte:</p>
<ol class="list">
<li>Comprueba que todas las cerraduras giran suaves; si alguna cuesta, cámbiala ahora y no a la vuelta.</li>
<li>Deja una copia de la llave a alguien de confianza que pueda pasar a revisar.</li>
<li>Asegura almacenes y cuartos auxiliares con candados de arco protegido.</li>
<li>No dejes escaleras ni herramientas a la vista en la parcela.</li>
<li>Si alguna cerradura es antigua, valora cambiarla por una de seguridad antes de la temporada.</li>
</ol>
<p>Y si a la vuelta la llave no entra o la cerradura está bloqueada, llama: es un aviso frecuente en casas que llevan tiempo cerradas.</p>
</div></section>
"""
EXTRA_FAQ["cerrajero-la-alberca-santo-angel.html"] = [
    ("Al volver a la casa después del verano la llave no entra, ¿qué pasa?",
     "Puede ser suciedad, óxido o, a veces, un intento de manipulación. No fuerces la llave: llama y el cerrajero abrirá y revisará si hay que cambiar el bombín."),
]

EXTRA["cerrajero-beniajan-torreaguera.html"] = """
<section><div class="wrap">
<h2>Seguridad para almacenes y casas con patio</h2>
<p>En Beniaján y Torreagüera muchas viviendas tienen patio trasero o almacén con salida a otra calle o a la huerta. Esa segunda puerta suele ser la menos cuidada y la más tentadora para quien quiere entrar sin ser visto.</p>
<ul class="list">
<li>Ponle a la puerta trasera un <strong>cerrojo de seguridad</strong> por dentro, además de la cerradura.</li>
<li>Si el almacén comunica con la casa, trata su puerta como si fuera la principal.</li>
<li>Usa <strong>bombines con la misma llave</strong> para no tener un manojo enorme.</li>
<li>Revisa que las bisagras de las puertas metálicas no se puedan desmontar desde fuera.</li>
</ul>
</div></section>
"""
EXTRA_FAQ["cerrajero-beniajan-torreaguera.html"] = [
    ("¿Qué cerradura pongo en la puerta trasera del patio?",
     "Lo más eficaz es una cerradura en buen estado más un cerrojo de seguridad por dentro. Si la puerta es metálica, revisa también que las bisagras no se puedan sacar desde fuera."),
]

# ------------------------------------------------------------------ CÓMO TRABAJAMOS / CONTACTO
EXTRA["contacto.html"] = """
<section><div class="wrap">
<h2>Horario de atención</h2>
<p>El teléfono atiende <strong>las 24 horas, los 7 días de la semana</strong>, incluidos festivos. Para urgencias, llama siempre: un mensaje de WhatsApp puede tardar más en verse que una llamada. Usa WhatsApp para mandar la ubicación o una foto de la cerradura una vez hayas hablado con el cerrajero.</p>
<h2>Si llamas de parte de una comunidad o empresa</h2>
<p>Administradores de fincas, presidentes de comunidad y negocios pueden llamar al mismo número para trabajos programados: cambio de cerraduras de portal, amaestramiento de llaves o revisión de la seguridad de un local. Indica que no es una urgencia y el cerrajero te propondrá día y hora.</p>
</div></section>
"""

# ------------------------------------------------------------------ AMPLIACIÓN DE ZONAS CORTAS
EXTRA["cerrajero-centro-murcia.html"] = """
<section><div class="wrap">
<h2>Oficinas y despachos del centro</h2>
<p>Además de viviendas y comercios, el centro de Murcia concentra despachos, consultas y oficinas en entreplantas y primeros pisos. Cuando se pierde la llave de una oficina o un empleado se va sin devolverla, lo prudente es cambiar el bombín de inmediato: en una oficina hay documentación, equipos y datos de clientes.</p>
<p>Para despachos con varias personas, un sistema de llaves amaestradas permite que cada uno abra solo su puerta y las zonas comunes, mientras que el responsable tiene una llave que lo abre todo. Si quieres valorarlo, llama al mismo teléfono e indica que no es una urgencia.</p>
</div></section>
"""
EXTRA["cerrajero-campo-de-murcia.html"] = """
<section><div class="wrap">
<h2>Urbanizaciones de golf y viviendas de temporada</h2>
<p>En el Campo de Murcia hay urbanizaciones con muchos propietarios que pasan aquí solo parte del año. En estas casas se repiten tres situaciones: la llave que no entra al volver tras meses fuera, la cerradura dañada por un intento de apertura mientras la casa estaba vacía y el familiar o vecino que necesita entrar para revisar la casa y no tiene llave.</p>
<p>Si eres propietario, deja una copia de la llave a alguien de confianza en la zona, revisa la seguridad de la puerta antes de cerrar la casa por temporada y, si la cerradura es antigua, cámbiala por un <a href="cerraduras-de-seguridad.html">bombín de seguridad con escudo</a>. Un bombín con tarjeta de propiedad te permite saber cuántas copias existen aunque estés lejos.</p>
</div></section>
"""
EXTRA["cerrajero-sangonera-la-verde.html"] = """
<section><div class="wrap">
<h2>Patios traseros y puertas de garaje</h2>
<p>En los adosados de Sangonera la Verde, el patio trasero y la puerta del garaje suelen comunicar directamente con la casa. Son accesos que se usan a diario y se cuidan menos que la puerta principal. Revisa que la puerta del patio tenga una cerradura en buen estado y, si es de aluminio o PVC, que no se pueda abrir haciendo palanca. En la puerta del garaje, el bombín debería ser tan bueno como el de la puerta principal.</p>
<p>Si tienes niños que vuelven solos del colegio, una cerradura electrónica con código puede ahorrarte más de una llamada al cerrajero por llaves olvidadas.</p>
</div></section>
"""
EXTRA["cerrajero-algezares-los-garres.html"] = """
<section><div class="wrap">
<h2>Romerías, fiestas y llaves perdidas</h2>
<p>En los días de mucha gente en la subida a la Fuensanta y en las fiestas de las pedanías, es habitual que se pierdan llaves o que alguien vuelva a casa de madrugada y no pueda entrar. Si te pasa, antes de llamar revisa con calma bolsos y bolsillos y pregunta a quien te acompañaba. Si no aparecen y las llaves llevaban algo que identifique tu casa, cambia el bombín cuanto antes, aunque sea de noche.</p>
<p>Y si vives en una casa con parcela y varias puertas, aprovecha para dejar todas con la misma llave: la próxima vez solo tendrás que preocuparte por un llavero.</p>
</div></section>
"""
EXTRA["cerrajero-guadalupe-la-nora.html"] = """
<section><div class="wrap">
<h2>Residenciales con zonas comunes</h2>
<p>Muchas urbanizaciones de Guadalupe tienen piscina, garaje comunitario y trasteros, cada uno con su llave. Cuando un vecino pierde un llavero, la comunidad se plantea si cambiar las cerraduras comunes. Un sistema amaestrado con tarjeta de propiedad evita ese problema: cada vecino lleva una sola llave, que abre su casa y las zonas comunes, y las copias solo se hacen con autorización. Lo explicamos en <a href="cerrajeria-para-comunidades.html">cerrajería para comunidades</a>.</p>
</div></section>
"""
EXTRA["cerrajero-las-torres-de-cotillas.html"] = """
<section><div class="wrap">
<h2>Casas con cochera en el casco urbano</h2>
<p>En el casco urbano de Las Torres de Cotillas son muy habituales las casas de dos plantas con cochera a la calle. Esa puerta de cochera es, muchas veces, la entrada que más se usa: se abre varias veces al día y su cerradura se desgasta antes que la de la puerta principal. Si notas que la llave entra dura o hay que buscarle el punto, cámbiala antes de que te deje el coche dentro.</p>
<p>Y si la cochera comunica con la vivienda, trátala como una puerta principal: bombín de seguridad, escudo protector y, si es una puerta basculante, un cerrojo interior.</p>
</div></section>
"""
EXTRA["cerrajero-santomera.html"] = """
<section><div class="wrap">
<h2>Pisos y casas del núcleo urbano</h2>
<p>En el centro de Santomera conviven bloques de pisos con portal de comunidad y casas de pueblo con puerta directa a la calle. En los pisos, la urgencia más frecuente es la puerta cerrada de golpe; en las casas, la cerradura antigua que deja de girar. En ambos casos, el cerrajero abre sin romper siempre que se pueda y, si hace falta, cambia el bombín en la misma visita.</p>
<p>Si vives de alquiler, avisa al propietario antes de cambiar la cerradura y guarda el bombín antiguo. Y si eres propietario, cambia el bombín cada vez que cambie el inquilino.</p>
</div></section>
"""
