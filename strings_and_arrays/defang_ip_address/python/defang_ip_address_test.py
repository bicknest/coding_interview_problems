from defang_ip_address import defang_ip_address

def test_defang_ip_address():
    address = "1.1.1.1"
    defanged = defang_ip_address(address)
    assert defanged == "1[.]1[.]1[.]1"
