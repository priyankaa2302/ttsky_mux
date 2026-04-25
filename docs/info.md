<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements a **2:1 multiplexer (MUX)** in Verilog.

The MUX selects one of two input signals based on a select line.

### Input mapping:
- `ui_in[0]` → Input A
- `ui_in[1]` → Input B
- `ui_in[2]` → Select signal (S)

### Output mapping:
- `uo_out[0]` → Output Y

### Operation:
- When `S = 0`, the output `Y` follows input `A`
- When `S = 1`, the output `Y` follows input `B`

## How to test

Set inputs using `ui_in`:
- `ui_in[0]` = A  
- `ui_in[1]` = B  
- `ui_in[2]` = S  

Wait briefly and check `uo_out[0]`.

### Expected behavior:
- If `S = 0` → output = A  
- If `S = 1` → output = B
Try all combinations of A, B, and S to verify correct MUX operation.

## External hardware

No External Hardware is used.
