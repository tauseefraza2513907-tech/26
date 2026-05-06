import gradio as gr
import numpy as np

# Beam deflection formulas
def beam_deflection(load_type, E, I, L, P=0, w=0, x=0):
    try:
        E = float(E)
        I = float(I)
        L = float(L)
        x = float(x)

        if load_type == "Point Load (Center)":
            P = float(P)
            # Max deflection at center
            delta = (P * L**3) / (48 * E * I)

        elif load_type == "Uniformly Distributed Load (UDL)":
            w = float(w)
            # Max deflection at center
            delta = (5 * w * L**4) / (384 * E * I)

        else:
            return "Invalid Load Type"

        return f"Maximum Deflection = {delta:.6e} meters"

    except:
        return "Error: Please enter valid numeric values"


# Gradio UI
with gr.Blocks() as app:
    gr.Markdown("# 🔧 Beam Deflection Calculator")
    gr.Markdown("Calculate maximum deflection of a simply supported beam")

    load_type = gr.Dropdown(
        ["Point Load (Center)", "Uniformly Distributed Load (UDL)"],
        label="Select Load Type"
    )

    E = gr.Textbox(label="Young's Modulus (Pa)")
    I = gr.Textbox(label="Moment of Inertia (m⁴)")
    L = gr.Textbox(label="Beam Length (m)")
    x = gr.Textbox(label="Position x (optional)", value="0")

    P = gr.Textbox(label="Point Load P (N)", value="0")
    w = gr.Textbox(label="UDL w (N/m)", value="0")

    output = gr.Textbox(label="Result")

    btn = gr.Button("Calculate")

    btn.click(
        beam_deflection,
        inputs=[load_type, E, I, L, P, w, x],
        outputs=output
    )

app.launch()
