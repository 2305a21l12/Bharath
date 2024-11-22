import streamlit as st
import math

# Define the Tran_OC function
def Tran_OC(V0, I0, W0):
    """
    Calculate resistance (R0) and reactance (X0) of a transformer based on open circuit test measurements.
    
    Parameters:
        V0 (float): Open circuit voltage
        I0 (float): Open circuit current
        W0 (float): Power in watts
    
    Returns:
        tuple: R0 (float), X0 (float)
    """
    # Calculate No-Load Power Factor (NPF)
    NPF = W0 / (V0 * I0)
    
    # Calculate magnetizing current (Iµ)
    Imu = I0 * math.sqrt(1 - NPF**2)
    
    # Calculate active current (Iw)
    Iw = I0 * NPF
    
    # Calculate R0 and X0
    R0 = V0 / Iw
    X0 = V0 / Imu
    
    return R0, X0

# Streamlit Web Application
st.title("2305A21L12-PS7")

st.header("Calculate Transformer Resistance (R0) and Reactance (X0)")

# Input fields
V0 = st.number_input("Enter Open Circuit Voltage (V0) in volts:", min_value=0.0, step=0.1)
I0 = st.number_input("Enter Open Circuit Current (I0) in amperes:", min_value=0.0, step=0.1)
W0 = st.number_input("Enter Power (W0) in watts:", min_value=0.0, step=0.1)

# Calculate button
if st.button("Calculate"):
    if V0 > 0 and I0 > 0 and W0 > 0:
        R0, X0 = Tran_OC(V0, I0, W0)
        st.success(f"Calculated Results:\n\nResistance (R0): {R0:.2f} Ω\nReactance (X0): {X0:.2f} Ω")
    else:
        st.error("Please enter positive values for V0, I0, and W0.")