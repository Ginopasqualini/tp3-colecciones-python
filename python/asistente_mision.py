"""
═══════════════════════════════════════════════════════════════════════════════
    PROGRAMA: ASISTENTE DE MISIÓN ESPACIAL (TP3 - COLECCIONES EN PYTHON)
    Laboratorio de Aplicaciones II - 6° G - 2026
    
    Objetivo: Implementar el uso de estructuras de datos (listas, tuplas y
    conjuntos) dentro de una interfaz de consola funcional.
═══════════════════════════════════════════════════════════════════════════════
"""

def mostrar_menu():
    """Muestra las opciones del sistema de control."""
    print("\n" + "="*70)
    print("🚀 SISTEMA DE CONTROL LUNAR - ASISTENTE DE MISIÓN ESPACIAL 🚀")
    print("="*70)
    print("1. 🎵 Gestión de Playlist Dinámica (Listas)")
    print("2. 📊 Cálculo de Promedio de Calificaciones (Funciones de Listas)")
    print("3. 📦 Inventario de Productos (Listas + Tuplas)")
    print("4. 🗺️  Coordenadas y Desempaquetado (Tuplas)")
    print("5. 👥 Registro de Invitados Únicos (Sets/Conjuntos)")
    print("6. 🚪 Salir")
    print("="*70)


def opcion_1_playlist():
    """OPCIÓN 1: Gestión de Playlist Dinámica (Listas)"""
    print("\n🎵 OPCIÓN 1: GESTIÓN DE PLAYLIST DINÁMICA")
    print("-" * 70)
    
    playlist_mision = []
    
    try:
        cantidad = int(input("¿Cuántas canciones deseas agregar a la lista?: "))
        
        if cantidad <= 0:
            print("⚠️  Por favor, ingresa un número mayor a 0.")
            return
        
        # Carga dinámica de canciones usando for con range
        for i in range(cantidad):
            cancion = input(f"Proporciona la canción {i + 1}: ").strip()
            if cancion:  # Validar que no esté vacía
                playlist_mision.append(cancion)
        
        if not playlist_mision:
            print("⚠️  No se agregaron canciones válidas.")
            return
        
        # Ordenar alfabéticamente
        print("\n¿Cómo deseas ordenar la lista?")
        print("1. Ascendente (A-Z)")
        print("2. Descendente (Z-A)")
        orden = input("Selecciona (1 o 2): ").strip()
        
        if orden == "1":
            playlist_mision.sort()
            print("\n📋 Playlist ordenada ASCENDENTE (A-Z):")
        elif orden == "2":
            playlist_mision.sort(reverse=True)
            print("\n📋 Playlist ordenada DESCENDENTE (Z-A):")
        else:
            playlist_mision.sort()
            print("\n📋 Playlist (orden por defecto - Ascendente):")
        
        # Mostrar la lista final
        for idx, cancion in enumerate(playlist_mision, 1):
            print(f"  {idx}. 🎶 {cancion}")
        
        print(f"\n✅ Total de canciones en la playlist: {len(playlist_mision)}")
        
    except ValueError:
        print("⚠️  Error: Por favor, ingresa un número entero válido.")


