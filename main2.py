from sistemainventario import *

p1=Producto("coca",15, 20)
p1.descuento(0.5)
p2 = Producto("Pepsi 600ml", 14, 30)
p3 = Producto("Agua Mineral 1L", 18, 15)
p4 = Producto("Papas Saladas", 17, 50)
p5 = Producto("Galletas de Chocolate", 22, 40)
p6 = Producto("Jugo de Naranja 1L", 25, 12)

# Lácteos y Refrigerados
p7 = Producto("Leche Entera 1L", 26, 20)
p8 = Producto("Yogurt de Fresa", 12, 25)
p9 = Producto("Queso Panela 400g", 65, 10)
p10 = Producto("Mantequilla 90g", 28, 18)
p11 = Producto("Jamón de Pavo 250g", 55, 15)

# Despensa
p12 = Producto("Arroz Blanco 1kg", 32, 45)
p13 = Producto("Frijol Negro 1kg", 38, 40)
p14 = Producto("Aceite Vegetal 1L", 42, 22)
p15 = Producto("Pasta para Sopa", 10, 60)
p16 = Producto("Café Soluble 100g", 85, 10)
p17 = Producto("Azúcar Estándar 1kg", 28, 35)

# Limpieza y Cuidado Personal
p18 = Producto("Detergente Multiusos 1kg", 35, 20)
p19 = Producto("Jabón de Tocador", 18, 50)
p20 = Producto("Champú 400ml", 75, 12)
p21 = Producto("Pasta de Dientes", 35, 30)
p22 = Producto("Papel Higiénico 4 rollos", 28, 25)

# Otros / Papelería
p23 = Producto("Cuaderno Profesional", 45, 15)
p24 = Producto("Bolígrafo Tinta Negra", 8, 100)
p25 = Producto("Pilas AA 4 pack", 120, 8)
p26 = Producto("Cereal de Maíz", 55, 14)

cat1=Categoria("despensa")
cat1.nuevop(p12)
cat1.nuevop(p13)
cat1.nuevop(p14)
cat1.nuevop(p15)

cat1.valor()

maquillaje= Categoria("maquillaje")
ropa= Categoria("ropa")

p27= Producto("labial", 150,90)
p28=Producto("chamarra",200,100)

maquillaje.nuevop(p27)
ropa.nuevop(p28)

pedido1=Pedido("marcos", p28)
print("\ntotal del pedido con iva:", pedido1.calcular_total())
pedido1.finalizar_p()

tienda= Tienda("tienda")
tienda.rcategoria(maquillaje)
tienda.rcategoria(ropa)

tienda.pedidosr.append(pedido1)

print("\n reporte")
tienda.greporte()

tienda.productocaro()