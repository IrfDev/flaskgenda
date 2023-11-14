# Make an app to being used as an agenda with users that can manage contacts

Agenda de contactos

- Permite crer un usuario de la agenda y crear contactos relacionados a ese usuario
- Un usuario solo va a poder tener acceso (crear, modificar, ver y eliminar) a sus propios contactos
- Datos del contacto: primer_nombre, segundo_nombre, email, telefono_casa, movil

endpoints:
    POST /api/users/ -> crear un nuevo usuario
    POST /api/token/ -> crea los tokens de acceso y de actualizacion
    POST /api/token/refresh/ -> actualiza un token

    GET       /api/contacts/ -> consultar todos los contactos DEL USUARIO
    POST      /api/contacts/ -> crea un nuevo contacto
    GET       /api/contacts/:pk -> muestra los detalles de un contacto
    PATCH/PUT /api/contacts/:pk -> modifica un contacto
    DELETE    /api/contacts/:pk -> elimina un contacto


