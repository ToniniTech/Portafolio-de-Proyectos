## Dominio: Sistemas de ordenes 

---

"Un sistema ecommerce (comercio electrónico) es la plataforma tecnológica y el conjunto de procesos para vender y comprar productos o servicios por internet"
### Entidades

#### Usuario

-- Debe tener ID

-- Puede crear ordenes (cliente)

-- Debe tener un solo carrito (cliente)

-- Puede pagar ordenes (cliente)

-- tener rol (admin/cliente)


#### Producto

-- Debe tener ID

-- Debe tener precio

-- Debe tener nombre

-- Debe mostrar si existe stock o no 

#### Orden

-- Debe tener un ID de usuario

-- Debe tener un ID de compra

-- Debe tener fecha de compra

-- Debe tener precio total de la orden incluyendo impuesto y envíos

-- Debe tener cantidad total por producto y cantidad cantidad total de productos

-- Tiene estados: pendiente, cancelado, pagado, enviado

#### Carrito

-- Es una entidad persistente

-- Tiene id

-- Tiene un usuario id (comprador)

-- Debe tener productos + cantidades

-- Estado (pendiente, activo, abandonado)

#### Envio

-- Debe tener una orden_id

-- Debe tener un ID de envío

-- Debe tener dirección

-- Debe tener tiempos aprox de llegada del pedido

-- Tiene estado (procesando, enviado, recibido)

-- Un envío puede tener solo una orden


#### Reglas 

-- No se puede pagar un producto sin stock disponible

-- No se puede pagar sin un medio de pago de digital

-- No se puede cambiar una compra una vez ha sido enviada

-- El stock nunca puede ser negativo

-- Se congela el precio una vez la orden esta pendiente


