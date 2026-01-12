# Proyecto E-commerce (En Desarrollo)

##  Descripción General

Este proyecto corresponde a la implementación de un **sistema básico de carrito de compras**, orientado a un contexto de comercio electrónico. El diseño sigue principios de **programación orientada a objetos** y algunos conceptos de **Domain-Driven Design (DDD)**, como entidades, value objects y aggregate roots.

Actualmente, el proyecto se encuentra en **fase de implementación**, por lo que existen métodos y módulos que aún no están completamente desarrollados (`pass`). El objetivo principal es modelar el dominio antes de cerrar la lógica de negocio.

---

## 🧩 Estructura del Proyecto

```
├── carrito.py
├── carrito_detalle.py
├── usuario.py
├── direccion.py
├── envio.py
```

---

## 📦 Módulos y Estado de Avance

### `carrito.py`

**Estado:** 🟡 Parcialmente implementado

Define la entidad **Carrito**, que representa el carrito de compras del usuario.

**Responsabilidades:**

* Mantener el estado del carrito (activo / inactivo).
* Agregar, eliminar y editar productos.
* Validar existencia de productos en el catálogo.

**Clases principales:**

* `estadoCarrito (Enum)`
* `Carrito`

**Pendiente:**

* Implementación del método `VerificarStock()`.

---

### `carrito_detalle.py`

**Estado:** 🟡 Parcialmente implementado

Representa el detalle de un producto dentro del carrito.

**Responsabilidades:**

* Almacenar producto y cantidad.
* Calcular subtotales y totales.

**Métodos implementados:**

* `CalcularSubTotal()`
* `CalcularTotal()`

**Pendiente:**

* `CalcularEnvio()`
* `CalcularImpuestos()`
* `AplicarDescuentos()`
* `ObtenerItems()`

---

###  `usuario.py`

**Estado:** 🟡 Parcialmente implementado

Define la entidad **Usuario** y su gestor.

**Responsabilidades:**

* Registro de usuarios.
* Validación y hash de contraseñas (bcrypt).
* Manejo de dirección del usuario.

**Clases principales:**

* `Usuario`
* `gestorUsuarios`

**Pendiente / Observaciones:**

* Método `login()` no implementado.
* Error lógico en `cambiar_direccion()` (`==` en vez de `=`).
* El constructor de `Usuario` espera `direccion`, pero no se envía al registrar.

---

### `direccion.py`

**Estado:** 🟢 Implementación base completa

Define el **Value Object Dirección**, separado del usuario por composición.

**Responsabilidades:**

* Representar una dirección como valor inmutable.
* Comparar direcciones por valor.

**Clases principales:**

* `Direccion`
* `GestorDirecciones` (pendiente de implementación)

**Pendiente:**

* Implementar lógica en `GestorDirecciones`.
* Corrección menor en el método `__eq__` (comparación del número).

---

### `envio.py`

**Estado:** 🔴 En desarrollo

Modela el concepto de **envío** asociado a una dirección y usuario.

**Responsabilidades esperadas:**

* Registrar envíos.
* Asociar dirección y estado del envío.

**Pendiente:**

* Implementación completa del método `registrar_envio()`.
* Definición de estados de envío.

---

## Conceptos Aplicados

* Programación Orientada a Objetos (POO)
* Domain-Driven Design (DDD)

  * Entidades (`Usuario`, `Carrito`)
  * Value Objects (`Direccion`)
  * Aggregate Root (`Usuario`)
* Seguridad básica de contraseñas con `bcrypt`

---

## 🚧 Estado del Proyecto

🔧 **Fase actual:** Implementación

El proyecto aún no es funcional en su totalidad. Varias clases y métodos se encuentran en desarrollo, ya que el foco principal ha sido el modelado del dominio y la estructura del sistema.

---

## Notas

Este README describe el estado actual del proyecto según el avance del código. No representa una versión final del sistema, sino una referencia del trabajo realizado hasta el momento.

