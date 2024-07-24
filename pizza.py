import streamlit as st
import pandas as pd

# Funciones para calcular el total y el cambio
def calcular_total(pedido):
    total = 0
    for item, precio in pedido.items():
        total += precio
    return total

def calcular_cambio(pago, total):
    cambio = pago - total
    return cambio

# Definición de precios
pizzas = {
    "Peperoni": 349.70,
    "Borde queso": 659.25,
    "Mixta": 520.10
}

extras = {
    "Pan de ajo": 250.05,
    "Palitos de queso": 198.10,
    "Refresco grande": 200.10,
    "Refresco pequeño": 70.25
}

# Encabezado de la página
st.title(" ¡Bienvenido a 🍕Pizza el gran T T 👍! ")

# Selección de pizza
pizza_seleccionada = st.selectbox("Elige tu pizza:", list(pizzas.keys()))
precio_pizza = pizzas[pizza_seleccionada]

# Selección de extras
extras_seleccionados = st.multiselect("Elige tus extras (opcional):", list(extras.keys()))
precio_extras = 0
for extra in extras_seleccionados:
    precio_extras += extras[extra]

# Cálculo del total
total = precio_pizza + precio_extras
st.markdown(f"**Total:** ${total:.2f}")

# Pago e impresión del recibo
pago = st.number_input("Ingrese su pago:")

if pago >= total:
    cambio = calcular_cambio(pago, total)
    pedido = {
        "Pizza": pizza_seleccionada,
        "Extras": extras_seleccionados,
        "Total": total,
        "Pago": pago,
        "Cambio": cambio
    }

    df_pedido = pd.DataFrame.from_dict(pedido, orient="index", columns=["Valor"])
    df_pedido.index = df_pedido.index.set_names(["Detalle"])
    st.markdown("** Factura **")
    st.table(df_pedido)
    st.markdown(f"**¡Buen provecho! Regrese pronto **")
else:
    st.error(f"Su pago (${pago:.2f}) es insuficiente. El total es de ${total:.2f}")
