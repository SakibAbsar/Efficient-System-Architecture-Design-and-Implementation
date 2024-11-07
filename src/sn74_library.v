// SN74 Logic Series Library
module AND_gate(output Y, input A, B);
   assign Y = A & B;
endmodule

module OR_gate(output Y, input A, B);
   assign Y = A | B;
endmodule

module NOT_gate(output Y, input A);
   assign Y = ~A;
endmodule
