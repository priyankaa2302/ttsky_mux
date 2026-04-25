import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mux(dut):
    dut._log.info("Start MUX Test (Timer-based)")

    # Initialize
    dut.ena.value = 1
    dut.rst_n.value = 1  # no reset needed for combinational logic
    dut.uio_in.value = 0

    test_cases = [
        (0, 0, 0, 0),  # A B S Y
        (1, 0, 0, 1),
        (0, 1, 0, 0),
        (1, 1, 0, 1),
        (0, 0, 1, 0),
        (1, 0, 1, 0),
        (0, 1, 1, 1),
        (1, 1, 1, 1),
    ]

    for a, b, s, expected in test_cases:

        # Pack inputs into ui_in
        dut.ui_in.value = (s << 2) | (b << 1) | a

        # allow propagation delay
        await Timer(10, units="ns")

        actual = int(dut.uo_out.value) & 1

        assert actual == expected, (
            f"FAIL: A={a} B={b} S={s} → Got {actual}, Expected {expected}"
        )

        dut._log.info(f"PASS: A={a}, B={b}, S={s} → Y={actual}")