def opcion_2_promedio():
    """OPCIÓN 2: Cálculo de Promedio de Calificaciones (Funciones de Listas)"""
    print("\n📊 OPCIÓN 2: CÁLCULO DE PROMEDIO DE CALIFICACIONES")
    print("-" * 70)
    
    calificaciones = []
    
    try:
        cantidad = int(input("¿Cuántas calificaciones deseas evaluar?: "))
        
        if cantidad <= 0:
            print("⚠️  Por favor, ingresa un número mayor a 0.")
            return
        
        # Carga dinámica de calificaciones
        for i in range(cantidad):
            while True:
                try:
                    nota = float(input(f"Ingresa la calificación {i + 1} (0-10): "))
                    if 0 <= nota <= 10:
                        calificaciones.append(nota)
                        break
                    else:
                        print("⚠️  La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("⚠️  Por favor, ingresa un número válido.")
        
        # Calcular promedio usando sum()
        suma_total = sum(calificaciones)
        promedio = suma_total / len(calificaciones)
        
        # Mostrar resultados
        print("\n📋 LISTA DE CALIFICACIONES:")
        for idx, nota in enumerate(calificaciones, 1):
            print(f"  {idx}. {nota}")
        
        print(f"\n📊 ESTADÍSTICAS:")
        print(f"  • Cantidad de notas: {len(calificaciones)}")
        print(f"  • Suma total: {suma_total}")
        print(f"  • Promedio: {promedio:.2f}")
        print(f"  • Calificación mínima: {min(calificaciones)}")
        print(f"  • Calificación máxima: {max(calificaciones)}")
        
        # Evaluar desempeño
        if promedio >= 8:
            print(f"  • Desempeño: ⭐ Excelente")
        elif promedio >= 7:
            print(f"  • Desempeño: ✅ Muy Bueno")
        elif promedio >= 6:
            print(f"  • Desempeño: 👍 Bueno")
        else:
            print(f"  • Desempeño: ⚠️  Necesita Mejora")
        
    except ValueError:
        print("⚠️  Error: Por favor, ingresa números válidos.")


def opcion_3_inventario():
    """OPCIÓN 3: Inventario de Productos (Combinación de Listas y Tuplas)"""
    print("\n📦 OPCIÓN 3: INVENTARIO DE PRODUCTOS (LISTAS + TUPLAS)")
    print("-" * 70)
    
    inventario = []
    
    try:
        cantidad = int(input("¿Cuántos productos deseas agregar al inventario?: "))
        
        if cantidad <= 0:
            print("⚠️  Por favor, ingresa un número mayor a 0.")
            return
        
        # Carga dinámica de productos como tuplas
        for i in range(cantidad):
            print(f"\n📝 Producto {i + 1}:")
            id_producto = input("  ID del producto: ").strip()
            descripcion = input("  Descripción: ").strip()
            
            while True:
                try:
                    precio = float(input("  Precio ($): "))
                    if precio < 0:
                        print("⚠️  El precio no puede ser negativo.")
                        continue
                    break
                except ValueError:
                    print("⚠️  Por favor, ingresa un número válido.")
            
            # Crear tupla (ID, Descripción, Precio) y agregar a lista
            producto = (id_producto, descripcion, precio)
            inventario.append(producto)
        
        # Mostrar inventario con desempaquetado (unpacking)
        print("\n" + "="*70)
        print("📋 INVENTARIO COMPLETO:")
        print("="*70)
        
        precio_total = 0
        
        for idx, producto in enumerate(inventario, 1):
            # Desempaquetado: extraer valores de la tupla
            id_prod, desc, precio = producto
            precio_total += precio
            print(f"\n{idx}. ID: {id_prod}")
            print(f"   Descripción: {desc}")
            print(f"   Precio: ${precio:.2f}")
        
        print("\n" + "="*70)
        print(f"💰 PRECIO TOTAL DEL INVENTARIO: ${precio_total:.2f}")
        print(f"📊 Total de productos: {len(inventario)}")
        print(f"💵 Precio promedio por producto: ${precio_total/len(inventario):.2f}")
        print("="*70)
        
    except ValueError:
        print("⚠️  Error: Por favor, ingresa datos válidos.")


def opcion_4_coordenadas():
    """OPCIÓN 4: Coordenadas y Desempaquetado (Tuplas)"""
    print("\n🗺️  OPCIÓN 4: COORDENADAS Y DESEMPAQUETADO (TUPLAS)")
    print("-" * 70)
    
    try:
        # Solicitar coordenadas
        x = float(input("Ingresa la coordenada X: "))
        y = float(input("Ingresa la coordenada Y: "))
        
        # Almacenar en tupla (inmutable)
        coordenada = (x, y)
        print(f"\n✅ Coordenada almacenada: {coordenada}")
        print("   (Las tuplas son INMUTABLES - no se pueden modificar después de crear)")
        
        # Demostrar acceso por índices
        print(f"\n🔍 Acceso mediante índices:")
        print(f"  • Índice 0 (X): {coordenada[0]}")
        print(f"  • Índice 1 (Y): {coordenada[1]}")
        
        # Desempaquetado
        x_val, y_val = coordenada
        print(f"\n📦 Desempaquetado:")
        print(f"  • x_val = {x_val}")
        print(f"  • y_val = {y_val}")
        
        # Intentar modificar (demostrar inmutabilidad)
        print(f"\n⚠️  Intentando modificar la tupla...")
        try:
            coordenada[0] = 10
            print("Esto no debería aparecer...")
        except TypeError as e:
            print(f"❌ ERROR (Esperado): {e}")
            print("   Las tuplas son inmutables y no permiten modificaciones.")
        
        # Calcular distancia desde origen
        import math
        distancia = math.sqrt(x**2 + y**2)
        print(f"\n📐 Cálculos:")
        print(f"  • Distancia desde el origen (0,0): {distancia:.2f} unidades")
        
    except ValueError:
        print("⚠️  Error: Por favor, ingresa números válidos para las coordenadas.")
    except Exception as e:
        print(f"⚠️  Error inesperado: {e}")


def opcion_5_invitados():
    """OPCIÓN 5: Registro de Invitados Únicos (Sets/Conjuntos)"""
    print("\n👥 OPCIÓN 5: REGISTRO DE INVITADOS ÚNICOS (SETS/CONJUNTOS)")
    print("-" * 70)
    
    invitados = set()  # Conjunto para almacenar invitados únicos
    
    print("Ingresa nombres de invitados (escribe 'listo' para terminar).")
    print("💡 Los Sets NO permiten duplicados - se eliminarán automáticamente.\n")
    
    while True:
        nombre = input("Ingresa un nombre (o 'listo' para terminar): ").strip().lower()
        
        if nombre == "listo":
            break
        
        if not nombre:
            print("⚠️  Por favor, ingresa un nombre válido.")
            continue
        
        # Verificar si ya existe usando el operador 'in'
        if nombre in invitados:
            print(f"⚠️  '{nombre}' ya está en la lista de invitados (duplicado ignorado).")
        else:
            # Agregar al conjunto usando add()
            invitados.add(nombre)
            print(f"✅ '{nombre}' agregado a la lista de invitados.")
    
    # Mostrar resultados
    print("\n" + "="*70)
    print("📋 LISTA DE INVITADOS ÚNICOS:")
    print("="*70)
    
    if invitados:
        for idx, invitado in enumerate(sorted(invitados), 1):
            print(f"  {idx}. 👤 {invitado.capitalize()}")
        
        print(f"\n📊 ESTADÍSTICAS:")
        print(f"  • Total de invitados únicos: {len(invitados)}")
        
        # Verificar si un nombre específico está en la lista
        print("\n🔍 Verificar pertenencia:")
        buscar = input("¿Quién deseas buscar?: ").strip().lower()
        
        if buscar in invitados:
            print(f"✅ '{buscar}' SÍ está en la lista de invitados.")
        else:
            print(f"❌ '{buscar}' NO está en la lista de invitados.")
    else:
        print("❌ No se agregó ningún invitado.")
    
    print("="*70)


def ejecutar_asistente():
    """Función principal que ejecuta el programa."""
    nave = "Apolo 11"
    continuar = True
    
    print("\n" + "="*70)
    print("🚀 BIENVENIDO AL ASISTENTE DE MISIÓN ESPACIAL 🚀")
    print("="*70)
    print(f"Nave asignada: {nave}")
    print("="*70)
    
    while continuar:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            opcion_1_playlist()
        elif opcion == "2":
            opcion_2_promedio()
        elif opcion == "3":
            opcion_3_inventario()
        elif opcion == "4":
            opcion_4_coordenadas()
        elif opcion == "5":
            opcion_5_invitados()
        elif opcion == "6":
            print(f"\n🚪 Cerrando conexión desde la nave {nave}.")
            print("👋 ¡Gracias por usar el Asistente de Misión Espacial!")
            print("   ¡Buen viaje! 🌌\n")
            continuar = False
        else:
            print("⚠️  Opción no válida. Por favor, intenta de nuevo.")
    
    print("="*70)


# ═══════════════════════════════════════════════════════════════════════════════
# Punto de entrada del programa
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    ejecutar_asistente()
