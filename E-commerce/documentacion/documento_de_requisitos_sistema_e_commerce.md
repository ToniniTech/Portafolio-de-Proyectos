# Documento de Requisitos Funcionales y de Dominio

## 1. Introducción
Este documento describe los requisitos funcionales y reglas de negocio de un sistema de comercio electrónico basado en el modelo entidad–relación provisto (usuarios, productos, carrito, órdenes y envíos). Su objetivo es servir como base para el diseño técnico y la implementación.

## 2. Alcance del sistema
El sistema permitirá a usuarios registrados seleccionar productos, gestionarlos en un carrito de compras, confirmar órdenes y realizar el seguimiento de envíos.

## 3. Actores
- **Usuario**: Persona que navega, agrega productos al carrito y realiza compras.
- **Sistema**: Lógica interna que valida reglas y estados.

## 4. Casos de uso

### CU-01 Registrar usuario
**Actor:** Usuario
**Descripción:** Permite registrar un nuevo usuario en el sistema.
**Flujo principal:**
1. El usuario ingresa sus datos personales.
2. El sistema valida unicidad de email y rut.
3. El sistema crea el usuario.

---

### CU-02 Agregar producto al carrito
**Actor:** Usuario
**Descripción:** Permite agregar un producto al carrito activo.
**Precondición:** El usuario tiene un carrito activo.
**Flujo principal:**
1. El usuario selecciona un producto.
2. Indica la cantidad.
3. El sistema agrega el producto al carrito.

**Reglas:**
- El carrito debe estar en estado activo.

---

### CU-03 Confirmar orden
**Actor:** Usuario
**Descripción:** Convierte el carrito en una orden de compra.
**Precondición:** El carrito contiene al menos un producto.
**Flujo principal:**
1. El usuario confirma la compra.
2. El sistema crea la orden.
3. El sistema calcula el total.
4. El sistema cambia el estado de la orden a confirmada.

## 5. Reglas de negocio

- RN-01: Un carrito solo puede modificarse si su estado es activo.
- RN-02: El subtotal de un detalle de orden es cantidad × precio unitario.
- RN-03: El total de una orden es la suma de sus subtotales.
- RN-04: Una orden confirmada no puede modificarse.
- RN-05: Un envío solo puede crearse a partir de una orden confirmada.

## 6. Estados y transiciones

### Carrito
- Estados: activo, cerrado
- Transiciones:
  - activo → cerrado (al confirmar orden)

### Orden
- Estados: creada, confirmada, pagada, cancelada
- Transiciones:
  - creada → confirmada
  - confirmada → pagada
  - creada → cancelada

### Envío
- Estados: pendiente, enviado, entregado
- Transiciones:
  - pendiente → enviado
  - enviado → entregado

## 7. Consideraciones técnicas
- La lógica de negocio se implementará en el dominio (clases y métodos).
- El modelo ER se usará exclusivamente para persistencia de datos.

## 8. Glosario
- **Carrito activo:** Carrito que aún acepta modificaciones.
- **Orden confirmada:** Orden validada y lista para pago/envío.

---
Documento preparado como base para diseño UML y posterior implementación en Python.

