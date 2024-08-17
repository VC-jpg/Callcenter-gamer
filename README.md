# Call Center Gamer

¡Bienvenido al repositorio del **Call Center Gamer**! Este sistema de soporte técnico ha sido diseñado especialmente para los amantes de los videojuegos, proporcionando una solución completa para la gestión de preguntas frecuentes y problemas técnicos. Desarrollado con HTML, CSS y JavaScript, este proyecto ofrece una interfaz intuitiva que permite a los usuarios resolver sus dudas de manera rápida y eficiente, mientras que los administradores pueden gestionar las consultas con facilidad.

## Descripción General

El **Call Center Gamer** es una plataforma web diseñada para ofrecer soporte técnico especializado a gamers. El sistema no solo facilita la consulta de preguntas frecuentes, sino que también permite a los usuarios enviar nuevas preguntas y recibir respuestas de manera organizada y accesible. Con una interfaz moderna y amigable, el sistema está optimizado para brindar una experiencia de usuario simple tanto para jugadores como para administradores.

### Funcionalidades Principales

#### 1. **Interfaz de Usuario Amigable**

La plataforma cuenta con una landing page, diseñada por Figma como paso inicial para asegurar un diseño moderno y responsivo. Esta página inicial tiene como objetivo captar la atención del usuario proporcionando un acceso rápido a las secciones más importantes del sistema, como las preguntas frecuentes, el inicio de sesión y el registro.


#### 2. **Página de Inicio de Sesión y Registro**

El sistema incluye formularios de inicio de sesión y registro para los usuarios, con validaciones implementadas en **JavaScript** para asegurar que los datos ingresados sean correctos antes de ser enviados. Además, se ha implementado protección contra ataques de Cross-Site Request Forgery (**CSRF**) para garantizar la seguridad de las cuentas de usuario.

- **Validación de Formularios**: Uso de **JavaScript** para validar campos obligatorios, verificar contraseñas y asegurar que los correos electrónicos tengan el formato correcto.
- **Seguridad Mejorada**: Protección CSRF y contraseñas cifradas integrada para prevenir ataques y asegurar que los datos de los usuarios estén protegidos.

#### 3. **Gestión Eficiente de Preguntas y Respuestas**

Una de las funcionalidades clave del sistema es la gestión de preguntas y respuestas. Los usuarios pueden enviar preguntas técnicas directamente desde la plataforma, las cuales son revisadas y respondidas por los administradores. Las respuestas se presentan de manera clara, y tanto las preguntas como las respuestas se almacenan en un sistema organizado que facilita su consulta y gestión.

- **Envío de Preguntas**: Los usuarios pueden enviar nuevas preguntas utilizando un formulario simple y directo. 
- **Administración de Contenidos**: Los administradores tienen acceso a una interfaz donde pueden revisar, responder y administrar todas las preguntas recibidas. Esta sección está diseñada para ser clara y eficiente, tan solo con su nombre de usuario y contraseña la cúal ya está registrada como administrador en la base de datos.


### Tecnologías Utilizadas

- **HTML/CSS**: Estructura básica del sistema, proporcionando una base sólida para el contenido y la interfaz.
- **JavaScript**: Lógica del lado del cliente para la validación de formularios y la mejora de la interacción del usuario con la plataforma.
- **Bootstrap**: Framework CSS que asegura un diseño consistente y adaptable a diferentes dispositivos y resoluciones.
- **Django/MySQL**: Backend encargado de la base de datos y gestor de todos los elementos del sitio que pueden administrar.

## Cómo Ejecutar el Proyecto

1. **Clona el Repositorio**
   ```bash
   git clone https://github.com/VC-jpg/call-center-gamer.git
   ```

2. **Abre el Proyecto en tu Navegador**
   Una vez clonado, puedes abrir el archivo `index.html` en tu navegador para ver la landing page y explorar las funcionalidades del sistema.

3. **Personaliza el Proyecto**
   Puedes modificar los archivos HTML, CSS o JavaScript según tus necesidades para personalizar el sistema o agregar nuevas funcionalidades.

## Contribuciones

Este proyecto está abierto a contribuciones de la comunidad. Si tienes ideas para mejorar el sistema o encuentras algún error, no dudes en abrir un issue o enviar un pull request. Agradezco cualquier aporte que nos ayude a mejorar esta plataforma de soporte técnico para gamers.

---

2023
