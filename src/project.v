/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_mux (
    input  wire [7:0] ui_in,    
    output wire [7:0] uo_out,   
    input  wire [7:0] uio_in,   
    output wire [7:0] uio_out,  
    output wire [7:0] uio_oe,   
    input  wire       ena,      
    input  wire       clk,      
    input  wire       rst_n     
);

  // Inputs
  wire A = ui_in[0];
  wire B = ui_in[1];
  wire S = ui_in[2];

  // MUX logic
  wire Y = S ? B : A;

  // Output mapping
  assign uo_out[0] = Y;
  assign uo_out[7:1] = 7'b0000000;

  // No bidirectional IO used
  assign uio_out = 8'b00000000;
  assign uio_oe  = 8'b00000000;

  // Prevent unused warnings
  wire _unused = &{ena, clk, rst_n, uio_in};

endmodule
