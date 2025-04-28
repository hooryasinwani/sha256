import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
import random

@cocotb.test()
async def test_sha2_top_basic(dut):
    """Basic test for sha2_top."""

    
    clock = Clock(dut.clk, 10, units="ns") 
    cocotb.start_soon(clock.start())

   
    dut.src_ready.value = 1
    dut.din.value = 0x00000001
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert dut.dout.value != 0

@cocotb.test()
async def test_sha2_top_multiple_inputs(dut):
    """Test for multiple different inputs to SHA256."""

    
    clock = Clock(dut.clk, 10, units="ns")  
    cocotb.start_soon(clock.start())

    
    dut.src_ready.value = 1
    dut.din.value = 0xdeadbeef
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert dut.dout.value != 0 

    
    dut.din.value = 0x01234567
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert dut.dout.value != 0 

@cocotb.test()
async def test_sha2_top_edge_cases(dut):
    """Test edge cases for sha2_top."""

   
    clock = Clock(dut.clk, 10, units="ns")  
    cocotb.start_soon(clock.start())

    dut.src_ready.value = 1
    dut.din.value = 0x00000000  
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert dut.dout.value != 0 

    dut.din.value = 0xFFFFFFFF  
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert dut.dout.value != 0 

 
    dut.din.value = 0xFFFFFFFF  
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert dut.dout.value != 0 

@cocotb.test()
async def test_sha2_top_random_inputs(dut):
    """Test with random inputs to check randomness."""

   
    clock = Clock(dut.clk, 10, units="ns")  
    cocotb.start_soon(clock.start())

    
    for _ in range(5):
        dut.src_ready.value = 1
        dut.din.value = random.getrandbits(32)  
        await RisingEdge(dut.clk)
        await RisingEdge(dut.clk)
        assert dut.dout.value != 0 

async def test_sha2_top_control_signals(dut):
    """Test with different control signals."""
   
    dut.src_ready <= 0
    
    
    await RisingEdge(dut.clk)
    
  
    assert dut.dout.value == 0, f"Output dout should be zero when src_ready is disabled, but got {dut.dout.value}"

    


async def test_sha2_top_reset_behavior(dut):
    
    

    dut.rst_n <= 0 
    
 
    await RisingEdge(dut.clk)
    
  
    dut.rst_n <= 1

 
    await RisingEdge(dut.clk)

   
    assert dut.dout.value == 0, f"After reset, dout should be 0, but got {dut.dout.value}"

