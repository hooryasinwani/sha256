

TOPLEVEL_LANG = verilog
SIM = icarus  

VERILOG_SOURCES = sha2_single.v  
TOPLEVEL = sha2_top  
MODULE = sha256cocotb  


include $(shell cocotb-config --makefiles)/Makefile.sim 
