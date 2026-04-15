### ARCHIVO Y GESTIÓN DE AERONAVES ###

Este programa sirve para archivar datos de aeronaves, horas de uso, componentes y emite alertas de mantenimiento cuando es necesario. Hecho por Samuel Mejía Bravo de ID 000531329.

Al ser tantas funciones lo separé en varios archivos para no cargar uno solo con tantas líneas de código. Cada aeronave se guarda en un .json y sus componentes en otro, esto para no cargar un solo diccionario y el uso del .json es para conservar los datos cada que se cierra y se vuelve a utilizar el programa, de lo contrario no se guardarían.

Además, utilicé el apoyo de Inteligencia Artificial a la hora de hacer el .gitignore y al separar todo el archivo de funciones por partes por ahorrar tiempo de copiar, pegar y reescribir comandos de inserción de módulos.

Para utilizar el programa sólo se debe ejecutar el documento .src y tener python instalado.

El programa automáticamente elimina los datos caché almacenados por sesiones anteriores así que no es una preocupación para el usuario tener que borrarlas manualmente. Para esta función pedí ayuda a Copilot porque no me estaba funcionando bien. El problema resultó ser más sencillo de lo que creía y la IA no lo solucionaba bien. Aprendí por mí mismo a hacerlo y comprobé que funciona.

Está todo "documentado" en el programa mismo. Cada función tiene un título descriptivo para saber rápidamente adónde dirigirse en caso de encontrar un error en el programa.